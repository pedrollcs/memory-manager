#!/usr/bin/env python3
"""
Valida a consistência do sistema Multi-Agent Memory.

Uso:
    python validate.py /path/to/project/memory
    python validate.py .                         # se já estiver em /memory

Verificações:
  - Estrutura de diretórios obrigatória existe
  - Todos os arquivos .md em features/ estão listados no index.md
  - Todos os links do index.md apontam para arquivos que existem
  - Arquivos de feature contêm seções obrigatórias (Status, Resumo, Decisões)
  - Nenhum arquivo de memória excede 500 linhas (recomendação de progressive disclosure)
"""

import sys
import re
from pathlib import Path

# Cores ANSI
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

errors = []
warnings = []


def ok(msg):
    print(f"  {GREEN}✓{RESET} {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"  {YELLOW}⚠{RESET} {msg}")


def error(msg):
    errors.append(msg)
    print(f"  {RED}✗{RESET} {msg}")


def check_structure(memory_path: Path):
    """Verifica se a estrutura obrigatória existe."""
    print(f"\n{BOLD}1. Estrutura de diretórios{RESET}")

    required_files = [
        "readme.md",
        "index.md",
        "project/context.md",
        "project/arch.md",
    ]

    optional_files = [
        "project/design.md",
    ]

    for f in required_files:
        path = memory_path / f
        if path.exists():
            ok(f"{f} encontrado")
        else:
            error(f"{f} NÃO encontrado (obrigatório)")

    for f in optional_files:
        path = memory_path / f
        if path.exists():
            ok(f"{f} encontrado")
        else:
            warn(f"{f} não encontrado (recomendado)")

    features_dir = memory_path / "features"
    if features_dir.exists():
        feature_files = list(features_dir.glob("*.md"))
        template_files = [f for f in feature_files if f.name.startswith("_")]
        content_files = [f for f in feature_files if not f.name.startswith("_")]
        ok(f"features/ contém {len(content_files)} feature(s) documentada(s)")
    else:
        warn("features/ não existe — nenhuma feature documentada ainda")


def check_index_consistency(memory_path: Path):
    """Verifica se index.md está consistente com os arquivos reais."""
    print(f"\n{BOLD}2. Consistência do index.md{RESET}")

    index_path = memory_path / "index.md"
    if not index_path.exists():
        error("index.md não existe — impossível validar")
        return

    index_content = index_path.read_text(encoding="utf-8")

    # Remove HTML comments before scanning for links
    clean_content = re.sub(r'<!--.*?-->', '', index_content, flags=re.DOTALL)

    # Extrai todos os links de arquivos do index.md
    link_pattern = re.compile(r'\[`?([^`\]]+)`?\]\(([^)]+)\)')
    linked_files = set()
    for match in link_pattern.finditer(clean_content):
        target = match.group(2)
        if target.endswith(".md") and not target.startswith("http"):
            linked_files.add(target)

    # Verifica se links apontam para arquivos existentes
    for link in sorted(linked_files):
        target_path = memory_path / link
        if target_path.exists():
            ok(f"Link → {link} (arquivo existe)")
        else:
            error(f"Link → {link} (arquivo NÃO encontrado)")

    # Verifica se features existentes estão no index
    features_dir = memory_path / "features"
    if features_dir.exists():
        for feature_file in sorted(features_dir.glob("*.md")):
            if feature_file.name.startswith("_"):
                continue
            relative = f"features/{feature_file.name}"
            if relative in linked_files:
                ok(f"Feature {feature_file.name} está no index")
            else:
                warn(f"Feature {feature_file.name} NÃO está no index.md")


def check_feature_quality(memory_path: Path):
    """Verifica se arquivos de feature contêm seções obrigatórias."""
    print(f"\n{BOLD}3. Qualidade dos arquivos de feature{RESET}")

    features_dir = memory_path / "features"
    if not features_dir.exists():
        warn("Nenhuma feature para validar")
        return

    required_sections = ["Status", "Resumo", "Decisões Técnicas"]
    recommended_sections = ["Regras para o Próximo Agente", "Changelog"]

    for feature_file in sorted(features_dir.glob("*.md")):
        if feature_file.name.startswith("_"):
            continue

        content = feature_file.read_text(encoding="utf-8")
        print(f"\n  {BOLD}{feature_file.name}{RESET}")

        for section in required_sections:
            if section.lower() in content.lower() or f"## {section}" in content:
                ok(f"Contém '{section}'")
            else:
                warn(f"Falta seção '{section}' (recomendada)")

        for section in recommended_sections:
            if section.lower() in content.lower() or f"## {section}" in content:
                ok(f"Contém '{section}'")
            else:
                warn(f"Falta seção '{section}' (desejável)")


def check_file_sizes(memory_path: Path):
    """Verifica se arquivos não excedem o limite recomendado."""
    print(f"\n{BOLD}4. Tamanho dos arquivos{RESET}")

    max_lines = 500
    for md_file in sorted(memory_path.rglob("*.md")):
        line_count = len(md_file.read_text(encoding="utf-8").splitlines())
        relative = md_file.relative_to(memory_path)
        if line_count > max_lines:
            warn(f"{relative}: {line_count} linhas (recomendado <{max_lines})")
        elif line_count > max_lines * 0.8:
            warn(f"{relative}: {line_count} linhas (aproximando do limite de {max_lines})")
        else:
            ok(f"{relative}: {line_count} linhas")


def check_security(memory_path: Path):
    """Verifica se não há secrets ou credenciais nos arquivos de memória."""
    print(f"\n{BOLD}5. Segurança{RESET}")

    suspicious_patterns = [
        (r'(?:password|senha|secret|token|api[_-]?key)\s*[:=]\s*["\']?\S+', "possível credencial"),
        (r'sk-[a-zA-Z0-9]{20,}', "possível API key OpenAI"),
        (r'xox[bprs]-[a-zA-Z0-9-]+', "possível token Slack"),
        (r'ghp_[a-zA-Z0-9]{36}', "possível token GitHub"),
    ]

    found_issues = False
    for md_file in memory_path.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        relative = md_file.relative_to(memory_path)
        for pattern, desc in suspicious_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                error(f"{relative}: {desc} detectada")
                found_issues = True

    if not found_issues:
        ok("Nenhuma credencial ou secret detectada")


def main():
    if len(sys.argv) < 2:
        print("Uso: python validate.py <caminho-para-/memory>")
        sys.exit(1)

    memory_path = Path(sys.argv[1]).resolve()

    # Se apontou para o projeto, ajusta para /memory
    if (memory_path / "memory").exists() and not (memory_path / "index.md").exists():
        memory_path = memory_path / "memory"

    if not memory_path.exists():
        print(f"❌ Caminho não encontrado: {memory_path}")
        sys.exit(1)

    print(f"{BOLD}Multi-Agent Memory — Validação{RESET}")
    print(f"Diretório: {memory_path}")

    check_structure(memory_path)
    check_index_consistency(memory_path)
    check_feature_quality(memory_path)
    check_file_sizes(memory_path)
    check_security(memory_path)

    # Sumário
    print(f"\n{'='*50}")
    if errors:
        print(f"{RED}{BOLD}✗ {len(errors)} erro(s){RESET}")
    if warnings:
        print(f"{YELLOW}{BOLD}⚠ {len(warnings)} aviso(s){RESET}")
    if not errors and not warnings:
        print(f"{GREEN}{BOLD}✓ Memória 100% consistente!{RESET}")
    elif not errors:
        print(f"{GREEN}{BOLD}✓ Nenhum erro crítico{RESET}")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
