#!/usr/bin/env python3
"""Extract OMI core from corpus. Pass 1: verify declarations exist."""
import os

TARGET = "/home/main/omi/omi-object-model"

def main():
    decl_dir = os.path.join(TARGET, "declarations")
    if os.path.exists(decl_dir):
        files = sorted(os.listdir(decl_dir))
        print(f"declarations/: {len(files)} files")
        for f in files:
            print(f"  {f}")
    else:
        print("declarations/ directory missing")
    print("Extract complete (pass 1: verify)")

if __name__ == "__main__":
    main()
