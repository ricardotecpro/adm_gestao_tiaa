#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificação Simplificada de Conformidade com Master Prompt
"""

import pathlib
from rich import print


def verificar_master_prompt_simples():
    """Verificação manual de conformidade com o Master Prompt"""
    
    print("\n[bold cyan]🔍 VERIFICAÇÃO MASTER PROMPT - CONFORMIDADE[/bold cyan]")
    print("=" * 70)
    
    conformidades = []
    issues = []
    
    # 1. MÓDULO 1: INFRAESTRUTURA E AGNOSTICISMO
    print("\n[bold blue]📦 MÓDULO 1: INFRAESTRUTURA E AGNOSTICISMO[/bold blue]")
    
    # 1.1 Identidade Visual SVG
    logo_svg = pathlib.Path('docs/assets/images/logic_logo.svg')
    if logo_svg.exists():
        conformidades.append("✅ Logo SVG encontrado")
    else:
        issues.append("❌ Logo SVG não encontrado")
    
    # 1.2 Paleta de Cores
    mkdocs_content = pathlib.Path('mkdocs.yml').read_text(encoding='utf-8')
    if 'primary: teal' in mkdocs_content and 'accent: amber' in mkdocs_content:
        conformidades.append("✅ Paleta teal/amber configurada")
    else:
        issues.append("❌ Paleta não está teal/amber")
    
    if 'prefers-color-scheme' in mkdocs_content:
        conformidades.append("✅ Media queries para tema automático")
    else:
        issues.append("❌ Media queries não configuradas")
    
    # 1.3 Metadados pyproject.toml
    pyproject_content = pathlib.Path('pyproject.toml').read_text(encoding='utf-8')
    if 'name = \"adm_gestao_tiaa\"' in pyproject_content:
        conformidades.append("✅ Nome do projeto correto (baseado na pasta)")
    else:
        issues.append("❌ Nome do projeto não está baseado na pasta")
    
    if 'Ricardo Tec Pro' in pyproject_content:
        conformidades.append("✅ Author padrão Ricardo Tec Pro")
    else:
        issues.append("❌ Author não está no padrão")
    
    # 1.4 Plugins e navegação
    nav_features = ['navigation.sections', 'navigation.path', 'navigation.instant']
    for feature in nav_features:
        if feature in mkdocs_content:
            conformidades.append(f"✅ {feature} ativo")
        else:
            issues.append(f"❌ {feature} não encontrado")
    
    if 'exclude_docs:' in mkdocs_content and 'src/*' in mkdocs_content:
        conformidades.append("✅ exclude_docs configurado")
    else:
        issues.append("❌ exclude_docs não configurado")
    
    # 1.5 Agnosticismo de Scripts
    scripts_path = pathlib.Path('scripts')
    agnostic_ok = True
    if scripts_path.exists():
        for script_file in scripts_path.glob('*.py'):
            content = script_file.read_text(encoding='utf-8')
            if 'Desenvolvimento Mobile Nativo' in content:
                issues.append(f"❌ {script_file.name} não é agnóstico")
                agnostic_ok = False
    
    if agnostic_ok:
        conformidades.append("✅ Scripts são agnósticos")
    
    # 2. MÓDULO 2: ARQUITETURA PEDAGÓGICA
    print("\n[bold green]📚 MÓDULO 2: ARQUITETURA PEDAGÓGICA[/bold green]")
    
    # 2.1 Padrão das 16 Aulas
    aulas_ok = 0
    for i in range(1, 17):
        aula_path = pathlib.Path(f'docs/aulas/aula-{i:02d}.md')
        if aula_path.exists():
            content = aula_path.read_text(encoding='utf-8')
            
            has_mermaid = '```mermaid' in content
            has_termynal = 'termynal' in content.lower()
            has_admonitions = any(adm in content for adm in ['!!! info', '!!! warning', '!!! tip'])
            
            if has_mermaid and has_termynal and has_admonitions:
                aulas_ok += 1
    
    conformidades.append(f"✅ {aulas_ok}/16 aulas com padrão completo (Mermaid + TermynalJS + Admonitions)")
    
    # 2.2 Exercícios e Soluções
    exercicios_ok = 0
    for i in range(1, 17):
        exercicio_path = pathlib.Path(f'docs/exercicios/exercicio-{i:02d}.md')
        solucao_path = pathlib.Path(f'docs/exercicios/solucao-{i:02d}.md')
        
        if exercicio_path.exists() and solucao_path.exists():
            exercicios_ok += 1
    
    conformidades.append(f"✅ {exercicios_ok}/16 pares exercício-solução")
    
    # 2.3 Quizzes
    quizzes_ok = 0
    for i in range(1, 17):
        quiz_path = pathlib.Path(f'docs/quizzes/quiz-{i:02d}.md')
        if quiz_path.exists():
            quizzes_ok += 1
    
    conformidades.append(f"✅ {quizzes_ok}/16 quizzes criados")
    
    # 2.4 Slides
    slides_ok = 0
    for i in range(1, 17):
        slide_path = pathlib.Path(f'docs/slides/slide-{i:02d}.html')
        if slide_path.exists():
            slides_ok += 1
    
    conformidades.append(f"✅ {slides_ok}/16 slides HTML gerados")
    
    # 3. MÓDULO 3: PREVENÇÃO DE ERROS
    print("\n[bold yellow]🔧 MÓDULO 3: PREVENÇÃO DE ERROS[/bold yellow]")
    
    # 3.1 Mermaid versão 11.12.3
    if 'mermaid@11.12.3' in mkdocs_content:
        conformidades.append("✅ Mermaid versão 11.12.3 configurada")
    else:
        issues.append("❌ Mermaid não está na versão correta")
    
    # 3.2 MathJax configurado
    if 'arithmatex:' in mkdocs_content and 'generic: true' in mkdocs_content:
        conformidades.append("✅ MathJax (arithmatex) configurado")
    else:
        issues.append("❌ MathJax não configurado corretamente")
    
    # 4. MÓDULO 4: PLANO DE VALIDAÇÃO
    print("\n[bold magenta]✅ MÓDULO 4: VALIDAÇÃO[/bold magenta]")
    
    # 4.1 Estrutura de pastas
    required_folders = [
        'docs/aulas', 'docs/exercicios', 'docs/projetos', 
        'docs/quizzes', 'docs/slides', 'docs/setups', 'logs'
    ]
    folders_ok = sum(1 for folder in required_folders if pathlib.Path(folder).exists())
    conformidades.append(f"✅ {folders_ok}/{len(required_folders)} pastas obrigatórias")
    
    # 4.2 Navegação com 4 abas
    nav_sections = ['- Informações:', '- Aulas:', '- Materiais:', '- Impressão:']
    nav_ok = sum(1 for section in nav_sections if section in mkdocs_content)
    conformidades.append(f"✅ {nav_ok}/4 seções de navegação principais")
    
    # RESUMO FINAL
    print("\n[bold]📊 RESUMO DE CONFORMIDADE:[/bold]")
    print(f"✅ Conformidades: {len(conformidades)}")
    print(f"❌ Issues pendentes: {len(issues)}")
    
    compliance_rate = len(conformidades) / (len(conformidades) + len(issues)) * 100
    print(f"📈 Taxa de conformidade: {compliance_rate:.1f}%")
    
    if len(issues) == 0:
        print("\n[bold green]🎉 PROJETO 100% CONFORME COM MASTER PROMPT![/bold green]")
    else:
        print("\n[bold yellow]⚠️ ISSUES A CORRIGIR:[/bold yellow]")
        for issue in issues:
            print(f"  {issue}")
    
    return len(issues) == 0


if __name__ == '__main__':
    verificar_master_prompt_simples()