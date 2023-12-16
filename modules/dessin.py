"""Module pour dessins"""

import random as rd
import svg

def couleur_aleatoire():
    """Génère une couleur aléatoire"""
    return rd.choice(["red", "yellow", "green", "blue"])

def affiche_triangle(triangle, couleur):
    """Affiche un triangle"""
    print(svg.genere_balise_debut_groupe_transp(0.5))
    print(svg.genere_balise_debut_groupe("none", couleur, 1))
    print(svg.genere_polygone(triangle))
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_groupe())
