# 🏗️ Arquitetura do Sistema

> Decisões de infraestrutura, estrutura de pastas e padrões de organização.
> Carregue ao criar novos arquivos, módulos, ou alterar a infra.

**Última atualização:** YYYY-MM-DD  
**Atualizado por:** [agente/pessoa]

---

## Estrutura de Pastas

```
/
├── src/
│   ├── app/               # [descreva: ex: App Router do Next.js - rotas e layouts]
│   ├── components/        # [descreva: ex: Componentes React reutilizáveis]
│   │   ├── ui/            # [descreva: ex: Componentes base do Design System]
│   │   └── features/      # [descreva: ex: Componentes específicos de features]
│   ├── lib/               # [descreva: ex: Utilitários, helpers, clients]
│   ├── hooks/             # [descreva: ex: Custom hooks do React]
│   ├── services/          # [descreva: ex: Camada de acesso a APIs e serviços]
│   ├── types/             # [descreva: ex: Types e interfaces TypeScript]
│   └── config/            # [descreva: ex: Constantes e configurações]
├── prisma/                # [descreva: ex: Schema e migrações do Prisma]
├── public/                # [descreva: ex: Assets estáticos]
├── memory/                # Sistema de memória do projeto (você está aqui)
└── ...
```

> **Para agentes:** Ao criar um novo arquivo, siga esta estrutura. Não crie pastas novas
> sem registrar a decisão neste arquivo.

---

## Padrões de Arquitetura

### Organização de Componentes
[Descreva o padrão. Exemplo:]
- Componentes de UI genéricos vão em `components/ui/`
- Componentes específicos de uma feature vão em `components/features/[feature-name]/`
- Cada componente complexo tem sua pasta: `ComponentName/index.tsx` + `ComponentName.types.ts`

### Camada de Dados
[Descreva o padrão. Exemplo:]
- Acesso ao banco via Prisma, centralizado em `services/`
- Cada domínio tem seu service: `services/user.service.ts`, `services/billing.service.ts`
- Server Actions do Next.js para mutações simples, API Routes para lógica complexa

### Autenticação & Autorização
[Descreva o padrão. Exemplo:]
- Supabase Auth com middleware de proteção em `middleware.ts`
- Roles: `admin`, `member`, `viewer` — armazenados em `user_metadata`

### Gerenciamento de Estado
[Descreva o padrão. Exemplo:]
- Estado local: `useState` / `useReducer`
- Estado global: Zustand stores em `lib/stores/`
- Estado do servidor: TanStack Query com keys padronizadas

---

## Banco de Dados

### Convenções
- [ex: Tabelas em snake_case, colunas em snake_case]
- [ex: Toda tabela tem `id` (UUID), `created_at`, `updated_at`]
- [ex: Soft delete via coluna `deleted_at` (nullable)]
- [ex: Foreign keys seguem o padrão `{tabela_referenciada}_id`]

### Migrações
- [ex: Geradas via `npx prisma migrate dev --name descricao-da-mudanca`]
- [ex: Nunca editar migrações já aplicadas em produção]

### Multi-tenancy
- [ex: Todas as queries filtram por `organization_id` — nunca retornar dados sem este filtro]
- [ex: RLS (Row Level Security) ativo no Supabase para todas as tabelas]

---

## Deploy & Ambientes

| Ambiente | URL | Branch | Deploy |
|---|---|---|---|
| Desenvolvimento | localhost:3000 | `dev` | Local |
| Staging | [URL] | `staging` | [ex: Auto via push] |
| Produção | [URL] | `main` | [ex: Manual via tag] |

### Variáveis de Ambiente
- [ex: `.env.local` para desenvolvimento — nunca commitar]
- [ex: Variáveis obrigatórias listadas em `.env.example`]
- [ex: Segredos gerenciados via Vercel/AWS Secrets Manager]

---

## Decisões Arquiteturais Importantes

<!-- Registre aqui decisões que afetam todo o projeto -->

### [YYYY-MM-DD] [Título da decisão]
**Contexto:** [Por que essa decisão foi necessária]  
**Decisão:** [O que foi decidido]  
**Alternativas descartadas:** [O que foi considerado e por quê não]  
**Consequências:** [O que muda a partir desta decisão]
