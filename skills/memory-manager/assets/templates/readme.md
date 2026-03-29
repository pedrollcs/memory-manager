# 🧠 Memory System — Regras de Uso

> Este arquivo define o protocolo que **todo agente de IA** deve seguir ao trabalhar neste projeto.
> Leia-o por completo na sua primeira interação. Nas seguintes, vá direto ao `index.md`.

---

## O que é o `/memory`

Este diretório é a **memória compartilhada** do projeto. Ele existe para resolver um problema
simples: quando múltiplas IAs (Claude, Gemini, Cursor, Codex, etc.) trabalham no mesmo repositório,
o conhecimento se perde entre sessões. Aqui é onde esse conhecimento é persistido.

**Você, agente, é tanto consumidor quanto autor** destas memórias.

---

## Protocolo: Check-in / Check-out

### 🟢 Check-in (Antes de começar qualquer tarefa)

1. **Leia este arquivo** (você já está fazendo isso ✓)
2. **Leia `index.md`** — é o mapa de todas as memórias disponíveis
3. **Carregue apenas o necessário** — identifique no índice quais memórias são relevantes para sua tarefa e carregue só essas. Não leia tudo.
4. **Se é sua primeira vez no projeto**, leia também `project/context.md` para entender a visão macro

### 🔴 Check-out (Antes de encerrar a tarefa)

Se você criou algo novo, tomou uma decisão de arquitetura, ou mudou um comportamento existente:

1. **Crie ou atualize** o arquivo de feature em `/memory/features/nome_da_feature.md`
2. **Atualize `index.md`** adicionando a nova entrada (se criou um arquivo novo)
3. **Se alterou algo estrutural** (stack, pastas, deploy, design system), atualize o arquivo relevante em `/memory/project/`

> **Regra de Ouro:** Na dúvida, registre. Prefira registrar demais do que de menos.
> O custo de uma memória extra é mínimo. O custo de um agente futuro sem contexto é alto.

---

## Regras de Escrita

### O que registrar

- Decisões de arquitetura ou design e **por que** foram tomadas
- Componentes, módulos ou serviços novos criados
- Padrões estabelecidos que devem ser seguidos por futuros agentes
- Dependências adicionadas ao projeto
- Mudanças em regras de negócio
- Armadilhas conhecidas (bugs, limitações, workarounds)
- **Anti-decisões**: alternativas consideradas e descartadas (e por que)

### O que NÃO registrar

- Detalhes de implementação triviais (o código já documenta isso)
- Bugs temporários que já foram corrigidos
- Informações que mudam a cada commit (use git para isso)

### Como registrar

- Use Markdown com headers e listas — facilita o parsing por outros agentes
- Seja conciso: escreva para uma IA que precisa entender rápido, não para um relatório humano
- Priorize o **"por quê"** sobre o **"como"** — o "como" está no código
- Sempre inclua **data** (`YYYY-MM-DD`) e **autor** (nome do agente ou desenvolvedor)
- Use o template de features como base (veja `/memory/features/` para exemplos)

---

## Estrutura de Pastas

```
/memory
├── readme.md        ← Você está aqui. Regras do sistema.
├── index.md         ← Mapa de todas as memórias. Leia sempre.
├── /project         ← Memórias estruturais (mudam raramente)
│   ├── context.md   ← Visão macro: negócio, stack, público
│   ├── arch.md      ← Arquitetura: pastas, infra, deploy
│   └── design.md    ← Design System: tokens, componentes, regras
└── /features        ← Memórias de funcionalidades (mudam frequentemente)
    └── *.md         ← Uma por feature ou domínio
```

---

## Convenções de Nomenclatura

- Arquivos de feature: `kebab-case.md` (ex: `user-auth.md`, `payment-flow.md`)
- Sem espaços, sem caracteres especiais, sem acentos nos nomes de arquivo
- Agrupe por domínio, não por sprint ou data

---

## Conflitos

Se você encontrar uma memória que contradiz o estado atual do código:

1. **O código é a verdade.** Ele reflete o que realmente está implementado.
2. **Atualize a memória** para refletir o estado real.
3. **Registre a correção** com uma nota explicando a divergência.

---

## Para Humanos

Se você é um desenvolvedor humano lendo isso: este sistema funciona melhor quando você também
participa. Ao tomar decisões importantes, registre-as aqui. Ao revisar PRs gerados por IA,
verifique se a memória foi atualizada. O `/memory` só é útil se estiver atualizado.
