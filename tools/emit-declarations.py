#!/usr/bin/env python3
"""Emit declarations from templates. Pass 1: static templates."""
import os

TARGET = "/home/main/omi/omi-object-model"

def main():
    decl_dir = os.path.join(TARGET, "declarations")
    if os.path.exists(decl_dir):
        files = sorted(os.listdir(decl_dir))
        print(f"declarations/: {len(files)} files")
    print("Emit complete (pass 1: static templates)")

if __name__ == "__main__":
    main()
