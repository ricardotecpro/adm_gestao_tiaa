
import pathlib
import re

def fix_slides():
    slides_path = pathlib.Path('docs/slides/src')
    for slide_file in slides_path.glob('slide-*.md'):
        content = slide_file.read_text(encoding='utf-8')
        # Replace { .fragment } with <!-- .element: class="fragment" -->
        new_content = content.replace('{ .fragment }', '<!-- .element: class="fragment" -->')
        # Also handle potential variations or common reveal.js patterns if needed
        if content != new_content:
            slide_file.write_text(new_content, encoding='utf-8')
            print(f"Fixed {slide_file.name}")

if __name__ == '__main__':
    fix_slides()
