#!/usr/bin/env python3

"""Tout éteint"""

import sys

def conversion(file):
    """Lit et convertit l'état initial du jeu"""
    etat = []
    for line in file:
        ligne = []
        for case in line.rstrip():
            if case == "_":
                ligne.append(0)
            else:
                ligne.append(1)
        etat.append(ligne)
    return etat, len(etat), len(etat[0])

def choix_case():
    """Demande à l'utilisateur de choisir une case"""
    case = input("Choisissez une case à jouer :\n")
    ligne = ord(case[0]) - 65
    colonne = int(case[1]) - 1
    return (ligne, colonne)

def changement_case(case):
    """Change l'état d'une case"""
    return (case + 1) % 2

def changement_etat(etat, H, L, i, j):
    """Change l'état du jeu après le choix d'une case"""
    etat[i][j] = changement_case(etat[i][j])
    for di in (-1, 1):
        if 0 <= i + di < H:
            etat[i+di][j] = changement_case(etat[i+di][j])
    for dj in (-1, 1):
        if 0 <= j + dj < L:
            etat[i][j+dj] = changement_case(etat[i][j+dj])

def interface(etat, H, L):
    """Affiche l'état du jeu et vérifie si la partie est terminée"""
    game = False
    print("")
    print("  " + "+" + "-"*L + "+")
    for i in range(H):
        ligne = chr(i + 65) + " |"
        for case in etat[i]:
            if case == 0:
                ligne += "."
            else:
                ligne += "#"
                game = True
        ligne += "|"
        print(ligne)
    print("  " + "+" + "-"*L + "+")
    print("")
    return game

def main():
    """Jeu lights out"""
    if len(sys.argv) <= 1:
        sys.exit(f"Syntaxe : {sys.argv[0]} file_name")

    file = open(sys.argv[1], "r")
    etat, H, L = conversion(file)
    game = interface(etat, H, L)
    nb_coups = 0
    while game:
        i, j = choix_case()
        changement_etat(etat, H, L, i, j)
        game = interface(etat, H, L)
        nb_coups += 1
    print(f"Félicitations, vous avez résolu le niveau en {nb_coups} coup(s) !")
    file.close()

if __name__ == "__main__":
    main()
    