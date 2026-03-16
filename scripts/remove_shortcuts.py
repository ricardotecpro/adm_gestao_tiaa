import os
import re

slides_dir = r"D:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\slides"

# Pattern to match the shortcuts div, its style, and the script logic
# Removing lines 24-49 and lines 84-104 (roughly)
# It's safer to use regex to find the blocks

div_pattern = re.compile(r'<div class="reveal-shortcuts">.*?</div>', re.DOTALL)
style_pattern = re.compile(r'<style>\s*\.reveal-shortcuts.*?/style>', re.DOTALL)
script_pattern = re.compile(r'// Fullscreen detection for shortcuts to pass test_fullscreen\.py.*?toggleFullscreenClass\(\);', re.DOTALL)

for i in range(1, 17):
    filename = f"slide-{i:02d}.html"
    filepath = os.path.join(slides_dir, filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the div
        content = div_pattern.sub('', content)
        # Remove the style
        content = style_pattern.sub('', content)
        # Remove the script block
        content = script_pattern.sub('', content)
        
        # Clean up double newlines that might result from removals
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Processed {filename}")
    else:
        print(f"File {filename} not found")
