#!/usr/bin/env python3

"""Lecture de fichier"""

import sys

def main():
    """Ouvre un fichier en lecture et affiche son contenu sur la sortie standard"""
    if len(sys.argv) <= 1:
        sys.exit(f"Utilisation : {sys.argv[0]} file_name")

    file = open(sys.argv[1], 'r')
    for line in file:
        print(line)

if __name__ == "__main__":
    main()
