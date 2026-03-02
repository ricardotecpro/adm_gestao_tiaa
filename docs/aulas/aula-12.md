# Aula 12 - E-mail Corporativo e Ferramentas de Comunicação 📧

!!! tip "Objetivo"
    **Objetivo**: Entender a importância da comunicação formal no ambiente empresarial, aprender as boas práticas de uso do e-mail corporativo e conhecer ferramentas modernas de colaboração interna.

---

## 1. O E-mail como Documento Oficial 📑

No mundo dos negócios, o e-mail não é apenas uma mensagem; ele é um **registro documental**. Acordos, aprovações e instruções enviadas por e-mail têm valor administrativo e, muitas vezes, jurídico.

### 🌟 Regras de Ouro do E-mail Corporativo:
*   **Assunto Claro**: Deve resumir o conteúdo (ex: "Aprovação de Orçamento - Projeto X").
*   **Profissionalismo**: Evite gírias, use saudação e assinatura formal.
*   **Gramática e Ortografia**: Revisar sempre antes de enviar.
*   **Cópia (CC e CCO)**: Use CC para manter pessoas informadas e CCO quando precisar ocultar destinatários por privacidade.

---

## 2. Ferramentas de Colaboração (Chat e Projetos) 💬

Além do e-mail, as empresas modernas utilizam ferramentas de comunicação em tempo real e gestão de tarefas.

### 🗨️ Chat Corporativo (Slack / Microsoft Teams)
Focado em conversas rápidas, troca de arquivos e reuniões por vídeo. Reduz o volume de e-mails internos.

### 📋 Gestão de Tarefas (Trello / Jira / Asana)
Sistemas onde o administrador delega funções e acompanha o progresso de cada projeto através de quadros (Kanban).

---

## 3. Fluxo de Comunicação Interna (Mermaid) 🌊

A informação deve circular de forma eficiente entre os colaboradores.

```mermaid
graph LR
    D[Diretoria] -- "E-mail (Oficial)" --> G[Gerentes]
    G -- "Teams/Slack (Alinhamento)" --> E[Equipes]
    E -- "Trello (Status)" --> G
    G -- "Relatório" --> D
    style G fill:#f9f,stroke:#333
```

---

## 4. Simulando a Gestão de Comunicação no Terminal 🚀

Visualize como o sistema integra e-mail e tarefas:

<!-- termynal -->
```bash
$ comunicacao-enviar-aviso --setor "Financeiro" --msg "Reunião de metas amanhã às 09h"
[E-MAIL] Enviando para 15 destinatários... [OK]
[SLACK] Postando no canal #financeiro-avisos... [OK]
$ projeto-criar-tarefa --quadro "Expansão" --titulo "Análise de novo ponto"
[TRELLO] Tarefa criada na coluna 'A fazer'.
[NOTIFICAÇÃO] Gestor alertado via e-mail corporativo.
```

---

## 5. Mini-Projeto: Etiqueta no E-mail 🚀

Sua missão é atuar como um gestor de RH:

1.  Um funcionário enviou um e-mail para toda a empresa com o assunto "ALGUÉM ESQUECEU O CARRO ACESO NO ESTACIONAMENTO!!!!!!" (tudo em maiúsculas).
2.  Aponte **2 erros de etiqueta** nesse e-mail.
3.  Reescreva o e-mail de forma profissional.
    *   *Exemplo*: Erros: Títulos em maiúsculas (gritar) e falta de clareza no assunto. Sugestão: "Aviso: Veículo com luzes acesas no estacionamento".

---

## 6. Exercício de Fixação 🧠

Responda em seu caderno/arquivo de notas:

1.  Por que o e-mail corporativo ainda é essencial, mesmo com o uso de chats como Slack?
2.  Explique a diferença entre enviar um e-mail em CC (Cópia Carbono) e CCO (Cópia Carbono Oculta).
3.  Como ferramentas de gestão como o Trello ajudam a evitar a "sobrecarga de e-mails"?

---

## 🔗 Materiais da Aula

<div class="grid cards" markdown>
- :material-presentation: **Slides**

    ---

    Material visual com diagramas e conceitos-chave.

    [:octicons-arrow-right-24: Slide 12](../slides/slide-12.html)

- :material-help-circle: **Quiz**

    ---

    Teste seu conhecimento com 10 questões interativas.

    [:octicons-arrow-right-24: Quiz 12](../quizzes/quiz-12.md)

- :fontawesome-solid-pencil: **Exercícios**

    ---

    5 exercícios progressivos (básico → desafio).

    [:octicons-arrow-right-24: Exercício 12](../exercicios/exercicio-12.md)

- :material-briefcase-outline: **Projeto**

    ---

    Aplicação prática dos conceitos da aula.

    [:octicons-arrow-right-24: Projeto 12](../projetos/projeto-12.md)

</div>

---

[➡️ Próxima Aula: Aula 13](./aula-13.md){ .md-button .md-button--primary }
