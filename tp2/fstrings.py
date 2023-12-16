#!/usr/bin/env python3

def convertit_point_en_chaine(x, y):
    """Renvoie une chaîne de caractère représentant le point d'abscisse x et d'ordonnée y"""
    return f"({x}, {y})"

print(convertit_point_en_chaine(12.2, 3.3))