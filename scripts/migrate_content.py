#!/usr/bin/env python3
"""
Migration script: cp-algorithms MkDocs -> Hugo (hugo-book theme)
"""

import os
import re
import shutil
from pathlib import Path

SRC_DIR = Path("D:/Projects/cp-algorithms-hugo/src")
HUGO_CONTENT = Path("D:/Projects/cp-algorithms-hugo/hugo/content")
HUGO_STATIC = Path("D:/Projects/cp-algorithms-hugo/hugo/static")

# Sections to migrate (dir name -> display name)
SECTIONS = {
    "algebra": "Algebra",
    "combinatorics": "Combinatorics",
    "data_structures": "Data Structures",
    "dynamic_programming": "Dynamic Programming",
    "game_theory": "Game Theory",
    "geometry": "Geometry",
    "graph": "Graphs",
    "linear_algebra": "Linear Algebra",
    "num_methods": "Numerical Methods",
    "others": "Miscellaneous",
    "schedules": "Schedules",
    "sequences": "Sequences",
    "string": "String Processing",
}

# Section weights derived from navigation.md order
SECTION_WEIGHTS = {
    "algebra": 10,
    "data_structures": 20,
    "dynamic_programming": 30,
    "string": 40,
    "linear_algebra": 50,
    "combinatorics": 60,
    "num_methods": 70,
    "geometry": 80,
    "graph": 90,
    "sequences": 100,
    "game_theory": 110,
    "schedules": 120,
    "others": 130,
}

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}

stats = {
    "files_migrated": 0,
    "images_copied": 0,
    "errors": [],
    "complex_admonitions": [],  # files needing manual review
}


# ──────────────────────────────────────────────
# Admonition / shortcode conversion
# ──────────────────────────────────────────────

ADMONITION_TYPE_MAP = {
    "note": "info",
    "info": "info",
    "tip": "tip",
    "warning": "warning",
    "danger": "danger",
    "example": "info",
    "abstract": "info",
    "success": "tip",
    "question": "info",
    "failure": "danger",
    "bug": "danger",
    "quote": "info",
    "seealso": "info",
}


def convert_admonitions(content: str, filepath: str) -> str:
    """
    Convert MkDocs admonitions (!!!) and collapsible details (???) to Hugo shortcodes.
    Handles multi-line indented content blocks.
    """
    lines = content.split("\n")
    out = []
    i = 0
    had_complex = False

    while i < len(lines):
        line = lines[i]

        # Match !!! type "Title" or !!! type
        m_admon = re.match(r'^(!!!)\s+(\w+)(?:\s+"([^"]*)")?(?:\s+"")?$', line)
        # Match ??? type "Title" or ??? type
        m_detail = re.match(r'^(\?\?\?)\s+(\w+)(?:\s+"([^"]*)")?(?:\s+"")?$', line)

        match = m_admon or m_detail
        if match:
            is_detail = bool(m_detail)
            admon_type_raw = match.group(2).lower()
            title = match.group(3) if match.group(3) else admon_type_raw.capitalize()
            hugo_type = ADMONITION_TYPE_MAP.get(admon_type_raw, "info")

            # Collect indented body lines (4 spaces)
            body_lines = []
            i += 1
            while i < len(lines) and (lines[i].startswith("    ") or lines[i].strip() == ""):
                body_lines.append(lines[i])
                i += 1

            # Strip 4-space indent
            body = "\n".join(l[4:] if l.startswith("    ") else l for l in body_lines).rstrip()

            if is_detail:
                out.append(f'{{{{< details "{title}" >}}}}')
                if body:
                    out.append(body)
                out.append("{{< /details >}}")
            else:
                out.append(f"{{{{< hint {hugo_type} >}}}}")
                out.append(f"**{title}**")
                if body:
                    out.append("")
                    out.append(body)
                out.append("{{< /hint >}}")

            if any("    " in bl for bl in body_lines if bl.startswith("    ")):
                had_complex = True
            continue

        out.append(line)
        i += 1

    if had_complex:
        stats["complex_admonitions"].append(filepath)

    return "\n".join(out)


# ──────────────────────────────────────────────
# Tabbed content → bold headers
# ──────────────────────────────────────────────

def convert_tabs(content: str) -> str:
    """
    Convert === "Tab Name" to **Tab Name** headers.
    Indented code block lines (4 spaces under a tab) lose one level of indent.
    """
    lines = content.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^=== "(.+)"$', line)
        if m:
            tab_name = m.group(1)
            out.append(f"\n**{tab_name}**\n")
            i += 1
            # Consume indented block (4 spaces) and de-indent by 4
            while i < len(lines) and (lines[i].startswith("    ") or lines[i].strip() == ""):
                body_line = lines[i]
                if body_line.startswith("    "):
                    out.append(body_line[4:])
                else:
                    out.append(body_line)
                i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


# ──────────────────────────────────────────────
# Image reference updates
# ──────────────────────────────────────────────

def update_image_refs(content: str, section: str) -> str:
    """
    Rewrite relative image references to /images/<section>/filename.
    Handles both markdown ![alt](img.png) and HTML <img src="img.png"> forms.
    """
    # Markdown images: ![alt](path/to/image.ext)
    def rewrite_md_img(m):
        alt = m.group(1)
        path = m.group(2)
        # Skip if already absolute or external
        if path.startswith("http") or path.startswith("/"):
            return m.group(0)
        filename = Path(path).name
        return f"![{alt}](/images/{section}/{filename})"

    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', rewrite_md_img, content)

    # HTML img tags
    def rewrite_html_img(m):
        full = m.group(0)
        src = m.group(1)
        if src.startswith("http") or src.startswith("/"):
            return full
        filename = Path(src).name
        return full.replace(src, f"/images/{section}/{filename}")

    content = re.sub(r'<img\s[^>]*src="([^"]+)"', rewrite_html_img, content)

    return content


# ──────────────────────────────────────────────
# Frontmatter handling
# ──────────────────────────────────────────────

def extract_frontmatter(content: str):
    """Return (frontmatter_dict_str, body) tuple."""
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            fm = content[3:end].strip()
            body = content[end + 4:].lstrip("\n")
            return fm, body
    return "", content


def add_title_to_frontmatter(fm: str, body: str) -> str:
    """
    If frontmatter has no 'title:', try to extract it from the first H1 in body.
    """
    if "title:" in fm:
        return fm
    m = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    if m:
        title = m.group(1).strip().replace('"', '\\"')
        return f'title: "{title}"\n{fm}'
    return fm


# ──────────────────────────────────────────────
# Transform a single markdown file
# ──────────────────────────────────────────────

def transform_md(content: str, section: str, filepath: str) -> str:
    fm_raw, body = extract_frontmatter(content)
    fm_raw = add_title_to_frontmatter(fm_raw, body)

    # Remove MkDocs-specific frontmatter keys
    fm_lines = fm_raw.split("\n")
    skip_keys = {"e_maxx_link", "search"}
    clean_fm_lines = [l for l in fm_lines if not any(l.startswith(k + ":") for k in skip_keys)]
    fm_clean = "\n".join(clean_fm_lines).strip()

    # Process body
    body = convert_admonitions(body, filepath)
    body = convert_tabs(body)
    body = update_image_refs(body, section)

    # Remove MkDocs HTML comment title hints  <!--?title ... -->
    body = re.sub(r'<!--\?title[^>]*-->\n?', '', body)

    result = f"---\n{fm_clean}\n---\n\n{body}"
    return result


# ──────────────────────────────────────────────
# Create section _index.md
# ──────────────────────────────────────────────

def create_section_index(section: str, title: str, dest_dir: Path):
    weight = SECTION_WEIGHTS.get(section, 999)
    index_path = dest_dir / "_index.md"
    # Don't overwrite if it already exists and has content
    if index_path.exists():
        return
    index_path.write_text(
        f'---\ntitle: "{title}"\nbookCollapseSection: true\nweight: {weight}\n---\n',
        encoding="utf-8"
    )


# ──────────────────────────────────────────────
# Copy images for a section
# ──────────────────────────────────────────────

def copy_images(section: str, src_section_dir: Path):
    images_dest = HUGO_STATIC / "images" / section
    images_dest.mkdir(parents=True, exist_ok=True)
    for f in src_section_dir.iterdir():
        if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS:
            dest = images_dest / f.name
            shutil.copy2(f, dest)
            stats["images_copied"] += 1


# ──────────────────────────────────────────────
# Migrate a section
# ──────────────────────────────────────────────

def migrate_section(section: str, title: str):
    src_section = SRC_DIR / section
    dest_section = HUGO_CONTENT / section

    if not src_section.exists():
        stats["errors"].append(f"Source dir not found: {src_section}")
        return

    dest_section.mkdir(parents=True, exist_ok=True)
    create_section_index(section, title, dest_section)
    copy_images(section, src_section)

    for src_file in src_section.glob("*.md"):
        dest_file = dest_section / src_file.name
        try:
            content = src_file.read_text(encoding="utf-8")
            transformed = transform_md(content, section, str(src_file))
            dest_file.write_text(transformed, encoding="utf-8")
            stats["files_migrated"] += 1
        except Exception as e:
            stats["errors"].append(f"Error processing {src_file}: {e}")


# ──────────────────────────────────────────────
# Migrate top-level files
# ──────────────────────────────────────────────

def migrate_toplevel():
    # index.md → skip, _index.md is managed manually
    src_index = SRC_DIR / "index.md"
    dest_index = HUGO_CONTENT / "_index.md"
    if False and src_index.exists():  # skipped: root _index.md is manually maintained
        try:
            content = src_index.read_text(encoding="utf-8")
            transformed = transform_md(content, "", str(src_index))
            dest_index.write_text(transformed, encoding="utf-8")
            stats["files_migrated"] += 1
        except Exception as e:
            stats["errors"].append(f"Error processing index.md: {e}")
    else:
        stats["errors"].append("index.md not found in src/")

    # contrib.md and code_of_conduct.md → content/
    for fname in ["contrib.md", "code_of_conduct.md"]:
        src_f = SRC_DIR / fname
        dest_f = HUGO_CONTENT / fname
        if src_f.exists():
            try:
                content = src_f.read_text(encoding="utf-8")
                transformed = transform_md(content, "", str(src_f))
                dest_f.write_text(transformed, encoding="utf-8")
                stats["files_migrated"] += 1
            except Exception as e:
                stats["errors"].append(f"Error processing {fname}: {e}")


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

def main():
    print("=" * 60)
    print("cp-algorithms MkDocs -> Hugo migration")
    print("=" * 60)

    HUGO_CONTENT.mkdir(parents=True, exist_ok=True)

    # Migrate top-level files
    migrate_toplevel()

    # Migrate each section
    for section, title in SECTIONS.items():
        print(f"  Migrating {section}/ ({title}) ...")
        migrate_section(section, title)

    # Print report
    print("\n" + "=" * 60)
    print("MIGRATION REPORT")
    print("=" * 60)
    print(f"Files migrated : {stats['files_migrated']}")
    print(f"Images copied  : {stats['images_copied']}")
    print(f"Errors         : {len(stats['errors'])}")

    if stats["errors"]:
        print("\nERRORS:")
        for e in stats["errors"]:
            print(f"  - {e}")

    print(f"\nFiles with complex admonitions (may need manual review): {len(stats['complex_admonitions'])}")
    if stats["complex_admonitions"]:
        for f in stats["complex_admonitions"]:
            print(f"  - {f}")

    print("\nDone.")


if __name__ == "__main__":
    main()
