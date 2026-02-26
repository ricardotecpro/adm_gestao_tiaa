#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Auditoria das Aulas - ADM Gestão TI
Verifica se as 16 aulas seguem os padrões estabelecidos no Master Prompt
"""

import pathlib
import re
from dataclasses import dataclass
from typing import List, Dict
from rich import print
from rich.console import Console
from rich.table import Table

@dataclass
class AulaAudit:
    numero: int
    arquivo: str
    tem_mermaid: bool = False
    tem_termynal: bool = False
    tem_emoji: bool = False
    tem_admonitions: bool = False
    tem_exemplos: bool = False
    nivel_conteudo: str = "básico"
    observacoes: List[str] = None
    
    def __post_init__(self):
        if self.observacoes is None:
            self.observacoes = []

def verificar_aula(numero: int) -> AulaAudit:
    """Verifica uma aula específica"""
    arquivo = f"docs/aulas/aula-{numero:02d}.md"
    caminho = pathlib.Path(arquivo)
    
    audit = AulaAudit(numero=numero, arquivo=arquivo)
    
    if not caminho.exists():
        audit.observacoes.append("⚠️  Arquivo não encontrado")
        return audit
    
    conteudo = caminho.read_text(encoding='utf-8')
    
    # Verificar Mermaid
    if '```mermaid' in conteudo:
        audit.tem_mermaid = True
    else:
        audit.observacoes.append("❌ Falta diagrama Mermaid")
    
    # Verificar TermynalJS
    if '```termynal' in conteudo or 'termynal' in conteudo.lower():
        audit.tem_termynal = True
    else:
        audit.observacoes.append("❌ Falta exemplo TermynalJS")
    
    # Verificar Emojis
    emoji_pattern = r'[\U0001F300-\U0001F9FF]|[\U00002600-\U000027BF]|[\U0001F600-\U0001F64F]'
    if re.search(emoji_pattern, conteudo):
        audit.tem_emoji = True
    else:
        audit.observacoes.append("❌ Poucos emojis")
    
    # Verificar Admonitions
    admonitions = ['!!! info', '!!! warning', '!!! tip', '!!! note', '!!! danger']
    if any(adm in conteudo for adm in admonitions):
        audit.tem_admonitions = True
    else:
        audit.observacoes.append("❌ Falta blocos de destaque (admonitions)")
    
    # Verificar exemplos práticos
    indicadores_exemplos = ['exemplo:', 'vamos', 'na prática', 'caso real', 'cenário']
    if any(ind in conteudo.lower() for ind in indicadores_exemplos):
        audit.tem_exemplos = True
    else:
        audit.observacoes.append("❌ Poucos exemplos práticos")
    
    # Avaliar nível de conteúdo
    palavras_intermediarias = [
        'integração', 'arquitetura', 'escalabilidade', 'performance',
        'segurança', 'otimização', 'automação', 'workflow', 'api',
        'microso', 'dashboard', 'analytics', 'compliance'
    ]
    
    count_intermediario = sum(1 for palavra in palavras_intermediarias 
                             if palavra in conteudo.lower())
    
    if count_intermediario >= 3:
        audit.nivel_conteudo = "intermediário"
    elif count_intermediario >= 1:
        audit.nivel_conteudo = "básico-intermediário"
    else:
        audit.nivel_conteudo = "básico"
        audit.observacoes.append("⚠️  Conteúdo muito básico - expandir para nível intermediário")
    
    # Verificações específicas de qualidade
    linhas = conteudo.split('\n')
    if len(linhas) < 50:
        audit.observacoes.append("⚠️  Conteúdo muito curto - expandir")
    
    # Verificar se tem listas estruturadas
    if not re.search(r'^[\s]*[-*] ', conteudo, re.MULTILINE):
        audit.observacoes.append("❌ Falta listas estruturadas")
    
    return audit

def main():
    """Executa auditoria completa das 16 aulas"""
    console = Console()
    
    print("\n[bold cyan]🔍 AUDITORIA DAS AULAS - ADM GESTÃO TI[/bold cyan]")
    print("=" * 60)
    
    audits = []
    
    for i in range(1, 17):
        audit = verificar_aula(i)
        audits.append(audit)
    
    # Criar tabela resumo
    table = Table(title="📊 Resumo da Auditoria")
    
    table.add_column("Aula", justify="center", style="cyan")
    table.add_column("Mermaid", justify="center")
    table.add_column("Termynal", justify="center")
    table.add_column("Emojis", justify="center")
    table.add_column("Destaque", justify="center")
    table.add_column("Exemplos", justify="center")
    table.add_column("Nível", justify="center")
    table.add_column("Status", justify="center")
    
    for audit in audits:
        status = "✅" if len(audit.observacoes) == 0 else "⚠️" if len(audit.observacoes) <= 2 else "❌"
        
        table.add_row(
            f"{audit.numero:02d}",
            "✅" if audit.tem_mermaid else "❌",
            "✅" if audit.tem_termynal else "❌",
            "✅" if audit.tem_emoji else "❌",
            "✅" if audit.tem_admonitions else "❌",
            "✅" if audit.tem_exemplos else "❌",
            audit.nivel_conteudo,
            status
        )
    
    console.print(table)
    
    # Relatório detalhado
    print("\n[bold yellow]📋 RELATÓRIO DETALHADO[/bold yellow]")
    
    for audit in audits:
        if audit.observacoes:
            print(f"\n[bold]📄 Aula {audit.numero:02d}:[/bold]")
            for obs in audit.observacoes:
                print(f"  • {obs}")
    
    # Estatísticas globais
    total_ok = sum(1 for audit in audits if len(audit.observacoes) == 0)
    total_warning = sum(1 for audit in audits if 0 < len(audit.observacoes) <= 2)
    total_error = sum(1 for audit in audits if len(audit.observacoes) > 2)
    
    print(f"\n[bold green]📈 ESTATÍSTICAS GLOBAIS:[/bold green]")
    print(f"✅ Aulas em conformidade: {total_ok}/16")
    print(f"⚠️  Aulas com pequenos ajustes: {total_warning}/16") 
    print(f"❌ Aulas que precisam revisão: {total_error}/16")
    
    # Recomendações
    print(f"\n[bold blue]🎯 PRÓXIMOS PASSOS:[/bold blue]")
    
    if total_error > 0:
        print("1. 🔥 PRIORIDADE ALTA: Revisar aulas com muitos problemas")
        
    aulas_sem_termynal = [a.numero for a in audits if not a.tem_termynal]
    if aulas_sem_termynal:
        print(f"2. 💻 Adicionar exemplos TermynalJS nas aulas: {', '.join(map(str, aulas_sem_termynal))}")
    
    aulas_sem_admonitions = [a.numero for a in audits if not a.tem_admonitions]
    if aulas_sem_admonitions:
        print(f"3. 🧠 Adicionar blocos de destaque nas aulas: {', '.join(map(str, aulas_sem_admonitions))}")
        
    aulas_basicas = [a.numero for a in audits if a.nivel_conteudo == "básico"]
    if aulas_basicas:
        print(f"4. 📈 Expandir conteúdo para intermediário nas aulas: {', '.join(map(str, aulas_basicas))}")

if __name__ == '__main__':
    main()