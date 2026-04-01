# Guia de Escrita de Memórias

> Carregado sob demanda. Consulte quando precisar escrever ou melhorar memórias.

---

## Tipos de Memória

### Nível de Projeto (`/project`) — Contexto estrutural, muda raramente

- Stack tecnológica e versões
- Estrutura de pastas e convenções de nomenclatura
- Padrões de Design System (tokens, componentes base)
- Configurações de infra e deploy
- Regras de banco de dados e migrações
- Multi-tenancy e segurança

### Nível de Feature (`/features`) — Registro granular, muda frequentemente

- O que foi implementado e por quê
- Decisões técnicas tomadas (e alternativas descartadas)
- Componentes criados ou modificados
- Dependências introduzidas
- Status atual e próximos passos
- Regras e armadilhas para o próximo agente

---

## Princípios de Escrita

### Priorize o "por quê" sobre o "como"

Outro agente pode ler o código para ver o "como". O que ele NÃO consegue inferir é
o contexto da decisão. Compare:

```markdown
# ❌ Fraco — descreve o que o código já mostra
Usamos Zustand para gerenciar estado global.

# ✅ Forte — explica o contexto que o código não mostra
Escolhemos Zustand sobre Redux porque o projeto tem poucos stores globais (3-4),
e a API do Zustand elimina boilerplate. Context API foi descartado porque causava
re-renders desnecessários no dashboard de métricas.
```

### Registre Anti-decisões

"Não usamos Redux porque..." é tão valioso quanto "Usamos Zustand porque...".
Anti-decisões evitam que agentes futuros reproponham ideias já avaliadas e descartadas.

### Seja conciso mas completo

Cada token conta. Escreva para um agente de IA que precisa entender rapidamente,
não para um relatório humano. Use Markdown com headers e listas — facilita parsing.

### Sempre inclua metadata

- **Data:** `YYYY-MM-DD`
- **Autor:** Nome do agente ou desenvolvedor
- **Status:** Use os emojis padronizados (📋 🔨 🔄 ✅ ⏸️)

---

## O que Registrar vs. O que Ignorar

### ✅ Registrar

- Decisões de arquitetura ou design e por que foram tomadas
- Componentes, módulos ou serviços novos criados
- Padrões estabelecidos que devem ser seguidos
- Dependências adicionadas ao projeto
- Mudanças em regras de negócio
- Armadilhas conhecidas (bugs, limitações, workarounds)
- Anti-decisões: alternativas consideradas e descartadas

### ❌ Não Registrar

- Detalhes de implementação triviais (o código documenta isso)
- Bugs temporários que já foram corrigidos
- Informações que mudam a cada commit (use git)
- Secrets, credenciais, tokens de acesso
- Opiniões pessoais sem impacto técnico

---

## Formato de Feature (Referência Rápida)

Todo arquivo de feature segue esta estrutura. Use o template completo em
`assets/templates/features/_template.md`.

```
1. Título + Status + Data + Autor
2. Resumo em 2-3 linhas (o que é, por que existe)
3. Decisões técnicas (escolha, motivo, alternativas descartadas)
4. Arquivos principais (tabela com path e propósito)
5. Dependências introduzidas (pacote@versão + para quê)
6. Regras para o próximo agente (FAÇA, NÃO FAÇA, CUIDADO)
7. Status & Próximos passos (checklist)
8. Changelog (tabela: data | autor | mudança)
```

---

## Convenções de Nomenclatura

- Arquivos de feature: `kebab-case.md` (ex: `user-auth.md`, `payment-flow.md`)
- Sem espaços, sem caracteres especiais, sem acentos nos nomes de arquivo
- Agrupe por domínio, não por sprint ou data
- Um arquivo por feature/domínio — não por tarefa individual
