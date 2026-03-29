# 🎨 Design System

> Tokens, componentes base e regras de UI/UX do projeto.
> Carregue ao criar ou modificar qualquer interface visual.

**Última atualização:** YYYY-MM-DD  
**Atualizado por:** [agente/pessoa]

---

## Biblioteca de Componentes

**Base:** [ex: shadcn/ui / Radix / Material UI / custom]  
**Instalação:** [ex: `npx shadcn@latest add [componente]`]  
**Localização:** [ex: `src/components/ui/`]

---

## Tokens de Design

### Cores

```
Primária:       [ex: --primary: hsl(222, 47%, 31%)]
Secundária:     [ex: --secondary: hsl(210, 40%, 96%)]
Accent:         [ex: --accent: hsl(142, 71%, 45%)]
Destructive:    [ex: --destructive: hsl(0, 84%, 60%)]
Background:     [ex: --background: hsl(0, 0%, 100%)]
Foreground:     [ex: --foreground: hsl(222, 47%, 11%)]
Muted:          [ex: --muted: hsl(210, 40%, 96%)]
Border:         [ex: --border: hsl(214, 32%, 91%)]
```

> **Regra:** Nunca use cores hardcoded (ex: `#3B82F6`). Sempre use os tokens via
> variáveis CSS ou classes do Tailwind (ex: `bg-primary`, `text-destructive`).

### Tipografia

```
Font Family:    [ex: Inter (sans-serif)]
Headings:       [ex: font-bold tracking-tight]
Body:           [ex: font-normal text-base leading-relaxed]
Code:           [ex: JetBrains Mono (monospace)]
```

### Espaçamento

```
Padrão do Tailwind — usar a escala de 4px:
- Padding de cards: p-6
- Gap entre elementos: gap-4
- Margin entre seções: my-8
```

### Bordas & Sombras

```
Border radius:  [ex: rounded-lg (0.5rem) para cards, rounded-md para inputs]
Sombra padrão:  [ex: shadow-sm para cards, shadow-md para modais]
Border:         [ex: border border-border para separadores]
```

---

## Componentes do Projeto

Componentes customizados ou wrappers criados para este projeto:

### [Nome do Componente]
- **Localização:** `src/components/ui/[nome].tsx`
- **Quando usar:** [ex: Para todas as ações primárias do usuário]
- **Props principais:** [ex: variant, size, loading, disabled]
- **Exemplo:** `<Button variant="primary" size="lg">Salvar</Button>`

<!-- Copie o bloco acima para cada componente relevante -->

---

## Padrões de Layout

### Largura Máxima
- [ex: Container principal: `max-w-7xl mx-auto px-4`]
- [ex: Conteúdo de leitura: `max-w-prose`]
- [ex: Formulários: `max-w-lg`]

### Responsividade
- [ex: Mobile-first — breakpoints: sm(640) md(768) lg(1024) xl(1280)]
- [ex: Menu lateral colapsa em `< md`]
- [ex: Grid de cards: 1 col mobile, 2 cols tablet, 3 cols desktop]

### Padrões de Página
- [ex: Páginas de listagem: Header + Filtros + Tabela/Grid + Paginação]
- [ex: Páginas de formulário: Breadcrumb + Título + Form + Actions]
- [ex: Dashboards: Sidebar + Header + Content area]

---

## Regras de UI/UX

### Feedback ao Usuário
- [ex: Loading states obrigatórios em todo botão de submit]
- [ex: Toast notifications via Sonner para ações de sucesso/erro]
- [ex: Skeleton loaders para conteúdo assíncrono]

### Formulários
- [ex: Validação client-side via react-hook-form + zod]
- [ex: Erros inline abaixo do campo, nunca em alert/modal]
- [ex: Labels sempre visíveis (não usar apenas placeholder)]

### Acessibilidade
- [ex: Todos os inputs com `aria-label` ou `<label>` associado]
- [ex: Contraste mínimo AA (4.5:1 para texto)]
- [ex: Foco visível em todos os elementos interativos]

---

## Ícones

- **Biblioteca:** [ex: Lucide React]
- **Tamanho padrão:** [ex: `size={16}` inline, `size={20}` em botões, `size={24}` standalone]
- **Importação:** [ex: `import { IconName } from 'lucide-react'`]
