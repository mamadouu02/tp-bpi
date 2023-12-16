#!/usr/bin/env python3

"""Images PGM"""

import random as rd
from collections import namedtuple

Point = namedtuple("Point", "x y")
Disque = namedtuple("Disque", "centre rayon")

def dimensions_image():
    """Demande à l'utilisateur de donner les dimensions de l'image"""
    return eval(input())

def en_tete(largeur, hauteur):
    """Affiche l'en-tête du fichier"""
    print("P2")
    print(largeur, hauteur)
    print("255")

def disque(largeur, hauteur):
    """Tire aléatoirement les coordonnées d'un disque (centre et rayon)
    complétement localisés dans l'image"""
    centre = Point(rd.randint(1, largeur - 1), rd.randint(1, hauteur - 1))
    rayon_max = min([centre.x, centre.y, largeur - centre.x, hauteur - centre.y])
    rayon = rd.choice([1, rayon_max])
    return Disque(centre, rayon)

def distance(point, centre):
    """Renvoie la distance entre point et centre"""
    return (point.x - centre.x)**2 + (point.y - centre.y)**2

def in_disque(point, disque):
    """Vérifie si un point est dans un disque"""
    return distance(point, disque.centre) <= disque.rayon**2

def affiche_pixel(largeur, hauteur, disque1, disque2):
    """Affiche les valeurs des pixels"""
    for i in range(hauteur):
        fin = " "
        for j in range(largeur):
            if j == largeur - 1:
                fin = "\n"
            if in_disque(Point(i, j), disque1) or in_disque(Point(i, j), disque2):
                print(rd.randint(0, 255), end=fin)
            else:
                print(255, end=fin)

def main():
    """Génère un fichier PGM"""
    largeur, hauteur = dimensions_image()
    en_tete(largeur, hauteur)
    disque1 = disque(largeur, hauteur)
    disque2 = disque(largeur, hauteur)
    affiche_pixel(largeur, hauteur, disque1, disque2)

main()
