#!/usr/bin/env python3

import svg

p1 = svg.Point(500, 500)
p2 = svg.Point(400, 450)
p3 = svg.Point(600, 450)
p4 = svg.Point(500, 600)

print(svg.genere_balise_debut_image(1000, 1000))

print(svg.genere_balise_debut_groupe("black", "white", 1))
print(svg.genere_cercle(p1, 250))
print(svg.genere_balise_fin_groupe())

print(svg.genere_balise_debut_groupe("none", "black", 1))
print(svg.genere_cercle(p2, 10))
print(svg.genere_cercle(p3, 10))
print(svg.genere_cercle(p4, 20))
print(svg.genere_balise_fin_groupe())

print(svg.genere_balise_fin_image())
