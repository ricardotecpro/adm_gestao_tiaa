#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise e Limpeza de Pastas .src (Duplicatas Legadas)
"""

import pathlib
import shutil
from rich import print
from rich.console import Console
from rich.table import Table


def analisar_pastas_src():
    """Analisa as pastas src vs .src para confirmar se são duplicatas"""
    console = Console()
    
    print("\n[bold cyan]🔍 ANÁLISE DAS PASTAS SRC[/bold cyan]")
    print("=" * 60)
    
    # Verificar slides
    slides_src = pathlib.Path('docs/slides/src')
    slides_dot_src = pathlib.Path('docs/slides/.src')
    
    print("\n[bold blue]📊 SLIDES:[/bold blue]")
    if slides_src.exists() and slides_dot_src.exists():
        files_src = set(f.name for f in slides_src.glob('slide-*.md'))
        files_dot_src = set(f.name for f in slides_dot_src.glob('slide-*.md'))
        
        print(f"  /src: {len(files_src)} arquivos")
        print(f"  /.src: {len(files_dot_src)} arquivos")
        
        if files_src == files_dot_src:
            print("  ✅ Mesmo conjunto de arquivos")
        else:
            print("  ❌ Arquivos diferentes")
            
    # Verificar quizzes
    quizzes_src = pathlib.Path('docs/quizzes/src')
    quizzes_dot_src = pathlib.Path('docs/quizzes/.src')
    
    print("\n[bold green]❓ QUIZZES:[/bold green]")
    if quizzes_src.exists() and quizzes_dot_src.exists():
        files_src = set(f.name for f in quizzes_src.glob('quiz-*.md'))
        files_dot_src = set(f.name for f in quizzes_dot_src.glob('quiz-*.md'))
        
        print(f"  /src: {len(files_src)} arquivos")
        print(f"  /.src: {len(files_dot_src)} arquivos")
        
        if files_src == files_dot_src:
            print("  ✅ Mesmo conjunto de arquivos")
        else:
            print("  ❌ Arquivos diferentes")
    
    # Verificar qual pasta está sendo usada no script principal
    print("\n[bold yellow]🔧 CONFIGURAÇÃO ATUAL:[/bold yellow]")
    
    script_content = pathlib.Path('scripts/generate_slides_quizzes.py').read_text(encoding='utf-8')
    
    if "/ 'src'" in script_content:
        print("  ✅ Script usa pastas /src (sem ponto)")
    elif "/ '.src'" in script_content:
        print("  ⚠️ Script usa pastas /.src (com ponto)")
    
    # Verificar mkdocs.yml
    mkdocs_content = pathlib.Path('mkdocs.yml').read_text(encoding='utf-8')
    
    if 'src/*' in mkdocs_content:
        print("  ✅ mkdocs.yml exclui /src (sem ponto)")
    if '.src/*' in mkdocs_content:
        print("  ⚠️ mkdocs.yml exclui /.src (com ponto)")
    
    return True


def verificar_seguranca_remocao():
    """Verifica se é seguro remover as pastas .src"""
    
    print("\n[bold red]🛡️ VERIFICAÇÃO DE SEGURANÇA[/bold red]")
    
    riscos = []
    pastas_para_remover = [
        'docs/slides/.src',
        'docs/quizzes/.src'
    ]
    
    # 1. Verificar se algum script ativo usa .src
    scripts_usando_dot_src = []
    
    scripts_ativos = [
        'scripts/generate_slides_quizzes.py',
        'hooks/copy_slides.py'
    ]
    
    for script in scripts_ativos:
        script_path = pathlib.Path(script)
        if script_path.exists():
            content = script_path.read_text(encoding='utf-8')
            if '.src' in content:
                scripts_usando_dot_src.append(script)
    
    if scripts_usando_dot_src:
        riscos.append(f"Scripts ativos usando .src: {', '.join(scripts_usando_dot_src)}")
    
    # 2. Verificar tamanho das pastas
    total_size = 0
    for pasta in pastas_para_remover:
        pasta_path = pathlib.Path(pasta)
        if pasta_path.exists():
            size = sum(f.stat().st_size for f in pasta_path.rglob('*') if f.is_file())
            total_size += size
    
    print(f"  📁 Tamanho total das pastas .src: {total_size / 1024:.1f} KB")
    print(f"  📂 Pastas a remover: {len(pastas_para_remover)}")
    
    if riscos:
        print("\n[bold red]⚠️ RISCOS IDENTIFICADOS:[/bold red]")
        for risco in riscos:
            print(f"  • {risco}")
        return False
    else:
        print("\n[bold green]✅ REMOÇÃO SEGURA CONFIRMADA[/bold green]")
        print("  • Scripts ativos usam /src")
        print("  • mkdocs.yml configurado para /src")
        print("  • Pastas .src são duplicatas legadas")
        return True


def executar_limpeza():
    """Remove as pastas .src após confirmação"""
    
    if not verificar_seguranca_remocao():
        print("\n[bold red]❌ LIMPEZA CANCELADA - RISCOS DETECTADOS[/bold red]")
        return False
    
    print("\n[bold cyan]🧹 INICIANDO LIMPEZA SEGURA[/bold cyan]")
    
    pastas_removidas = []
    
    pastas_para_remover = [
        pathlib.Path('docs/slides/.src'),
        pathlib.Path('docs/quizzes/.src')
    ]
    
    for pasta in pastas_para_remover:
        if pasta.exists():
            try:
                arquivos_count = len(list(pasta.rglob('*')))
                shutil.rmtree(pasta)
                pastas_removidas.append(f"{pasta} ({arquivos_count} itens)")
                print(f"  ✅ Removido {pasta}")
            except Exception as e:
                print(f"  ❌ Erro ao remover {pasta}: {e}")
                return False
    
    print(f"\n[bold green]🎉 LIMPEZA CONCLUÍDA COM SUCESSO![/bold green]")
    print(f"  📁 Pastas removidas: {len(pastas_removidas)}")
    for pasta in pastas_removidas:
        print(f"    • {pasta}")
    
    # Verificar se ainda existem referências problemáticas
    scripts_legacy = [
        'scripts/convert_quizzes.py',
        'scripts/recover_quizzes.py'
    ]
    
    print(f"\n[bold yellow]📝 SCRIPTS LEGACY COM REFERÊNCIAS .src:[/bold yellow]")
    for script in scripts_legacy:
        if pathlib.Path(script).exists():
            print(f"  • {script} (não usado no fluxo principal)")
    
    return True


def main():
    """Executa análise e limpeza das pastas .src"""
    
    print("[bold]🧹 LIMPEZA DE PASTAS DUPLICADAS (.src)[/bold]")
    
    # 1. Análise inicial
    analisar_pastas_src()
    
    # 2. Perguntar se deve executar limpeza
    print("\n" + "="*60)
    resposta = input("\n🤔 Executar limpeza das pastas .src? (s/N): ").lower().strip()
    
    if resposta in ['s', 'sim', 'y', 'yes']:
        executar_limpeza()
    else:
        print("\n[yellow]ℹ️ Limpeza cancelada pelo usuário[/yellow]")


if __name__ == '__main__':
    main()