import re
import os
from pathlib import Path

content_dir = Path("D:/Projects/cp-algorithms-hugo/hugo/content")
pattern = re.compile(r'^(```)\{\.(\w+)[^}]*\}', re.MULTILINE)

fixed = 0
for md_file in content_dir.rglob("*.md"):
    text = md_file.read_text(encoding="utf-8")
    new_text = pattern.sub(r'\1\2', text)
    if new_text != text:
        md_file.write_text(new_text, encoding="utf-8")
        print(f"Fixed: {md_file.name}")
        fixed += 1

print(f"\nTotal files fixed: {fixed}")
