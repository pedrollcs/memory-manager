---
name: multi-agent-memory
description: >
  Manages persistent project memory for multi-agent development. Creates, reads, and updates
  a /memory directory that stores architectural decisions, feature documentation, design system
  tokens, and project context across AI agent sessions. Use when starting any coding task in a
  repo with a /memory directory, when the user asks to "register a decision", "initialize memory",
  "update context", "what was already done", "project history", "document this feature", or any
  variation of "memory", "context", "decisions log". Also triggers on Portuguese equivalents:
  "registra essa decisão", "qual o contexto", "o que já foi feito", "inicializa a memória",
  "atualiza o índice", "documenta essa feature". Do NOT use for general documentation generation,
  README writing, or changelog management unrelated to the /memory system.
license: MIT
metadata:
  author: pedrollcs
  version: "1.1.0"
  tags: ["memory", "multi-agent", "context", "collaboration", "documentation"]
---

# Multi-Agent Memory (MAM)

Sistema de persistência de conhecimento que resolve a **Amnésia de Contexto** — a perda de
informação quando múltiplos agentes de IA trabalham no mesmo projeto de forma assíncrona.

## Conceito Central

O diretório `/memory` é a **fonte da verdade** do projeto. Todo agente lê antes de agir,
e escreve antes de sair. O sistema usa **progressive disclosure**: o `index.md` funciona
como router — o agente lê o índice, identifica o que importa, e carrega só isso.

---

## Protocolo de Operação

### 1. CHECK-IN (Antes de qualquer tarefa)

```
1. Leia /memory/readme.md           → regras do sistema (só na primeira vez)
2. Leia /memory/index.md            → identifique memórias relevantes
3. Carregue APENAS o necessário     → não leia tudo, seja cirúrgico
4. Leia /memory/project/context.md  → se for sua primeira interação
```

**Exemplo de carregamento seletivo:**
- Tarefa "criar tela de login" → carregue `project/design.md` + `project/arch.md` + `features/auth.md`
- Tarefa "corrigir bug no billing" → carregue `features/billing.md` + `project/arch.md`
- NÃO carregue `features/billing.md` se a tarefa é sobre autenticação

### 2. EXECUÇÃO (Durante a tarefa)

Trabalhe normalmente. Mantenha registro mental de:
- Decisões de arquitetura ou design tomadas
- Componentes novos criados
- Padrões estabelecidos ou modificados
- Dependências adicionadas
- Qualquer coisa que outro agente PRECISARIA saber

### 3. CHECK-OUT (Fim da tarefa)

**Esta é a etapa mais crítica.** Antes de encerrar:

```
1. Crie ou atualize /memory/features/[feature].md
2. Atualize /memory/index.md com a nova entrada (se criou arquivo novo)
3. Se mudou algo estrutural → atualize /memory/project/[arquivo-relevante].md
4. Valide: releia o index.md e confirme que está consistente
```

**Regra de Ouro:** Na dúvida, registre. O custo de uma memória extra é mínimo.
O custo de um agente futuro sem contexto é alto.

### Checklist de Qualidade do Check-out

Antes de considerar o check-out completo, verifique:

- [ ] O arquivo de feature tem Status atualizado?
- [ ] Decisões técnicas incluem o "por quê" e alternativas descartadas?
- [ ] A seção "Regras para o Próximo Agente" cobre armadilhas conhecidas?
- [ ] O changelog da feature foi atualizado com data e autor?
- [ ] O index.md reflete o estado atual (nova entrada ou status atualizado)?
- [ ] Se houve mudança estrutural, o arquivo em /project/ foi atualizado?

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

Para detalhes sobre cada tipo de memória e como escrever boas memórias, consulte
`references/writing-guide.md`.

Para templates prontos de cada tipo de arquivo, consulte `assets/templates/`.

---

## Comandos Rápidos

| Comando do usuário | Ação |
|---|---|
| "registra essa decisão" | Crie/atualize o arquivo de feature relevante + atualize index.md |
| "qual o contexto do projeto?" | Leia e resuma `/memory/project/context.md` |
| "o que já foi feito em [feature]?" | Busque no index.md e carregue o arquivo da feature |
| "inicializa a memória" | Execute o script de inicialização (veja abaixo) |
| "atualiza o índice" | Releia todos os arquivos em `/memory` e regenere o `index.md` |
| "valida a memória" | Execute `scripts/validate.py` para checar consistência |
| "status do projeto" | Leia index.md e gere um resumo dos status de todas as features |

---

## Inicialização

Para criar o sistema de memória em um projeto novo:

```bash
# Copie os templates para a raiz do projeto
cp -r assets/templates/ /path/to/project/memory/

# Ou execute o script de inicialização
python scripts/init_memory.py /path/to/project
```

Depois da cópia:
1. Preencha `/memory/project/context.md` com informações do projeto
2. Preencha `/memory/project/arch.md` com a arquitetura atual
3. Preencha `/memory/project/design.md` se houver Design System
4. Ajuste `readme.md` e `index.md` conforme necessário

---

## Resolução de Conflitos

Se uma memória contradiz o estado atual do código:

1. **O código é a verdade** — ele reflete o que está implementado
2. **Atualize a memória** para refletir o estado real
3. **Registre a correção** com nota explicando a divergência no changelog da feature

---

## Limites desta Skill

- **NÃO substitui documentação de API** — use ferramentas dedicadas (Swagger, etc.)
- **NÃO rastreia mudanças commit-a-commit** — use git para isso
- **NÃO é um sistema de tickets** — registre decisões e contexto, não tarefas pendentes
- **NÃO armazene secrets ou credenciais** nos arquivos de memória
