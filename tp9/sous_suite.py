#!/usr/bin/env python3

"""Sous-suite monotone"""

import sys
from enum import Enum

class Monotonie(Enum):
    """Type énuméré Monotonie"""
    STATIONNAIRE = 0
    CROISSANTE = 1
    DECROISSANTE = -1

def traite_nombre(suite, type_suite, nombre):
    """Traite le nombre donné vis à vis de la suite donnée.

    Renvoie (True, nouveau_type_suite) si suite est toujours
    une suite monotone après ajout de nombre.
    Renvoie (False, nouveau_type_suite) si la suite a changé
    de sens.
    """
    if nombre == int(suite[-1]):
        nouveau_type_suite = Monotonie.STATIONNAIRE
    elif nombre > int(suite[-1]):
        nouveau_type_suite = Monotonie.CROISSANTE
    elif nombre < int(suite[-1]):
        nouveau_type_suite = Monotonie.DECROISSANTE
    else:
        nouveau_type_suite = type_suite
    est_monotone = type_suite.value * nouveau_type_suite.value != -1
    return (est_monotone, nouveau_type_suite)

def main():
    """Renvoie la plus grande sous-suite monotone d'une suite donnée"""
    if len(sys.argv) <= 1:
        sys.exit(f"Syntaxe : {sys.argv[0]} file_name")

    suite = []
    plus_grande_suite = []
    type_suite = Monotonie.STATIONNAIRE
    file = open(sys.argv[1], "r")

    for line in file:
        for nombre in line.split():
            nombre = int(nombre)
            est_monotone, type_suite = traite_nombre(suite, type_suite, nombre)
            if est_monotone:
                suite.append(nombre)
            else:
                suite = [suite[-1], nombre]
            if len(suite) > len(plus_grande_suite):
                plus_grande_suite = suite[:]
    
    print(plus_grande_suite)
    file.close()

if __name__ == "__main__":
    main()
