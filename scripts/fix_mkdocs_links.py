import os
import glob

def replace_in_files(file_pattern, replacements):
    for fpath in glob.glob(file_pattern):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        modified = False
        for old, new in replacements.items():
            if old in content:
                content = content.replace(old, new)
                modified = True
        
        if modified:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed links in {fpath}")

# Fix slides in docs/slides/
replace_in_files(
    r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\slides\slide-*.md",
    {
        "](./aula-": "](../aulas/aula-",
        "](./projeto-": "](../projetos/projeto-",
        "](../exercicios/": "](../exercicios/", # This is actually correct for docs/slides/
        "](../projetos/": "](../projetos/"
    }
)

# Fix slides in docs/slides/src/
replace_in_files(
    r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\slides\src\slide-*.md",
    {
        "](./aula-": "](../../aulas/aula-",
        "](../exercicios/": "](../../exercicios/",
        "](../projetos/": "](../../projetos/"
    }
)

# And fix index.md references
replace_in_files(
    r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\slides\index.md",
    {
        "](./slide-": "](slide-"
    }
)

print("Slide link fixes applied!")
