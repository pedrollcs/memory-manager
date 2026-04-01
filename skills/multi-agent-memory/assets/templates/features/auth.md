# Autenticação & Autorização

> Sistema de login, registro, sessões e controle de permissões por role.

**Status:** ✅ Concluída  
**Última atualização:** 2025-03-15  
**Autor:** Claude (Anthropic)

---

## Resumo

Implementação de autenticação completa via Supabase Auth com suporte a login por e-mail/senha
e OAuth (Google). Inclui middleware de proteção de rotas, gerenciamento de sessões server-side,
e sistema de roles (admin, member, viewer) armazenado em `user_metadata`.

---

## Decisões Técnicas

### Estratégia de autenticação
- **Escolha:** Supabase Auth com PKCE flow
- **Motivo:** Já usamos Supabase como banco; unificar reduz complexidade e custo
- **Alternativas descartadas:** NextAuth.js (adiciona camada extra desnecessária), Auth0 (custo alto para o estágio atual)

### Armazenamento de sessão
- **Escolha:** Cookies HTTP-only via `@supabase/ssr`
- **Motivo:** Segurança contra XSS; funciona com SSR e RSC do Next.js
- **Alternativas descartadas:** localStorage (vulnerável a XSS), session storage (não persiste entre abas)

### Controle de permissões
- **Escolha:** Roles em `user_metadata` + RLS no banco
- **Motivo:** Dupla camada de segurança — app e banco validam independentemente
- **Alternativas descartadas:** RBAC via tabela separada (over-engineering para 3 roles)

---

## Arquivos Principais

| Arquivo | Propósito |
|---|---|
| `src/lib/supabase/client.ts` | Cliente Supabase para browser |
| `src/lib/supabase/server.ts` | Cliente Supabase para server components |
| `src/lib/supabase/middleware.ts` | Refresh de sessão automático |
| `src/middleware.ts` | Proteção de rotas — redireciona não-autenticados |
| `src/app/(auth)/login/page.tsx` | Página de login |
| `src/app/(auth)/register/page.tsx` | Página de registro |
| `src/app/(auth)/callback/route.ts` | Callback do OAuth |
| `src/hooks/useAuth.ts` | Hook com user, role, isLoading, signOut |
| `src/components/features/auth/AuthGuard.tsx` | Wrapper de proteção por role |

---

## Dependências Introduzidas

- `@supabase/supabase-js@2.x` — SDK principal
- `@supabase/ssr@0.x` — Helpers para SSR (cookies, middleware)

---

## Regras para o Próximo Agente

> ⚠️ Leia com atenção antes de modificar qualquer coisa relacionada a auth.

- **FAÇA:** Use `useAuth()` para verificar o usuário logado e seu role
- **FAÇA:** Use `<AuthGuard requiredRole="admin">` para proteger seções da UI
- **FAÇA:** Sempre use o client de `lib/supabase/server.ts` em server components
- **NÃO FAÇA:** Não crie rotas de API sem `createServerClient()` para validar a sessão
- **NÃO FAÇA:** Não armazene tokens manualmente — o `@supabase/ssr` gerencia isso
- **NÃO FAÇA:** Não duplique lógica de permissão — centralize em `useAuth` e `AuthGuard`
- **CUIDADO:** O middleware faz refresh automático do token — se alterar `middleware.ts`, teste o fluxo de sessão expirada

---

## Status & Próximos Passos

- [x] Login com e-mail/senha
- [x] Login com Google OAuth
- [x] Middleware de proteção de rotas
- [x] Hook `useAuth` com role
- [x] Componente `AuthGuard`
- [x] RLS nas tabelas principais
- [ ] Login com Magic Link (backlog)
- [ ] Página de "esqueci minha senha"

---

## Changelog

| Data | Autor | Mudança |
|---|---|---|
| 2025-03-01 | Claude | Criação inicial: login e-mail/senha + middleware |
| 2025-03-08 | Cursor | Adicionado Google OAuth + callback route |
| 2025-03-15 | Claude | Implementado AuthGuard e sistema de roles |
