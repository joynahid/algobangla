#!/usr/bin/env python3
"""
set_weights.py - Convert MkDocs literate-nav navigation to Hugo-book weight frontmatter.

Parses navigation.md and assigns weight values to Hugo content files based on
their order in the navigation. Section _index.md files get weights based on
their section's position. Subsection _index.md files are created as needed.

Usage:
    python set_weights.py [--dry-run] [--nav PATH] [--content PATH]
"""

import re
import sys
import os
import argparse
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Navigation parser
# ---------------------------------------------------------------------------

def parse_navigation(nav_path: Path) -> list[dict]:
    """
    Parse navigation.md and return a flat list of entries with metadata.

    Each entry is a dict with keys:
      - type: "section" | "subsection" | "page"
      - title: str
      - path: str | None  (only for "page")
      - section_weight: int   (1-based index * 10 among top-level sections)
      - subsection_weight: int (1-based index * 10 within its section)
      - page_weight: int      (1-based index * 10 within its subsection/section)
      - section_name: str
      - subsection_name: str | None
      - section_dir: str | None   (derived from first page path in section)
    """
    text = nav_path.read_text(encoding="utf-8")

    entries = []
    current_section = None
    current_subsection = None
    section_counter = 0
    subsection_counter = 0
    page_counter = 0

    # Track section dirs — inferred from the first page in each section
    section_dir_map: dict[str, Optional[str]] = {}  # section_name -> dir

    for line in text.splitlines():
        stripped = line.lstrip()
        if not stripped.startswith("- "):
            continue

        indent = len(line) - len(stripped)
        item = stripped[2:].strip()  # remove "- "

        # Match a page link: [Title](path)
        link_match = re.match(r'^\[(.+?)\]\((.+?)\)$', item)

        if indent == 0:
            # Top-level section (e.g. "- Algebra")
            if link_match:
                # Top-level page (unusual, e.g. Home items listed flat)
                # Treat as a section by itself with no subsection
                section_counter += 1
                subsection_counter = 0
                page_counter = 1
                section_name = link_match.group(1)
                page_path = link_match.group(2)
                current_section = section_name
                current_subsection = None
                entries.append({
                    "type": "page",
                    "title": section_name,
                    "path": page_path,
                    "section_weight": section_counter * 10,
                    "subsection_weight": 0,
                    "page_weight": page_counter * 10,
                    "section_name": section_name,
                    "subsection_name": None,
                })
                page_counter += 1
            else:
                section_counter += 1
                subsection_counter = 0
                page_counter = 0
                current_section = item
                current_subsection = None
                entries.append({
                    "type": "section",
                    "title": item,
                    "path": None,
                    "section_weight": section_counter * 10,
                    "subsection_weight": 0,
                    "page_weight": 0,
                    "section_name": item,
                    "subsection_name": None,
                })

        elif indent == 4:
            # Either a subsection header or a direct page under a section
            if link_match:
                # Direct page under a section (no subsection)
                page_counter += 1
                page_path = link_match.group(2)
                entries.append({
                    "type": "page",
                    "title": link_match.group(1),
                    "path": page_path,
                    "section_weight": section_counter * 10,
                    "subsection_weight": 0,
                    "page_weight": page_counter * 10,
                    "section_name": current_section,
                    "subsection_name": None,
                })
            else:
                # Subsection header
                subsection_counter += 1
                page_counter = 0
                current_subsection = item
                entries.append({
                    "type": "subsection",
                    "title": item,
                    "path": None,
                    "section_weight": section_counter * 10,
                    "subsection_weight": subsection_counter * 10,
                    "page_weight": 0,
                    "section_name": current_section,
                    "subsection_name": item,
                })

        elif indent == 8:
            # Page under a subsection
            if link_match:
                page_counter += 1
                page_path = link_match.group(2)
                entries.append({
                    "type": "page",
                    "title": link_match.group(1),
                    "path": page_path,
                    "section_weight": section_counter * 10,
                    "subsection_weight": subsection_counter * 10,
                    "page_weight": page_counter * 10,
                    "section_name": current_section,
                    "subsection_name": current_subsection,
                })

    return entries


# ---------------------------------------------------------------------------
# Path utilities
# ---------------------------------------------------------------------------

def nav_path_to_content_path(nav_path_str: str, content_dir: Path) -> Path:
    """Convert a navigation.md path like 'algebra/fft.md' to an absolute content path."""
    return content_dir / nav_path_str


def get_section_dir_from_path(path_str: str) -> Optional[str]:
    """Extract the top-level directory from a path like 'algebra/fft.md' -> 'algebra'."""
    parts = Path(path_str).parts
    if len(parts) >= 2:
        return parts[0]
    return None


def build_section_dir_map(entries: list[dict]) -> dict[str, str]:
    """
    Map each section name to its filesystem directory,
    inferred by majority-vote among all page paths in that section.
    Falls back to the first page's directory if there's a tie.
    """
    from collections import Counter

    # Count directory occurrences per section
    dir_counts: dict[str, Counter] = {}
    first_dir: dict[str, str] = {}

    for e in entries:
        if e["type"] == "page" and e["path"]:
            sec = e["section_name"]
            if sec:
                d = get_section_dir_from_path(e["path"])
                if d:
                    if sec not in dir_counts:
                        dir_counts[sec] = Counter()
                        first_dir[sec] = d
                    dir_counts[sec][d] += 1

    result: dict[str, str] = {}
    for sec, counts in dir_counts.items():
        # Pick the most common directory for this section
        most_common = counts.most_common(1)
        if most_common:
            result[sec] = most_common[0][0]
        else:
            result[sec] = first_dir[sec]

    return result


def build_subsection_dir_map(entries: list[dict]) -> dict[tuple[str, str], str]:
    """
    Map (section_name, subsection_name) -> subdirectory (majority-vote).

    In practice, source files for a section are flat in one dir (e.g., algebra/),
    so subsections are logical groupings, not actual directories.
    """
    from collections import Counter

    dir_counts: dict[tuple[str, str], Counter] = {}
    for e in entries:
        if e["type"] == "page" and e["path"] and e["subsection_name"]:
            key = (e["section_name"], e["subsection_name"])
            d = get_section_dir_from_path(e["path"])
            if d:
                if key not in dir_counts:
                    dir_counts[key] = Counter()
                dir_counts[key][d] += 1

    result: dict[tuple[str, str], str] = {}
    for key, counts in dir_counts.items():
        most_common = counts.most_common(1)
        if most_common:
            result[key] = most_common[0][0]
    return result


def build_section_all_dirs(entries: list[dict]) -> dict[str, list[str]]:
    """
    Map section_name -> sorted list of all unique directories used by pages in that section.
    Used for multi-directory sections (e.g., Miscellaneous spans sequences/, others/, etc.)
    """
    from collections import OrderedDict

    dirs_seen: dict[str, list[str]] = {}
    for e in entries:
        if e["type"] == "page" and e["path"]:
            sec = e["section_name"]
            d = get_section_dir_from_path(e["path"])
            if sec and d:
                if sec not in dirs_seen:
                    dirs_seen[sec] = []
                if d not in dirs_seen[sec]:
                    dirs_seen[sec].append(d)
    return dirs_seen


# ---------------------------------------------------------------------------
# Frontmatter manipulation
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)


def read_frontmatter(content: str) -> tuple[dict[str, str], str]:
    """
    Parse YAML frontmatter from a markdown string.
    Returns (frontmatter_dict, body_after_frontmatter).
    Only handles simple key: value pairs (sufficient for our use-case).
    """
    match = FRONTMATTER_RE.match(content)
    if not match:
        return {}, content

    fm_text = match.group(1)
    body = content[match.end():]

    fm: dict[str, str] = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()

    return fm, body


def write_frontmatter(fm: dict[str, str], body: str) -> str:
    """Serialize frontmatter dict + body back to a markdown string."""
    lines = ["---"]
    for key, val in fm.items():
        lines.append(f"{key}: {val}")
    lines.append("---")
    lines.append("")  # blank line after frontmatter
    return "\n".join(lines) + body


def upsert_frontmatter_field(file_path: Path, key: str, value: str, dry_run: bool = False) -> bool:
    """
    Read a markdown file, set/update a frontmatter field, write back.
    Returns True if the file was modified, False if skipped/not found.
    """
    if not file_path.exists():
        return False

    original = file_path.read_text(encoding="utf-8")
    fm, body = read_frontmatter(original)

    fm[key] = value

    updated = write_frontmatter(fm, body)
    if updated == original:
        return False

    if not dry_run:
        file_path.write_text(updated, encoding="utf-8")
    return True


def upsert_multiple_fields(file_path: Path, updates: dict[str, str], dry_run: bool = False) -> bool:
    """
    Read a markdown file, set/update multiple frontmatter fields at once, write back.
    Preserves existing fields not in `updates`.
    Returns True if file was modified.
    """
    if not file_path.exists():
        return False

    original = file_path.read_text(encoding="utf-8")
    fm, body = read_frontmatter(original)

    changed = False
    for k, v in updates.items():
        if fm.get(k) != v:
            fm[k] = v
            changed = True

    if not changed:
        return False

    updated = write_frontmatter(fm, body)
    if not dry_run:
        file_path.write_text(updated, encoding="utf-8")
    return True


def create_index_file(file_path: Path, title: str, weight: int,
                      collapse: bool = True, dry_run: bool = False) -> bool:
    """
    Create a section _index.md file if it doesn't exist.
    If it exists, update its weight and bookCollapseSection.
    Returns True if file was created or modified.
    """
    updates = {
        "title": f'"{title}"',
        "weight": str(weight),
        "bookCollapseSection": str(collapse).lower(),
    }

    if file_path.exists():
        return upsert_multiple_fields(file_path, updates, dry_run)

    # Create new file
    fm_lines = ["---"]
    for k, v in updates.items():
        fm_lines.append(f"{k}: {v}")
    fm_lines.append("---")
    fm_lines.append("")
    fm_lines.append(f"# {title}")
    fm_lines.append("")

    content = "\n".join(fm_lines)
    if not dry_run:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process(nav_path: Path, content_dir: Path, dry_run: bool = False) -> None:
    print(f"Parsing navigation: {nav_path}")
    entries = parse_navigation(nav_path)

    section_dir_map = build_section_dir_map(entries)
    section_all_dirs = build_section_all_dirs(entries)
    subsection_dir_map = build_subsection_dir_map(entries)

    print(f"Found {len(entries)} navigation entries")
    print(f"Section->primary dir map: {section_dir_map}")
    print(f"Section->all dirs map:    {section_all_dirs}")
    print()

    stats = {"pages_updated": 0, "pages_skipped": 0, "pages_missing": 0,
             "sections_updated": 0, "subsections_updated": 0}

    # --- Track which sections and subsections we've already processed ---
    processed_sections: set[str] = set()
    processed_subsections: set[tuple[str, str]] = set()

    for entry in entries:
        etype = entry["type"]
        section_name = entry["section_name"]
        subsection_name = entry["subsection_name"]
        section_weight = entry["section_weight"]
        subsection_weight = entry["subsection_weight"]

        # -- Handle section _index.md --
        if etype == "section" and section_name not in processed_sections:
            processed_sections.add(section_name)
            all_dirs = section_all_dirs.get(section_name, [])
            primary_dir = section_dir_map.get(section_name)

            if not all_dirs:
                print(f"  SECTION  [{section_weight:4d}] {section_name!r} — no dir found, skipping _index.md")
            elif len(all_dirs) == 1:
                # Single-directory section: create one _index.md
                index_path = content_dir / primary_dir / "_index.md"
                modified = create_index_file(
                    index_path, section_name, section_weight, collapse=True, dry_run=dry_run
                )
                status = "updated/created" if modified else "unchanged"
                print(f"  SECTION  [{section_weight:4d}] {primary_dir}/_index.md  ({status})")
                stats["sections_updated"] += 1 if modified else 0
            else:
                # Multi-directory section (e.g. Miscellaneous spans sequences/, others/, etc.)
                # Create _index.md only in directories not already claimed by another section.
                # Directories already processed (belong to another section) are skipped.
                print(f"  SECTION  [{section_weight:4d}] {section_name!r} spans {all_dirs}")
                sub_idx = 0
                for d in all_dirs:
                    # Check if this dir is already the primary dir of a previously processed section
                    already_claimed = any(
                        section_dir_map.get(prev_sec) == d and prev_sec != section_name
                        for prev_sec in processed_sections
                    )
                    if already_claimed:
                        print(f"  SECTION  [skip] {d}/_index.md — already owned by another section")
                        continue
                    sub_weight = section_weight + sub_idx
                    sub_idx += 1
                    index_path = content_dir / d / "_index.md"
                    # Use the directory name as title if it's not the primary
                    dir_title = section_name if d == primary_dir else d.replace("_", " ").title()
                    modified = create_index_file(
                        index_path, dir_title, sub_weight, collapse=True, dry_run=dry_run
                    )
                    status = "updated/created" if modified else "unchanged"
                    print(f"  SECTION  [{sub_weight:4d}] {d}/_index.md  ({status})")
                    stats["sections_updated"] += 1 if modified else 0

        # -- Handle subsection: create a logical _index.md within the section dir --
        # hugo-book supports nested dirs for 2-level nav. Since the source files
        # for a section are all flat in one dir (e.g. algebra/), we use the
        # subsection as a logical grouping. We DO NOT create subdirectories unless
        # they actually exist in the content tree; instead we record the subsection
        # weight on a virtual _index placeholder if the dir exists.
        if etype == "subsection" and subsection_name and (section_name, subsection_name) not in processed_subsections:
            processed_subsections.add((section_name, subsection_name))
            sec_dir = section_dir_map.get(section_name)
            if sec_dir:
                # Check if there's a subdirectory for this subsection
                # (future-proof: if a parallel agent creates subdirs)
                sub_slug = re.sub(r'[^a-z0-9]+', '-', subsection_name.lower()).strip('-')
                sub_dir = content_dir / sec_dir / sub_slug
                if sub_dir.exists() and sub_dir.is_dir():
                    index_path = sub_dir / "_index.md"
                    modified = create_index_file(
                        index_path, subsection_name, subsection_weight, collapse=True, dry_run=dry_run
                    )
                    status = "updated/created" if modified else "unchanged"
                    print(f"  SUBSECT  [{subsection_weight:4d}] {sec_dir}/{sub_slug}/_index.md  ({status})")
                    stats["subsections_updated"] += 1 if modified else 0
                else:
                    print(f"  SUBSECT  [{subsection_weight:4d}] {section_name}/{subsection_name!r} "
                          f"— no subdir '{sub_slug}', weight noted only")

        # -- Handle page --
        if etype == "page" and entry["path"]:
            page_path_str = entry["path"]
            page_weight = entry["page_weight"]
            content_path = nav_path_to_content_path(page_path_str, content_dir)

            if content_path.exists():
                modified = upsert_frontmatter_field(content_path, "weight", str(page_weight), dry_run)
                status = "updated" if modified else "unchanged"
                print(f"  PAGE     [{page_weight:4d}] {page_path_str}  ({status})")
                if modified:
                    stats["pages_updated"] += 1
                else:
                    stats["pages_skipped"] += 1
            else:
                print(f"  PAGE     [{page_weight:4d}] {page_path_str}  (MISSING — file not found)")
                stats["pages_missing"] += 1

    print()
    print("=" * 60)
    print("Summary:")
    print(f"  Pages updated:         {stats['pages_updated']}")
    print(f"  Pages already correct: {stats['pages_skipped']}")
    print(f"  Pages missing:         {stats['pages_missing']}")
    print(f"  Sections updated:      {stats['sections_updated']}")
    print(f"  Subsections processed: {stats['subsections_updated']}")
    print("=" * 60)

    if stats["pages_missing"] > 0:
        print()
        print("NOTE: Missing files are expected if content migration is still in progress.")
        print("Re-run this script after all content files are created.")


# ---------------------------------------------------------------------------
# hugo.toml update
# ---------------------------------------------------------------------------

def update_hugo_toml(toml_path: Path, dry_run: bool = False) -> None:
    """
    Ensure hugo.toml uses filesystem-based navigation (hugo-book default).
    - Remove any [[menu.main]] entries
    - Ensure BookMenuFromSection is not set to a specific leaf (use "/" for root)
    - Ensure BookSection covers all top-level sections (set to "/" or remove)
    """
    if not toml_path.exists():
        print(f"hugo.toml not found at {toml_path}, skipping")
        return

    original = toml_path.read_text(encoding="utf-8")
    updated = original

    # Remove [[menu.main]] blocks
    menu_block_re = re.compile(
        r'\[\[menu\.main\]\][^\[]*',
        re.DOTALL
    )
    if menu_block_re.search(updated):
        updated = menu_block_re.sub('', updated)
        print("  hugo.toml: removed [[menu.main]] entries")

    # Update BookSection from a specific section to "/" so all top-level sections appear
    book_section_re = re.compile(r'(BookSection\s*=\s*)"[^"]*"')
    if book_section_re.search(updated):
        updated = book_section_re.sub(r'\1"/"', updated)
        print("  hugo.toml: updated BookSection to \"/\"")

    if updated == original:
        print("  hugo.toml: no changes needed")
        return

    if not dry_run:
        toml_path.write_text(updated, encoding="utf-8")
        print("  hugo.toml: written")
    else:
        print("  hugo.toml: (dry-run, not written)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--nav",
        default=str(Path(__file__).parent.parent.parent / "cp-algorithms" / "src" / "navigation.md"),
        help="Path to navigation.md"
    )
    parser.add_argument(
        "--content",
        default=str(Path(__file__).parent.parent / "hugo" / "content"),
        help="Path to Hugo content directory"
    )
    parser.add_argument(
        "--toml",
        default=str(Path(__file__).parent.parent / "hugo" / "hugo.toml"),
        help="Path to hugo.toml"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without writing files"
    )
    args = parser.parse_args()

    nav_path = Path(args.nav)
    content_dir = Path(args.content)
    toml_path = Path(args.toml)

    if not nav_path.exists():
        print(f"ERROR: navigation.md not found at {nav_path}", file=sys.stderr)
        sys.exit(1)

    if not content_dir.exists():
        print(f"WARNING: content directory not found at {content_dir}", file=sys.stderr)
        print("Creating content directory...")
        if not args.dry_run:
            content_dir.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print("DRY RUN — no files will be modified")
        print()

    print("--- Updating hugo.toml ---")
    update_hugo_toml(toml_path, dry_run=args.dry_run)
    print()

    print("--- Setting page/section weights ---")
    process(nav_path, content_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
