#!/usr/bin/env python3

"""Plateau"""

import sys
import svg

def genere_case(position, taille, numero):
    """Génère une case"""
    print(svg.genere_rectangle(position, taille, taille))
    print(svg.genere_texte(position.x + 5, position.y + taille - 5, numero, 10))

def pas_direction(i, taille, nb_colonnes):
    """Renvoie le pas et le nombre d'itérations pour la génération de cases"""
    if i%2 == 1:
        dx = 0
        dy = taille
        iterations = 1
    else:
        dy = 0
        iterations = nb_colonnes
        if i%4 == 0:
            dx = taille
        else:
            dx = -taille
    return dx, dy, iterations

def genere_cases_plateau(largeur, hauteur):
    """Génère les cases du plateau"""
    numero = 1
    taille = 40
    nb_colonnes = largeur//taille
    nb_lignes = hauteur//taille
    x = 0
    y = hauteur

    for i in range(nb_lignes):
        dx, dy, iterations = pas_direction(i, taille, nb_colonnes)
        if dx != 0:
            x -= dx
            y -= taille
        for _ in range(iterations):
            x += dx
            y -= dy
            genere_case(svg.Point(x, y), taille, numero)
            numero += 1

def main():
    """Génère un plateau de jeu SVG"""
    if len(sys.argv) != 3:
        print("utilisation:", sys.argv[0], "largeur hauteur > plateau.svg")
        sys.exit(1)
    
    largeur, hauteur = int(sys.argv[1]), int(sys.argv[2])
    print(svg.genere_balise_debut_image(largeur, hauteur))
    print(svg.genere_zone_colorie(0, 0, largeur, hauteur, "white"))
    print(svg.genere_balise_debut_groupe("black", "none", 1))
    genere_cases_plateau(largeur, hauteur)
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())

if __name__ == "__main__":
    main()
