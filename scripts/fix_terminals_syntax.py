import pathlib
import re

def fix_all_termynals():
    aulas_dir = pathlib.Path('docs/aulas')
    count = 0
    
    # Range of aulas to check
    for filepath in aulas_dir.glob('aula-*.md'):
        content = filepath.read_text(encoding='utf-8')
        
        # Pattern 1: Convert ```termynal ... ```  to <!-- termynal -->\n```console ... ```
        # This is for blocks that were already updated to use the 'termynal' language tag
        pattern_lang = re.compile(r'```termynal\s*(.*?)\s*```', flags=re.DOTALL)
        new_content, num_subs_lang = pattern_lang.subn(r'<!-- termynal -->\n```console\n\1\n```', content)
        
        # Pattern 2: Process any existing termy divs if they were missed/re-added
        pattern_div = re.compile(r'<div class="termy"[^>]*>\s*(```.*?```)\s*</div>', flags=re.DOTALL)
        new_content, num_subs_div = pattern_div.subn(r'<!-- termynal -->\n\1', new_content)
        
        num_subs = num_subs_lang + num_subs_div
        
        if num_subs > 0:
            filepath.write_text(new_content, encoding='utf-8')
            count += num_subs
            print(f"Modificado {filepath.name}: {num_subs} blocos corrigidos.")
            
    print(f"Total de terminais corrigidos: {count}")

if __name__ == "__main__":
    fix_all_termynals()
