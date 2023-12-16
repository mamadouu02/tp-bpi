"""Module pour triangles"""

import random as rd
import numpy as np
import svg

def triangle_aleatoire(largeur_lim, hauteur_lim):
    """Génère aléatoirement un triangle dans la partie de l'écran définie
    par largeur_lim et hauteur_lim"""
    x1 = int(largeur_lim[0])
    x2 = int(largeur_lim[1])
    y1 = int(hauteur_lim[0])
    y2 = int(hauteur_lim[1])
    return [svg.Point(rd.randint(x1, x2), rd.randint(y1, y2)) for _ in range(3)]

def tourne_triangle_autour(triangle, centre, angle):
    """Rotation de triangle"""
    xc, yc = centre
    triangle_tourne = []
    for point in triangle:
        x = point.x
        y = point.y
        x2 = int(xc + (x - xc) * np.cos(angle) - (y - yc) * np.sin(angle))
        y2 = int(yc + (x - xc) * np.sin(angle) + (y - yc) * np.cos(angle))
        triangle_tourne.append(svg.Point(x2, y2))
    return triangle_tourne
