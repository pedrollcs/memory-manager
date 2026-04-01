#!/usr/bin/env python3
"""
Regenera o index.md a partir dos arquivos existentes em /memory.

Uso:
    python regen_index.py /path/to/project/memory

Lê todos os arquivos .md em features/ e project/, extrai título e status,
e gera um index.md atualizado. Faz backup do index.md anterior.
"""

import sys
import re
import shutil
from pathlib import Path
from datetime import date


def extract_metadata(filepath: Path) -> dict:
    """Extrai título, status e primeira linha de descrição de um arquivo .md."""
    content = filepath.read_text(encoding="utf-8")
    lines = content.splitlines()

    title = filepath.stem.replace("-", " ").replace("_", " ").title()
    status = "❓"
    summary = ""

    for line in lines:
        stripped = line.strip()
        # Título: primeiro H1
        if stripped.startswith("# ") and not stripped.startswith("##"):
            title = stripped.lstrip("# ").strip()
            continue
        # Status
        status_match = re.search(
            r'\*\*Status:\*\*\s*(📋|🔨|🔄|✅|⏸️)\s*(.*)', stripped
        )
        if status_match:
            status = status_match.group(1).strip()
            continue
        # Resumo: primeira linha do blockquote
        if stripped.startswith(">") and not summary:
            summary = stripped.lstrip("> ").strip()
            continue

    return {"title": title, "status": status, "summary": summary}


def main():
    if len(sys.argv) < 2:
        print("Uso: python regen_index.py <caminho-para-/memory>")
        sys.exit(1)

    memory_path = Path(sys.argv[1]).resolve()
    if (memory_path / "memory").exists() and not (memory_path / "index.md").exists():
        memory_path = memory_path / "memory"

    if not memory_path.exists():
        print(f"❌ Caminho não encontrado: {memory_path}")
        sys.exit(1)

    index_path = memory_path / "index.md"

    # Backup do index anterior
    if index_path.exists():
        backup = memory_path / "index.md.bak"
        shutil.copy2(index_path, backup)
        print(f"📦 Backup salvo em: index.md.bak")

    # Gera conteúdo
    lines = []
    lines.append("# 📋 Índice de Memórias\n")
    lines.append("> **Para agentes de IA:** Leia este arquivo PRIMEIRO. Identifique quais memórias são relevantes")
    lines.append("> para sua tarefa atual e carregue apenas essas. Não leia todos os arquivos — otimize tokens.\n")
    lines.append(f"**Última atualização:** {date.today().isoformat()}  ")
    lines.append(f"**Atualizado por:** script regen_index.py\n")
    lines.append("---\n")

    # Projeto
    lines.append("## Projeto (Contexto Estrutural)\n")
    lines.append("Memórias que raramente mudam. Leia na primeira interação com o projeto.\n")
    lines.append("| Arquivo | Descrição | Quando carregar |")
    lines.append("|---|---|---|")

    project_dir = memory_path / "project"
    project_descriptions = {
        "context.md": ("Visão macro do negócio, stack tecnológica e convenções gerais", "Primeira interação ou dúvida sobre o projeto"),
        "arch.md": ("Arquitetura do sistema, estrutura de pastas, infra e deploy", "Tarefas que envolvem criar arquivos, módulos ou alterar infra"),
        "design.md": ("Design System: tokens, componentes, regras de UI/UX", "Tarefas de frontend ou criação de interfaces"),
    }

    if project_dir.exists():
        for f in sorted(project_dir.glob("*.md")):
            desc, when = project_descriptions.get(
                f.name, ("—", "—")
            )
            lines.append(f"| [`project/{f.name}`](project/{f.name}) | {desc} | {when} |")

    lines.append("\n---\n")

    # Features
    lines.append("## Features (Contexto por Funcionalidade)\n")
    lines.append("Memórias granulares. Carregue apenas as features relacionadas à sua tarefa.\n")
    lines.append("| Arquivo | Feature | Status | Resumo |")
    lines.append("|---|---|---|---|")

    features_dir = memory_path / "features"
    if features_dir.exists():
        for f in sorted(features_dir.glob("*.md")):
            if f.name.startswith("_"):
                continue
            meta = extract_metadata(f)
            lines.append(
                f"| [`features/{f.name}`](features/{f.name}) | {meta['title']} | {meta['status']} | {meta['summary']} |"
            )

    lines.append("")
    lines.append("<!-- ")
    lines.append("TEMPLATE PARA NOVAS ENTRADAS:")
    lines.append("| [`features/nome-da-feature.md`](features/nome-da-feature.md) | Nome da Feature | 🔨/✅/⏸️ | Resumo em uma linha |")
    lines.append("")
    lines.append("LEGENDA DE STATUS:")
    lines.append("✅ Concluída — implementada e estável")
    lines.append("🔨 Em progresso — sendo desenvolvida ativamente  ")
    lines.append("⏸️ Pausada — iniciada mas parada temporariamente")
    lines.append("📋 Planejada — documentada mas não iniciada")
    lines.append("🔄 Em revisão — implementada, aguardando review")
    lines.append("-->")

    # Escreve
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"✅ index.md regenerado com sucesso em: {index_path}")


if __name__ == "__main__":
    main()
