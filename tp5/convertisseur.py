#!/usr/bin/env python3

"""Conversion d'un fichier de points en un fichier svg"""

import svg

def main():
    print(svg.genere_balise_debut_image(640, 480))
    print(svg.genere_balise_debut_groupe("none", "black", "0"))
    for i in range(1000):
        pt = svg.Point(int(input()), int(input()))
        print(svg.genere_cercle(pt, 1))
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())

main()
