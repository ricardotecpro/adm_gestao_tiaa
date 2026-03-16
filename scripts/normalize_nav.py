"""
normalize_nav.py — Normaliza o nav de todos os repos para o Padrão Ouro de 4 abas.

Estrutura alvo:
  nav:
    - Principal:
        - Curso: index.md
        - Sobre: sobre.md
        - Plano: plano.md
    - Aulas:
        - aulas/index.md
        - Módulo X – ...: ...
    - Materiais:
        - materiais.md
        - Slides: ...
        - Exercícios: ...
        - Quizzes: ...
        - Projetos: ...
        - Configuração: ...
    - Impresso: print_page.md
"""

import os
import re
import sys
import yaml

REPOS_ROOT = r"D:\SourceCode\REPOS\github.io"
EXCLUDE_REPOS = {"ricardotecpro", "ricardotecpro.github.io"}

# Abas principais cujo conteúdo vai para "Materiais"
MATERIAIS_TABS = {"Slides", "Exercícios", "Exercicios", "Quizzes", "Projetos", "Configuração", "Configuracao",
                  "Exercício", "Projeto", "Slide", "Setup", "Setups", "Labs", "Labs e Projetos"}

# Abas que ficam em "Principal"
PRINCIPAL_SUBITEMS_MAP = {
    "Início": "index.md",
    "Home": "index.md",
    "Curso": "index.md",
    "Principal": None,   # Já é a aba, expandir seus subitems
    "Sobre": "sobre.md",
    "Plano de Ensino": "plano.md",
    "Plano": "plano.md",
}


def make_loader():
    class SafeIgnoreLoader(yaml.SafeLoader):
        pass
    SafeIgnoreLoader.add_constructor(None, lambda loader, node: None)
    return SafeIgnoreLoader


def load_yaml(path):
    try:
        with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
            return yaml.load(f, Loader=make_loader())
    except Exception as e:
        print(f"  [WARN] Cannot load {path}: {e}")
        return None


def save_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def flat_items(items, prefix=""):
    """Recursively flatten nav items to list of (label, path or list) tuples."""
    result = []
    for item in items:
        if isinstance(item, dict):
            for k, v in item.items():
                result.append((k, v))
        elif isinstance(item, str):
            result.append((None, item))
    return result


def normalize_nav(original_nav, docs_dir):
    """Convert any nav structure to the 4-tab Gold Standard."""

    principal_items = []
    aulas_item = None
    materiais_children = []
    impresso_path = "print_page.md"

    for entry in original_nav:
        if not isinstance(entry, dict):
            continue

        key = list(entry.keys())[0]
        val = entry[key]

        # ── Impresso / Print ─────────────────────────────────────────────────
        if key in ("Impressão", "Impresso", "Print", "Versão Impressa"):
            impresso_path = val if isinstance(val, str) else "print_page.md"

        # ── Principal ────────────────────────────────────────────────────────
        elif key in ("Principal",):
            # Already structured — extract subitems
            if isinstance(val, list):
                for sub in val:
                    if isinstance(sub, dict):
                        principal_items.append(sub)
                    else:
                        principal_items.append({"Curso": "index.md"})
            else:
                principal_items.append({"Curso": str(val)})

        elif key in ("Início", "Home"):
            if isinstance(val, str):
                principal_items.insert(0, {"Curso": val})

        elif key in ("Plano de Ensino", "Plano"):
            # Rename physical file if needed
            old = os.path.join(docs_dir, "plano-ensino.md")
            new = os.path.join(docs_dir, "plano.md")
            if os.path.exists(old) and not os.path.exists(new):
                os.rename(old, new)
                print("    [RENAME] plano-ensino.md → plano.md")
            principal_items.append({"Plano": "plano.md"})

        elif key in ("Sobre",):
            principal_items.append({"Sobre": "sobre.md"})

        # ── Aulas ────────────────────────────────────────────────────────────
        elif key in ("Aulas", "Módulos", "Modulos", "Módulos de Aula", "Conteúdo", "Conteúdo Programático"):
            aulas_item = entry

        # ── Materiais (already structured) ───────────────────────────────────
        elif key == "Materials": # Catch typo
            materiais_children.extend(val if isinstance(val, list) else [val])
        elif key == "Materiais":
            if isinstance(val, list):
                materiais_children = val
            else:
                materiais_children = [{"Materiais": val}]

        # ── Material children tabs → consolidate under Materiais ─────────────
        elif key in MATERIAIS_TABS:
            if isinstance(val, str):
                materiais_children.append({key: val})
            elif isinstance(val, list):
                materiais_children.append({key: val})

    # ── Scan for Aulas if missing ──────────────────────────────────────────────
    if not aulas_item:
        aulas_dir = os.path.join(docs_dir, "aulas")
        if os.path.exists(aulas_dir):
            # Build Aulas tab from directory
            aulas_list = []
            if os.path.exists(os.path.join(aulas_dir, "index.md")):
                aulas_list.append("aulas/index.md")
            
            # Simple flat list of found aulas
            files = sorted([f for f in os.listdir(aulas_dir) if f.startswith("aula-") and f.endswith(".md")])
            for f in files:
                # Try to extract title from file? Too heavy for now.
                label = f.replace(".md", "").capitalize().replace("-", " ")
                aulas_list.append({label: f"aulas/{f}"})
            
            if aulas_list:
                aulas_item = {"Aulas": aulas_list}

    # ── Ensure index.md is first principal item ───────────────────────────────
    has_index = any("index.md" in str(v) for item in principal_items for v in item.values())
    if not has_index and os.path.exists(os.path.join(docs_dir, "index.md")):
        principal_items.insert(0, {"Curso": "index.md"})

    # ── Ensure sobre.md / plano.md are in principal if they exist ────────────
    for fname, label in [("sobre.md", "Sobre"), ("plano.md", "Plano")]:
        exists = os.path.exists(os.path.join(docs_dir, fname))
        already = any(label in item for item in principal_items)
        if exists and not already:
            principal_items.append({label: fname})

    # ── Build Materiais if empty but files exist ──────────────────────────────
    if not materiais_children:
        if os.path.exists(os.path.join(docs_dir, "materiais.md")):
            materiais_children.append({"materiais.md": "materiais.md"})
        for section, index_file in [
            ("Slides", "slides/index.md"), ("Exercícios", "exercicios/index.md"),
            ("Quizzes", "quizzes/index.md"), ("Projetos", "projetos/index.md"),
            ("Configuração", "setups/index.md"),
        ]:
            if os.path.exists(os.path.join(docs_dir, index_file)):
                materiais_children.append({section: index_file})

    # ── Fallback: ensure materiais.md is first ────────────────────────────────
    has_materiais_md = any("materiais.md" in str(list(v.values())[0]) for v in materiais_children if isinstance(v, dict))
    if not has_materiais_md and os.path.exists(os.path.join(docs_dir, "materiais.md")):
        materiais_children.insert(0, "materiais.md")

    # ── Assemble final nav ────────────────────────────────────────────────────
    nav = []
    nav.append({"Principal": principal_items})
    if aulas_item:
        nav.append(aulas_item)
    if materiais_children:
        nav.append({"Materiais": materiais_children})
    nav.append({"Impresso": impresso_path})

    return nav


def process_repo(repo_path):
    repo_name = os.path.basename(repo_path)
    mkdocs_path = os.path.join(repo_path, "mkdocs.yml")
    docs_dir = os.path.join(repo_path, "docs")

    if not os.path.exists(mkdocs_path):
        print(f"  [SKIP] No mkdocs.yml: {repo_name}")
        return False

    config = load_yaml(mkdocs_path)
    if not config:
        print(f"  [ERR] Could not load: {repo_name}")
        return False

    original_nav = config.get("nav", [])

    # Skip if already has 4-tab Gold Standard
    top_keys = [list(item.keys())[0] if isinstance(item, dict) else str(item) for item in original_nav]
    if top_keys == ["Principal", "Aulas", "Materiais", "Impresso"]:
        print(f"  [SKIP] Already Gold Standard: {repo_name}")
        return True

    new_nav = normalize_nav(original_nav, docs_dir)
    config["nav"] = new_nav

    save_yaml(mkdocs_path, config)
    print(f"  [OK] Nav normalized: {repo_name}")
    return True


def main():
    if len(sys.argv) > 1 and sys.argv[1] != "all":
        # Single repo
        process_repo(sys.argv[1])
        return

    repos = sorted([
        d for d in os.listdir(REPOS_ROOT)
        if os.path.isdir(os.path.join(REPOS_ROOT, d)) and d not in EXCLUDE_REPOS
    ])

    print(f"🚀 Normalizing nav for {len(repos)} repos...")
    ok = 0
    for repo in repos:
        result = process_repo(os.path.join(REPOS_ROOT, repo))
        if result:
            ok += 1

    print(f"\n✅ Done: {ok}/{len(repos)} repos processed.")


if __name__ == "__main__":
    main()
