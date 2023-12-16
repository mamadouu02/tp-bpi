#!/usr/bin/env python3

fichier = open("toto.txt", "x")
fichier.write("Première ligne du fichier \n")
print("Seconde ligne du fichier", end="", file=fichier)
fichier.close()
