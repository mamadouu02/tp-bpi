#!/usr/bin/env python3

"""Ligne de commandes et arguments"""

import sys

if len(sys.argv) == 1:
    print("Usage : ./affiche_arguments.py arg1 arg2 ... argN")
else:
    for arg in sys.argv[1:]:
        print(arg)