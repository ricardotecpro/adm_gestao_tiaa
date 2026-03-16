import os
import shutil
import yaml
import re
import sys

# Configurações do Ecossistema
REF_REPO_PATH = r"D:\SourceCode\REPOS\github.io\ads_extra_hardware_e_compiladores"

# Definição de o que é "Infraestrutura" (Arquivos a serem copiados/sobrescritos)
INFRA_FOLDERS = ["scripts", "tests", "hooks", "overrides", ".github/workflows"]
INFRA_FILES = [".mailmap", ".gitignore"]

def load_yaml(path):
    if not os.path.exists(path):
        return None
    class IgnoreUndefinedLoader(yaml.SafeLoader):
        def construct_undefined(self, node):
            return None
    IgnoreUndefinedLoader.add_constructor(None, IgnoreUndefinedLoader.construct_undefined)
    try:
        with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
            return yaml.load(f, Loader=IgnoreUndefinedLoader)
    except Exception as e:
        print(f"  [WARN] Could not load YAML {path}: {e}")
        return None

def save_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

def ensure_structural_files(repo_path):
    docs_dir = os.path.join(repo_path, "docs")
    if not os.path.exists(docs_dir):
        return

    # 1. Rename plano-ensino.md to plano.md if needed
    old_plano = os.path.join(docs_dir, "plano-ensino.md")
    new_plano = os.path.join(docs_dir, "plano.md")
    if os.path.exists(old_plano) and not os.path.exists(new_plano):
        os.rename(old_plano, new_plano)
        print(f"    [OK] Renomeado: plano-ensino.md -> plano.md")

    # 2. Ensure basic files exist
    for fname in ["plano.md", "sobre.md", "materiais.md"]:
        fpath = os.path.join(docs_dir, fname)
        if not os.path.exists(fpath):
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(f"# {fname.replace('.md', '').capitalize()}\n\nConteúdo em breve.\n")
            print(f"    [NEW] Criado: {fname}")

    # 3. Ensure Hubs (index.md)
    hubs = ["aulas", "exercicios", "projetos", "quizzes", "slides", "setups"]
    for hub in hubs:
        hub_dir = os.path.join(docs_dir, hub)
        if not os.path.exists(hub_dir):
            os.makedirs(hub_dir)
        
        index_path = os.path.join(hub_dir, "index.md")
        if not os.path.exists(index_path):
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(f"# Índice de {hub.capitalize()}\n\n")
                if hub == "aulas":
                    f.write('<div class="grid cards" markdown>\n\n- :material-book-open: __Aulas__\n    - [Ver aulas](aula-01.md)\n\n</div>\n')
                else:
                    f.write(f"Confira os materiais de {hub} aqui.\n")
            print(f"    [NEW] Criado: {hub}/index.md")

def inject_standard(repo_path):
    repo_name = os.path.basename(repo_path)
    print(f"💉 Injetando Padrão Ouro: {repo_name}")
    
    if not os.path.exists(repo_path):
        print(f"❌ Erro: Caminho não localizado: {repo_path}")
        return

    # 0. Corrigir Estrutura Física
    ensure_structural_files(repo_path)

    # 1. Sincronizar Pastas de Infraestrutura
    for folder in INFRA_FOLDERS:
        src = os.path.join(REF_REPO_PATH, folder)
        dst = os.path.join(repo_path, folder)
        if os.path.exists(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"  [OK] Pasta sincronizada: {folder}")

    # 2. Sincronizar Arquivos de Raiz
    for file in INFRA_FILES:
        src = os.path.join(REF_REPO_PATH, file)
        dst = os.path.join(repo_path, file)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  [OK] Arquivo sincronizado: {file}")

    # 3. pyproject.toml
    ref_pyprof = os.path.join(REF_REPO_PATH, "pyproject.toml")
    target_pyprof = os.path.join(repo_path, "pyproject.toml")
    if os.path.exists(ref_pyprof) and os.path.exists(target_pyprof):
        with open(ref_pyprof, "r", encoding="utf-8") as f:
            ref_content = f.read()
        with open(target_pyprof, "r", encoding="utf-8") as f:
            target_content = f.read()
            
        name_match = re.search(r'name\s*=\s*"(.*?)"', target_content)
        name = name_match.group(1) if name_match else repo_name
        
        new_content = re.sub(r'name\s*=\s*"(.*?)"', f'name = "{name}"', ref_content, count=1)
        with open(target_pyprof, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("  [OK] pyproject.toml unificado")

    # 4. mkdocs.yml
    ref_mk = os.path.join(REF_REPO_PATH, "mkdocs.yml")
    target_mk = os.path.join(repo_path, "mkdocs.yml")
    if os.path.exists(ref_mk) and os.path.exists(target_mk):
        ref_config = load_yaml(ref_mk)
        target_config = load_yaml(target_mk)
        if ref_config and target_config:
            new_config = ref_config.copy()
            new_config["site_name"] = target_config.get("site_name", repo_name)
            new_config["site_url"] = target_config.get("site_url", f"https://ricardotecpro.github.io/{repo_name}")
            new_config["repo_url"] = target_config.get("repo_url", f"https://github.com/ricardotecpro/{repo_name}")
            new_config["repo_name"] = target_config.get("repo_name", f"ricardotecpro/{repo_name}")
            
            # Navegação (Simples)
            if "nav" in target_config:
                new_config["nav"] = target_config["nav"]
            
            save_yaml(target_mk, new_config)
            print("  [OK] mkdocs.yml unificado")

    print(f"✅ Sucesso: {repo_name}\n")

def main():
    if len(sys.argv) < 2:
        print("Uso: python gold_standard_injector.py <path | all | onda1>")
        return
    
    target = sys.argv[1]
    repos_base = r"D:\SourceCode\REPOS\github.io"
    
    if target == "all":
        ref_basename = os.path.basename(REF_REPO_PATH)
        exclude = ["ricardotecpro", "ricardotecpro.github.io", ref_basename]
        repos = sorted([d for d in os.listdir(repos_base) if os.path.isdir(os.path.join(repos_base, d)) and d not in exclude])
        for r in repos:
            inject_standard(os.path.join(repos_base, r))
    elif target == "onda1":
        for r in ["ads_mod_09_estruturas_de_dados", "ads_spec_backend_com_java", "ads_extra_redes_e_internet", "ads_mod_07_backends_e_apis"]:
            inject_standard(os.path.join(repos_base, r))
    else:
        inject_standard(target)

if __name__ == "__main__":
    main()
