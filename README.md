# 🚀 Zeppelin Skills

> O hub oficial de skills avançadas para agentes de IA da **Zeppelin IA**.

[![Agent Skills Spec](https://img.shields.io/badge/agent--skills-v1.0-blue)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Install with npx](https://img.shields.io/badge/npx-skills%20add-black)](https://skills.sh)

**Zeppelin Skills** é um repositório centralizado de extensões e ferramentas poderosas projetadas para turbinar o fluxo de trabalho de desenvolvedores que utilizam agentes de IA (como **Antigravity**, **Claude Code**, **Cursor**, **Gemini**, entre outros).

Em vez de repositórios isolados, unificamos nossas ferramentas aqui para facilitar a descoberta, instalação e manutenção.

---

## 🛠️ Como Instalar uma Skill

Você pode adicionar qualquer skill deste repositório ao seu agente favorito usando o comando `skills add`.

### Método Recomendado (npx)

```bash
# Adiciona a skill selecionada ao seu ambiente
npx skills add pedrollcs/zeppelin-skills/<nome-da-skill>
```

*(Exemplo: `npx skills add pedrollcs/zeppelin-skills/multi-agent-memory`)*

---

## 📂 Skills Disponíveis

### 1. 🧠 Multi-Agent Memory (MAM)
> **Status:** ✅ Estável | **Local:** `skills/multi-agent-memory`

Resolve o problema da **Amnésia de Contexto** em projetos onde múltiplos agentes trabalham de forma assíncrona. Cria um diretório `/memory` compartilhado que serve como a "fonte da verdade" exclusiva.

*   **Comando CLI:** `mam init`, `mam validate`.
*   **Protocolo:** Check-in / Check-out para persistência de conhecimento.

### 2. 🎨 Design System (Em breve)
> **Status:** 🔨 Em desenvolvimento | **Local:** `skills/design-system`

Componentes e tokens visuais pré-configurados para acelerar a criação de interfaces premium com a estética Zeppelin.

---

## 🏛️ Estrutura do Repositório

Todas as nossas skills seguem a especificação [Agent Skills](https://agentskills.io), garantindo compatibilidade multiplataforma:

```
zeppelin-skills/
├── skills/
│   ├── multi-agent-memory/    # Skill de Gerenciamento de Memória
│   │   ├── SKILL.md           # Definição e Triggers
│   │   ├── scripts/           # Ferramentas de automação
│   │   └── assets/            # Templates e recursos
│   └── (novas-skills)/        # Futuras adições
├── bin/                       # Executáveis globais e utilitários
└── README.md                  # Este guia
```

---

## 🤝 Contribuindo

Para adicionar uma nova skill a este repositório:

1.  Crie uma nova subpasta em `/skills/`.
2.  Implemente o arquivo `SKILL.md` seguindo o padrão YAML.
3.  Inclua os scripts e referências necessários.
4.  Submeta um Pull Request.

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

*Criado para orquestrar conhecimento na era da engenharia de software assistida por IA.*
