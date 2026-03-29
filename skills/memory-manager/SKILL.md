---
name: multi-agent-memory
description: >
  Sistema de memória persistente para projetos desenvolvidos por múltiplos agentes de IA.
  Use esta skill SEMPRE que iniciar qualquer tarefa de desenvolvimento em um projeto que contenha
  o diretório `/memory`. Também use quando o usuário pedir para criar, consultar, ou atualizar
  memórias de projeto, registrar decisões de arquitetura, documentar uma feature nova, ou quando
  precisar entender o contexto atual do projeto antes de codificar. Gatilhos incluem: menções a
  "memória", "memory", "contexto do projeto", "decisão de arquitetura", "design system",
  "o que já foi feito", "histórico de decisões", ou qualquer tarefa de código em repo com /memory.
---

# Multi-Agent Memory System

Sistema de persistência de conhecimento que resolve a "Amnésia de Contexto" — a perda de informação
que ocorre quando múltiplos agentes de IA (Claude, Gemini, Cursor, Codex, etc.) trabalham no mesmo
projeto de forma assíncrona.

## Por que isso existe

Sem memória compartilhada, cada agente que entra numa tarefa:
- Tenta ler todo o codebase para entender o estado atual (desperdiça tokens)
- Desconhece decisões de design tomadas por outro agente (gera conflitos)
- Pode desfazer ou contradizer implementações anteriores (cria um "Frankenstein")

O diretório `/memory` é a **fonte da verdade** do projeto.

---

## Protocolo de Operação

### 1. CHECK-IN (Início de qualquer tarefa)

Antes de escrever uma única linha de código:

```
1. Leia /memory/readme.md  → entenda as regras do sistema
2. Leia /memory/index.md   → identifique quais memórias são relevantes para sua tarefa
3. Carregue APENAS as memórias relevantes → não leia tudo, seja cirúrgico
4. Leia /memory/project/context.md → se for sua primeira interação com o projeto
```

O `index.md` funciona como um router de contexto. Cada entrada tem um título, uma descrição
de 1-2 linhas, e o caminho do arquivo. Leia o índice, identifique o que importa, carregue só isso.

**Exemplo:** Se a tarefa é "criar tela de login", carregue `project/design.md` (tokens de UI),
`project/arch.md` (estrutura de pastas), e `features/auth.md` (se existir). Não carregue
`features/billing.md`.

### 2. EXECUÇÃO (Durante a tarefa)

Trabalhe normalmente, mas mantenha uma lista mental de:
- Decisões de arquitetura ou design que você tomou
- Componentes novos que você criou
- Padrões que você estabeleceu ou modificou
- Dependências que você adicionou
- Qualquer coisa que outro agente PRECISARIA saber para não quebrar seu trabalho

### 3. CHECK-OUT (Fim da tarefa)

Esta é a parte mais importante. Antes de encerrar:

```
1. Atualize ou crie o arquivo de feature em /memory/features/
2. Atualize o /memory/index.md com a nova entrada (se criou arquivo novo)
3. Se mudou algo estrutural, atualize o arquivo relevante em /memory/project/
```

**Regra de Ouro:** Se você criou algo novo ou tomou uma decisão que afeta o futuro do projeto,
registre. Prefira registrar demais do que de menos.

---

## Estrutura do Diretório `/memory`

```
/memory
├── readme.md          # Regras para IAs (como ler/escrever memórias)
├── index.md           # Router de contexto (sumário com links)
├── /project           # Memórias permanentes — raramente mudam
│   ├── context.md     # Visão macro: negócio, stack, convenções
│   ├── arch.md        # Arquitetura: infra, pastas, deploys
│   └── design.md      # Design System: tokens, componentes, regras de UI
└── /features          # Memórias granulares — uma por feature/domínio
    ├── auth.md
    ├── billing.md
    └── ...
```

### Tipos de Memória

**Nível de Projeto (`/project`)** — Contexto estrutural que raramente muda:
- Stack tecnológica e versões
- Estrutura de pastas e convenções de nomenclatura
- Padrões de Design System (tokens, componentes base)
- Configurações de infra e deploy
- Regras de banco de dados e migrações

**Nível de Feature (`/features`)** — Registro granular por funcionalidade:
- O que foi implementado e por quê
- Decisões técnicas tomadas (e alternativas descartadas)
- Componentes criados ou modificados
- Dependências introduzidas
- Status atual e próximos passos

---

## Como Escrever Boas Memórias

### Formato de Feature

Cada arquivo de feature segue uma estrutura consistente. Consulte os templates em
`templates/features/` para o formato exato, mas os princípios são:

1. **Título e status** — Nome da feature e se está em progresso, concluída, ou em revisão
2. **Resumo em 2-3 linhas** — O que é e por que existe
3. **Decisões técnicas** — O que foi decidido e qual era a alternativa
4. **Componentes afetados** — Lista de arquivos criados ou modificados
5. **Regras para o próximo agente** — O que NÃO fazer, o que manter, armadilhas conhecidas

### Princípios de Escrita

- **Seja conciso mas completo.** Cada token conta. Escreva para um agente de IA que precisa
  entender rapidamente o que aconteceu, não para um humano que vai ler um relatório.
- **Priorize o "por quê" sobre o "como".** Outro agente pode ler o código para ver o "como".
  O que ele não consegue inferir é o contexto da decisão.
- **Use listas e headers.** Facilitam o parsing por outros agentes.
- **Registre as "anti-decisões".** "Não usamos Redux porque..." é tão valioso quanto "Usamos Zustand porque...".

---

## Comandos Rápidos

Se o usuário solicitar ações de memória, execute conforme abaixo:

| Comando do usuário | Ação |
|---|---|
| "registra essa decisão" | Crie/atualize o arquivo de feature relevante + atualize index.md |
| "qual o contexto do projeto?" | Leia e resuma `/memory/project/context.md` |
| "o que já foi feito em [feature]?" | Busque no index.md e carregue o arquivo da feature |
| "inicializa a memória" | Copie os templates para `/memory` e ajude a preencher `context.md` |
| "atualiza o índice" | Releia todos os arquivos em `/memory` e regenere o `index.md` |

---

## Inicialização

Para criar o sistema de memória em um projeto novo:

1. Copie a pasta `templates/` desta skill para o diretório raiz do projeto como `/memory`
2. Preencha `/memory/project/context.md` com as informações do projeto
3. Preencha `/memory/project/arch.md` com a arquitetura atual
4. Preencha `/memory/project/design.md` se houver Design System
5. O `readme.md` e `index.md` já vêm com conteúdo base — ajuste conforme necessário

Os templates estão em: `templates/` (relativo a esta skill).
