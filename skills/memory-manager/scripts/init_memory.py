#!/usr/bin/env python3
"""
Inicializa o sistema Multi-Agent Memory em um projeto.

Uso:
    python init_memory.py /path/to/project
    python init_memory.py .                    # projeto atual

Copia os templates para /memory na raiz do projeto e confirma a estrutura.
Se /memory já existir, aborta para não sobrescrever dados existentes.
"""

import sys
import shutil
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("Uso: python init_memory.py <caminho-do-projeto>")
        print("Exemplo: python init_memory.py /home/user/meu-projeto")
        sys.exit(1)

    project_path = Path(sys.argv[1]).resolve()
    memory_path = project_path / "memory"

    if not project_path.exists():
        print(f"❌ Diretório não encontrado: {project_path}")
        sys.exit(1)

    if memory_path.exists():
        print(f"⚠️  /memory já existe em {project_path}")
        print("    Para reinicializar, remova a pasta /memory primeiro.")
        sys.exit(1)

    # Localiza os templates relativos a este script
    script_dir = Path(__file__).parent.parent
    templates_dir = script_dir / "assets" / "templates"

    if not templates_dir.exists():
        print(f"❌ Templates não encontrados em: {templates_dir}")
        sys.exit(1)

    # Copia templates para /memory
    shutil.copytree(templates_dir, memory_path)

    # Lista os arquivos criados
    files_created = sorted(memory_path.rglob("*.md"))

    print(f"✅ Sistema de memória inicializado em: {memory_path}")
    print(f"   {len(files_created)} arquivos criados:")
    for f in files_created:
        rel = f.relative_to(memory_path)
        print(f"   └── {rel}")

    print()
    print("📋 Próximos passos:")
    print("   1. Preencha memory/project/context.md com informações do seu projeto")
    print("   2. Preencha memory/project/arch.md com a arquitetura atual")
    print("   3. Preencha memory/project/design.md se houver Design System")
    print("   4. Remova os arquivos de exemplo em memory/features/ (auth.md, proposals.md)")
    print("   5. Instrua seus agentes a verificar /memory no início de cada sessão")


if __name__ == "__main__":
    main()
