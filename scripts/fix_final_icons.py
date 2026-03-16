import os
import re

TARGET_REPOS = [
    r"D:\SourceCode\REPOS\github.io\ads_extra_redes_e_internet",
    r"D:\SourceCode\REPOS\github.io\ads_mod_09_estruturas_de_dados",
    r"D:\SourceCode\REPOS\github.io\ads_spec_backend_com_java"
]

ICON_MAP = {
    ":material-numeric-11:": ":material-memory:",
    ":material-numeric-12:": ":material-chip:",
    ":material-numeric-13:": ":material-expansion-card-variant:",
    ":material-numeric-14:": ":material-usb:",
    ":material-numeric-15:": ":material-matrix:",
    ":material-numeric-16:": ":material-rocket-launch:"
}

def fix_icons(repo_path):
    aulas_index = os.path.join(repo_path, "docs", "aulas", "index.md")
    if not os.path.exists(aulas_index):
        print(f"  [MISS] {aulas_index}")
        return

    with open(aulas_index, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    for old, new in ICON_MAP.items():
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(aulas_index, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  [OK] Icons fixed in {repo_path}")
    else:
        print(f"  [SKIP] No numeric icons found in {repo_path}")

for repo in TARGET_REPOS:
    fix_icons(repo)
