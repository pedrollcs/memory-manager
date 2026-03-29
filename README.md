# 🧠 Multi-Agent Memory (MAM)

> Sistema de persistência de conhecimento para projetos desenvolvidos por múltiplos agentes de IA.

O **Multi-Agent Memory (MAM)** é uma solução desenhada para resolver o problema da **"Amnésia de Contexto"**. Quando diferentes IAs (Claude, Gemini, Cursor, ChatGPT, etc.) trabalham em um mesmo projeto de forma assíncrona, informações críticas de design, decisões de arquitetura e regras de negócio tendem a se perder, resultando em retrabalho, inconsistências e desperdício de tokens.

Este repositório serve como a base e o guia para implementar o sistema de memória em qualquer projeto de desenvolvimento.

---

## 🚀 Como Funciona

O sistema baseia-se na criação de um diretório `/memory` na raiz do seu projeto. Este diretório funciona como a **fonte da verdade** do projeto para qualquer agente de IA.

### O Fluxo de Trabalho (Protocolo)

Todo agente de IA deve seguir este protocolo rigoroso:

1.  **🟢 CHECK-IN (Início da tarefa):**
    *   Leia `/memory/readme.md` para entender as regras do sistema.
    *   Consulte `/memory/index.md` (o "Router de Contexto") para identificar quais arquivos de memória são relevantes para a tarefa atual.
    *   Carregue **apenas** o contexto necessário para economizar tokens e evitar confusão.

2.  **🟡 EXECUÇÃO:**
    *   Desenvolva a funcionalidade, mantendo registro mental das decisões tomadas, componentes criados e novos padrões estabelecidos.

3.  **🔴 CHECK-OUT (Fim da tarefa):**
    *   Atualize ou crie o arquivo da funcionalidade em `/memory/features/`.
    *   Se houve mudanças estruturais, atualize os arquivos em `/memory/project/`.
    *   Atualize o índice global em `/memory/index.md`.

---

## 📁 Estrutura do Sistema de Memória

O diretório `/memory` segue uma organização lógica para facilitar o consumo por IAs:

```text
/memory
├── readme.md          # Protocolos e regras de uso do sistema
├── index.md           # Índice centralizado (mapa de todas as memórias)
├── /project           # Contexto permanente (raramente muda)
│   ├── context.md     # Visão macro: negócio, stack, visão geral
│   ├── arch.md        # Arquitetura: infra, pastas, padrões de código
│   └── design.md      # Design System: tokens, componentes, regras de UI
└── /features          # Contexto granular por funcionalidade
    ├── auth.md        # Histórico da feature de Autenticação
    ├── payments.md    # Detalhes técnicos do sistema de pagamentos
    └── ...
```

---

## 🛠️ Como Instalar no seu Projeto

Para começar a usar o MAM no seu repositório:

1.  Copie a pasta `skills/memory-manager/assets/templates/` deste repositório para o seu projeto, renomeando-a para `/memory`.
2.  Preencha os arquivos em `project/` com as informações básicas do seu sistema (Stack, Arquitetura, Design).
3.  Garanta que o `readme.md` e o `index.md` estejam na raiz da pasta `/memory`.
4.  **Dica Ouro:** Instrua sua IA (através do System Prompt ou Custom Instructions) a sempre verificar a pasta `/memory` no início de cada sessão.

---

## 💎 Benefícios

*   **Economia de Tokens:** As IAs não precisam ler todo o código para entender o progresso.
*   **Continuidade de Design:** Evita que novos agentes ignorem o Design System estabelecido.
*   **Decisões Documentadas:** Registra o "porquê" das coisas, algo que o código sozinho nem sempre explica.
*   **Colaboração Híbrida:** Facilita a transição de tarefas entre humanos e IAs.

---

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para adaptá-lo às necessidades do seu time de agentes.

---
*Desenvolvido para orquestrar o conhecimento na era da engenharia de software assistida por IA.*
