#!/usr/bin/env python3

from collections import namedtuple

Point = namedtuple("Point", "x, y")
Triangle = namedtuple("Triangle", "p1, p2, p3")

def affiche_triangle(triangle):
    """ Affiche les trois points de triangle sur la sortie standard """
    print(triangle[0], triangle[1], triangle[2])

p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
t = Triangle(p1, p2, p3)

affiche_triangle(t)
