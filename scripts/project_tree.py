#!/usr/bin/env python3
import os

def generate_tree(start_path=".", prefix=""):
    entries = sorted(os.listdir(start_path))
    entries_count = len(entries)

    for index, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        connector = "└── " if index == entries_count - 1 else "├── "

        print(prefix + connector + entry)

        if os.path.isdir(path):
            extension = "    " if index == entries_count - 1 else "│   "
            generate_tree(path, prefix + extension)

if __name__ == "__main__":
    print("📁 Project Tree\n")
    generate_tree(".")