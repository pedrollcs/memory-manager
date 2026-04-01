# Propostas Comerciais

> CRUD de propostas com geração automática de PDF e envio por e-mail.

**Status:** 🔨 Em progresso  
**Última atualização:** 2025-03-20  
**Autor:** Gemini

---

## Resumo

Módulo para criação e gestão de propostas comerciais. O usuário monta a proposta via formulário
(dados do cliente, itens, condições), o sistema gera um PDF estilizado e permite envio direto
por e-mail. Inclui dashboard de acompanhamento com status (rascunho, enviada, visualizada, aceita, recusada).

---

## Decisões Técnicas

### Geração de PDF
- **Escolha:** `@react-pdf/renderer` com templates React
- **Motivo:** Permite estilização rica com JSX; roda server-side; boa DX
- **Alternativas descartadas:** Puppeteer (pesado, complexo de deployar), jsPDF (API de baixo nível, difícil manter templates)

### Tracking de visualização
- **Escolha:** Pixel tracking via API route + token único por proposta
- **Motivo:** Simples, não requer JS no e-mail do cliente
- **Alternativas descartadas:** Link de visualização com analytics (requer página intermediária)

### Status da proposta
- **Escolha:** Enum no banco: `draft`, `sent`, `viewed`, `accepted`, `rejected`
- **Motivo:** Máquina de estados simples, sem necessidade de workflow engine
- **Alternativas descartadas:** Estado derivado (calculado a partir de eventos) — over-engineering

---

## Arquivos Principais

| Arquivo | Propósito |
|---|---|
| `src/app/(dashboard)/proposals/page.tsx` | Listagem de propostas com filtros |
| `src/app/(dashboard)/proposals/new/page.tsx` | Formulário de criação |
| `src/app/(dashboard)/proposals/[id]/page.tsx` | Visualização e edição |
| `src/services/proposal.service.ts` | CRUD no banco + lógica de negócio |
| `src/lib/pdf/proposal-template.tsx` | Template React-PDF da proposta |
| `src/lib/pdf/generate.ts` | Função de geração do PDF |
| `src/app/api/proposals/[id]/track/route.ts` | Pixel tracking de visualização |
| `prisma/migrations/20250318_proposals/` | Migração da tabela `proposals` + `proposal_items` |

---

## Dependências Introduzidas

- `@react-pdf/renderer@3.x` — Geração de PDF com React
- `resend@3.x` — Envio de e-mails transacionais (já existia no projeto)

---

## Regras para o Próximo Agente

> ⚠️ Feature em desenvolvimento ativo. Cuidado com conflitos.

- **FAÇA:** Use o `proposal.service.ts` para qualquer operação no banco — não acesse direto
- **FAÇA:** Siga o template de PDF existente (`proposal-template.tsx`) como base para variações
- **NÃO FAÇA:** Não altere a migração já aplicada — crie uma nova migração para mudanças no schema
- **NÃO FAÇA:** Não mude o enum de status sem atualizar a máquina de estados em `proposal.service.ts`
- **CUIDADO:** O PDF é gerado server-side — componentes usados no template não podem usar hooks de browser
- **CUIDADO:** O tracking de visualização depende da API route em `/api/proposals/[id]/track` — não renomear sem atualizar os links gerados nos e-mails

---

## Status & Próximos Passos

- [x] Schema do banco (proposals + proposal_items)
- [x] CRUD via service
- [x] Formulário de criação
- [x] Template de PDF
- [x] Geração de PDF server-side
- [ ] Envio por e-mail com PDF anexo
- [ ] Pixel tracking de visualização
- [ ] Dashboard com métricas (taxa de conversão, tempo médio de resposta)
- [ ] Duplicação de propostas existentes

---

## Changelog

| Data | Autor | Mudança |
|---|---|---|
| 2025-03-10 | Gemini | Criação do schema e CRUD base |
| 2025-03-14 | Claude | Template de PDF e geração server-side |
| 2025-03-20 | Gemini | Formulário de criação + listagem com filtros |
