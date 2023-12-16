#!/usr/bin/env python3

"""Fractales."""

import math
import random as rd
import svg

class Point:
    """Classe Point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __rmul__(self, factor):
        return Point(factor * self.x, factor * self.y)

    def distance(self, other):
        """Distance entre deux points."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def rotation(self, angle):
        """Rotation d'un point."""
        return Point(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle)
            )

    def similitude(self, rapport, angle):
        """Similitude d'un point."""
        return self - rapport * Point(1, 0).rotation(angle)

def genere_branches(initial, taille_max):
    """Générateur de branches."""
    nombre = rd.randint(2, 4)
    for _ in range(nombre):
        taille = rd.uniform(0, taille_max)
        if taille < 5:
            return
        angle = rd.uniform(math.pi/6, 5 * math.pi/6)
        final = initial.similitude(taille, angle)
        print(svg.genere_segment(initial, final))
        genere_branches(final, taille)

def main():
    """Générateur d'arbres en SVG."""
    largeur = 800
    hauteur = 600
    initial = Point(largeur/2, hauteur * 9/10)
    taille = hauteur/4
    angle = math.pi/2
    final = initial.similitude(taille, angle)

    print(svg.genere_balise_debut_image(largeur, hauteur))
    print(svg.genere_zone_colorie(0, 0, largeur, hauteur, "black"))
    print(svg.genere_balise_debut_groupe("white", "none", 1))
    print(svg.genere_segment(initial, final))
    genere_branches(final, taille)
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())

if __name__ == "__main__":
    main()
