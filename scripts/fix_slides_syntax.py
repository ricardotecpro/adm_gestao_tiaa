import os
import re

slides_dir = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\slides"

for filename in os.listdir(slides_dir):
    if filename.endswith(".md") and filename.startswith("slide-"):
        file_path = os.path.join(slides_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace { .fragment } with <!-- .element: class="fragment" -->
        # Handling potential variations in spacing
        new_content = re.sub(r'\{\s*\.fragment\s*\}', '<!-- .element: class="fragment" -->', content)
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filename}")
        else:
            print(f"No changes needed: {filename}")
