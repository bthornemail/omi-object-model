#!/usr/bin/env python3
"""Manifest-driven build for omi-object-model."""
import os

CORPUS = "/home/main/omi/omi---imo/declarations"
TARGET = "/home/main/omi/omi-object-model"

def scan_corpus():
    ports = []
    standalone = []
    for entry in sorted(os.listdir(CORPUS)):
        path = os.path.join(CORPUS, entry)
        if os.path.isdir(path):
            ports.append(entry)
        elif entry.endswith('.omilisp') or entry.endswith('.json'):
            standalone.append(entry)
    return ports, standalone

def verify_target_files():
    expected = [
        "README.md", "CHARTER.md", "PRINCIPLES.md", "MANIFEST.md",
        "AUTHORITY-BOUNDARY.md", "GLOSSARY.md", "NOTATION.md",
        "OMI-LISP.md", "OMI-PORT.md", "OMNICRON.md", "OMICRON.md",
        "METATRON.md", "TETRAGRAMMATRON.md", "AGENTS.md",
    ]
    missing = []
    for f in expected:
        if not os.path.exists(os.path.join(TARGET, f)):
            missing.append(f)
    return missing

def main():
    ports, standalone = scan_corpus()
    print(f"Corpus: {len(ports)} port dirs, {len(standalone)} standalone files")
    missing = verify_target_files()
    if missing:
        print(f"MISSING root files: {missing}")
    else:
        print("All expected root files present")
    print("Build complete (pass 1: manifest-driven)")

if __name__ == "__main__":
    main()
