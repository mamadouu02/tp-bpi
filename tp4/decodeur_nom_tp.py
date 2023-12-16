#!/usr/bin/env python3

"""Programme pour tester le module rotx."""

from rotx import *

def main():
    nom_fichier = input("Saisir un nom de fichier : ")
    fichier = open(nom_fichier + ".txt", "w")
    for lettre in nom_fichier:
        fichier.write(rot13(lettre))
    fichier.close()
    prenom = input("Saisir votre prénom : ")
    prenom_encode = ""
    for lettre in prenom:
        prenom_encode += rot13(lettre)
    print(prenom_encode)

main()