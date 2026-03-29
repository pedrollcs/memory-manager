# 📋 Índice de Memórias

> **Para agentes de IA:** Leia este arquivo PRIMEIRO. Identifique quais memórias são relevantes
> para sua tarefa atual e carregue apenas essas. Não leia todos os arquivos — otimize tokens.

**Última atualização:** YYYY-MM-DD  
**Atualizado por:** [agente/pessoa]

---

## Projeto (Contexto Estrutural)

Memórias que raramente mudam. Leia na primeira interação com o projeto.

| Arquivo | Descrição | Quando carregar |
|---|---|---|
| [`project/context.md`](project/context.md) | Visão macro do negócio, stack tecnológica e convenções gerais | Primeira interação ou dúvida sobre o projeto |
| [`project/arch.md`](project/arch.md) | Arquitetura do sistema, estrutura de pastas, infra e deploy | Tarefas que envolvem criar arquivos, módulos ou alterar infra |
| [`project/design.md`](project/design.md) | Design System: tokens, componentes, regras de UI/UX | Tarefas de frontend ou criação de interfaces |

---

## Features (Contexto por Funcionalidade)

Memórias granulares. Carregue apenas as features relacionadas à sua tarefa.

| Arquivo | Feature | Status | Resumo |
|---|---|---|---|
| [`features/auth.md`](features/auth.md) | Autenticação | ✅ Concluída | Login, registro, sessões e permissões |
| [`features/proposals.md`](features/proposals.md) | Propostas Comerciais | 🔨 Em progresso | CRUD de propostas e geração de PDF |

<!-- 
TEMPLATE PARA NOVAS ENTRADAS:
| [`features/nome-da-feature.md`](features/nome-da-feature.md) | Nome da Feature | 🔨/✅/⏸️ | Resumo em uma linha |

LEGENDA DE STATUS:
✅ Concluída — implementada e estável
🔨 Em progresso — sendo desenvolvida ativamente  
⏸️ Pausada — iniciada mas parada temporariamente
📋 Planejada — documentada mas não iniciada
🔄 Em revisão — implementada, aguardando review
-->
