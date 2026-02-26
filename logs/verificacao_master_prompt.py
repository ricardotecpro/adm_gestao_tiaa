#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificação de Conformidade com Master Prompt Refatoração Universal
"""

import pathlib
import yaml
from rich import print
from rich.console import Console
from rich.table import Table


def verificar_conformidade_agnostica():
    """Verifica se o projeto atende aos requisitos de agnosticismo do Master Prompt"""
    console = Console()
    
    print("\n[bold cyan]🔍 VERIFICAÇÃO DE CONFORMIDADE - MASTER PROMPT[/bold cyan]")
    print("=" * 70)
    
    issues = []
    conformidades = []
    
    # Verificar mkdocs.yml
    mkdocs_path = pathlib.Path('mkdocs.yml')
    if mkdocs_path.exists():
        with open(mkdocs_path, 'r', encoding='utf-8') as f:
            mkdocs_config = yaml.safe_load(f)
        
        # 1. Verificar paleta
        theme_palette = mkdocs_config.get('theme', {}).get('palette', [])
        if isinstance(theme_palette, list) and len(theme_palette) >= 2:
            light_mode = theme_palette[0]
            dark_mode = theme_palette[1] 
            
            if (light_mode.get('primary') == 'teal' and 
                light_mode.get('accent') == 'amber' and
                'media' in light_mode and
                dark_mode.get('primary') == 'teal' and 
                dark_mode.get('accent') == 'amber'):
                conformidades.append("✅ Paleta teal/amber com media queries")
            else:
                issues.append("❌ Paleta não configurada corretamente")
        
        # 2. Verificar plugins de navegação
        features = mkdocs_config.get('theme', {}).get('features', [])
        nav_features = ['navigation.sections', 'navigation.path', 'navigation.instant']
        missing_features = [f for f in nav_features if f not in features]
        
        if not missing_features:
            conformidades.append(f"✅ Features de navegação ativas: {', '.join(nav_features)}")
        else:
            issues.append(f"❌ Features ausentes: {', '.join(missing_features)}")
        
        # 3. Verificar Mermaid versão
        extra_js = mkdocs_config.get('extra_javascript', [])
        mermaid_js = [js for js in extra_js if 'mermaid' in js]
        if any('11.12.3' in js for js in mermaid_js):
            conformidades.append("✅ Mermaid versão 11.12.3 configurada")
        else:
            issues.append("❌ Mermaid não está na versão 11.12.3")
        
        # 4. Verificar structure do menu (4 abas principais)
        nav = mkdocs_config.get('nav', [])
        main_sections = [list(item.keys())[0] if isinstance(item, dict) else item for item in nav]
        expected_sections = ['Informações', 'Aulas', 'Materiais', 'Impressão']
        
        if all(section in main_sections for section in expected_sections):
            conformidades.append("✅ Menu com 4 seções principais corretas")
        else:
            issues.append(f"❌ Menu incorreto. Esperado: {expected_sections}, Atual: {main_sections}")
        
        # 5. Verificar exclude_docs
        exclude_docs = mkdocs_config.get('exclude_docs')
        if exclude_docs and 'src/*' in exclude_docs:
            conformidades.append("✅ exclude_docs configurado para pastas src/")
        else:
            issues.append("❌ exclude_docs não configurado corretamente")
    
    # Verificar pyproject.toml
    pyproject_path = pathlib.Path('pyproject.toml')
    if pyproject_path.exists():
        content = pyproject_path.read_text(encoding='utf-8')
        if 'name = "adm_gestao_tiaa"' in content:
            conformidades.append("✅ pyproject.toml com nome correto")
        else:
            issues.append("❌ pyproject.toml nome deve ser extraído da pasta")
        
        if 'Ricardo Tec Pro' in content and 'ricardotecpro@hotmail.com' in content:
            conformidades.append("✅ Author padrão configurado")
        else:
            issues.append("❌ Author não está no padrão Ricardo Tec Pro")
    
    # Verificar scripts agnósticos
    scripts_path = pathlib.Path('scripts')
    if scripts_path.exists():
        non_agnostic_files = []
        
        for script_file in scripts_path.glob('*.py'):
            content = script_file.read_text(encoding='utf-8')
            
            # Verificar strings fixas problemáticas
            problematic_strings = [
                'Desenvolvimento Mobile Nativo',
                'Engenharia de Software',
                'Mobile Nativo',
                'Python'  # específico de outro curso
            ]
            
            for string in problematic_strings:
                if string in content:
                    non_agnostic_files.append(f"{script_file.name} - contém '{string}'")
        
        if not non_agnostic_files:
            conformidades.append("✅ Scripts são agnósticos (sem strings fixas)")
        else:
            for file_issue in non_agnostic_files:
                issues.append(f"❌ Script não agnóstico: {file_issue}")
    
    # Verificar estrutura de pastas
    required_folders = [
        'docs/aulas', 'docs/exercicios', 'docs/projetos', 
        'docs/quizzes', 'docs/slides', 'docs/setups', 'logs'
    ]
    
    missing_folders = [folder for folder in required_folders 
                      if not pathlib.Path(folder).exists()]
    
    if not missing_folders:
        conformidades.append("✅ Estrutura de pastas completa")
    else:
        issues.append(f"❌ Pastas ausentes: {', '.join(missing_folders)}")
    
    # Mostrar resultados
    if conformidades:
        print("\n[bold green]✅ CONFORMIDADES ATENDIDAS:[/bold green]")
        for conf in conformidades:
            print(f"  {conf}")
    
    if issues:
        print("\n[bold red]❌ ISSUES A CORRIGIR:[/bold red]")
        for issue in issues:
            print(f"  {issue}")
    
    # Resumo
    total_checks = len(conformidades) + len(issues)
    compliance_rate = len(conformidades) / total_checks * 100
    
    print(f"\n[bold]📊 RESUMO DE CONFORMIDADE:[/bold]")
    print(f"✅ Atendidas: {len(conformidades)}")
    print(f"❌ Pendentes: {len(issues)}")
    print(f"📈 Taxa de Conformidade: {compliance_rate:.1f}%")
    
    return len(issues) == 0


def verificar_aulas_master_prompt():
    """Verifica se as 16 aulas atendem aos padrões do Master Prompt"""
    
    print("\n[bold yellow]📚 VERIFICAÇÃO DAS AULAS - PADRÃO MASTER PROMPT[/bold yellow]")
    
    issues_aulas = []
    
    for i in range(1, 17):
        aula_path = pathlib.Path(f'docs/aulas/aula-{i:02d}.md')
        
        if not aula_path.exists():
            issues_aulas.append(f"❌ Aula {i:02d} não encontrada")
            continue
        
        content = aula_path.read_text(encoding='utf-8')
        
        # Verificações específicas do Master Prompt
        checks = {
            'mermaid': '```mermaid' in content,
            'termynal': 'termynal' in content.lower(),
            'admonitions': any(adm in content for adm in ['!!! info', '!!! warning', '!!! tip', '!!! note']),
            'portugues': not any(eng in content.lower() for eng in ['hello', 'world', 'english'])
        }
        
        failed_checks = [check for check, passed in checks.items() if not passed]
        
        if failed_checks:
            issues_aulas.append(f"❌ Aula {i:02d}: {', '.join(failed_checks)}")
    
    if not issues_aulas:
        print("✅ Todas as 16 aulas atendem ao padrão Master Prompt")
    else:
        for issue in issues_aulas:
            print(f"  {issue}")
    
    return len(issues_aulas) == 0


if __name__ == '__main__':
    conformidade_ok = verificar_conformidade_agnostica()
    aulas_ok = verificar_aulas_master_prompt()
    
    print(f"\n[bold]{'✅ PROJETO EM TOTAL CONFORMIDADE' if (conformidade_ok and aulas_ok) else '⚠️ PROJETO PRECISA DE AJUSTES'}[/bold]")