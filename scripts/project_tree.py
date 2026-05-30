#!/usr/bin/env python3
import os
import re

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".cache",
    "temp",
    "lfs",
}

def generate_tree(start_path=".", prefix=""):
    """Gera a árvore de diretórios limpa."""
    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        return []

    entries = [e for e in entries if e not in IGNORE_DIRS]

    lines = []
    entries_count = len(entries)

    for index, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        connector = "└── " if index == entries_count - 1 else "├── "
        line = prefix + connector + entry
        lines.append(line)

        if os.path.isdir(path):
            extension = "    " if index == entries_count - 1 else "│   "
            lines.extend(generate_tree(path, prefix + extension))

    return lines


def update_readme(tree_lines, readme_path="README.md"):
    """Atualiza o README entre <!-- tree_start --> e <!-- tree_end -->."""
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    tree_block = "\n".join(tree_lines)

    new_tree_section = (
        "<details>\n"
        "  <summary><strong>📂 Ver árvore do projeto</strong></summary>\n\n"
        "  <br/>\n\n"
        "```text\n"
        f"{tree_block}\n"
        "```\n\n"
        "</details>"
    )

    new_content = re.sub(
        r"<!-- tree_start -->(.*?)<!-- tree_end -->",
        f"<!-- tree_start -->\n{new_tree_section}\n<!-- tree_end -->",
        content,
        flags=re.DOTALL
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✔ README.md atualizado com a nova árvore limpa e colapsável!")


if __name__ == "__main__":
    print("📁 Gerando árvore limpa…")
    tree = generate_tree(".")
    update_readme(tree)
    print("✅ Processo concluído!")