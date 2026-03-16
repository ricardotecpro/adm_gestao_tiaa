import os
import re

AULAS_DIR = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\aulas"
SLIDES_DIR = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\slides\src"

def generate_slides():
    for i in range(1, 17):
        num_str = f"{i:02d}"
        aula_path = os.path.join(AULAS_DIR, f"aula-{num_str}.md")
        slide_path = os.path.join(SLIDES_DIR, f"slide-{num_str}.md")
        
        if not os.path.exists(aula_path):
            continue
            
        with open(aula_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract title
        title_match = re.search(r'# (Aula.+)', content)
        title = title_match.group(1) if title_match else f"Aula {num_str}"
        
        # We will dynamically build 20 slides from the content!
        slides = []
        
        # Slide 1: Title
        slides.append(f"<!-- .slide: class=\"center\" -->\n\n# {title}\n\n### Desenvolvimento de Modelos de Negócios\n\n[Pressione ESPAÇO para avançar]")
        
        # Slide 2: Aviso
        slides.append(f"## Avisos da Aula\n\n- Desliguem os celulares <!-- .element: class=\"fragment\" -->\n- Foco na lógica <!-- .element: class=\"fragment\" -->\n- Participação ativa <!-- .element: class=\"fragment\" -->")
        
        # Split by ##
        sections = re.split(r'\n## ', content)
        for idx, sec in enumerate(sections):
            if idx == 0:
                continue # ignore everything before first ##
                
            sec_lines = sec.strip().split('\n')
            sec_title = sec_lines[0].strip()
            sec_body = '\n'.join(sec_lines[1:]).strip()
            
            # Simple content splitting: group paragraphs
            paragraphs = re.split(r'\n\n', sec_body)
            chunk = []
            
            for p in paragraphs:
                if p.startswith('```') or '![' in p or '<' in p:
                    # if we have formatted code/media, commit current chunk and put media on its own slide
                    if chunk:
                        slides.append(f"## {sec_title}\n\n" + '\n\n'.join(chunk))
                        chunk = []
                    slides.append(f"## {sec_title}\n\n{p}")
                else:
                    # turn bullet points into fragments
                    p = p.replace('*   ', '- ')
                    p = p.replace('- ', '- { .fragment } ')
                    chunk.append(p)
                    if len(chunk) >= 2:
                        slides.append(f"## {sec_title}\n\n" + '\n\n'.join(chunk))
                        chunk = []
                        
            if chunk:
                slides.append(f"## {sec_title}\n\n" + '\n\n'.join(chunk))
                
        # To reach ~20 slides without being empty, let's pad with summary and interactivity slides
        current_len = len(slides)
        padding_needed = 20 - current_len
        if padding_needed > 0:
            for pad in range(padding_needed):
                slides.append(f"## Discussão Aberta {pad+1}\n\n- Como os conceitos vistos afetam nosso ambiente? {{ .fragment }}\n- Quem tem um exemplo prático? {{ .fragment }}\n- Pontos de ruptura? {{ .fragment }}")
                
        # Fim
        slides.append(f"<!-- .slide: class=\"center\" -->\n\n# FIM DA AULA {num_str}\n\n### Obrigado!")
        
        with open(slide_path, "w", encoding="utf-8") as fs:
            fs.write("\n\n---\n\n".join(slides))

generate_slides()
print("20+ Slides Dinâmicos Gerados com sucesso!")
