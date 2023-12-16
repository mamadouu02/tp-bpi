#!/usr/bin/env python3
"""
On fait une analyse de texte pour dessiner le graphe des mots suivants.
Permet l'utilisation de dictionnaires et une imbrication de structures.
On se sert des donnees pour générer des phrases aléatoires.
"""
import sys
from re import finditer
from random import choice, random
from os import system


def get_mots(nom_fichier):
    """Renvoie un tableau dynamique sur tous les mots du fichier.

    Elimine au passage tout ce qui n'est pas une lettre.
    """
    mots = []
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            for mot in finditer("[a-zA-Z]+", ligne):
                mots.append(mot.group(0))
    return mots


def get_couples(tableau):
    """Renvoie un tableau dynamique des couples.

    Le tableau dynamique renvoyé contient tous les couples d'elements
    successifs du tableau donné.
    """
    couples = []
    valeur_precedente = tableau[0]
    for valeur in tableau[1:]:
        couples.append((valeur_precedente, valeur))
        valeur_precedente = valeur
    return couples


def analyse_texte():
    """Analyse le fichier donné en argument.

    L'analyse parcours les mots du fichier et dessine le graphe
    des mots suivants.

    Ensuite, une phrase aléatoire est générée à partir du dictionnaire
    des mots.
    """

    # Parcours
    if len(sys.argv) != 2:
        print("utilisation :", sys.argv[0], "fichier_texte")
        sys.exit(1)
    suivants = compte_mots_suivants(sys.argv[1])
    genere_graphe(suivants)

    # Génération d'une petite phrase aleatoire.
    mot_depart = choice(list(suivants.keys()))
    phrase = [mot_depart]
    for _ in range(10):
        phrase.append(get_suivant_aleatoire(phrase[-1], suivants))
    print(" ".join(phrase))


def compte_mots_suivants(nom_fichier):
    """Renvoie le dictionnaire des mots suivants.

    Renvoie un dictionnaire associant a chaque mot m1 du fichier
    un dictionnaire associant a chaque mot m2 suivant m1 dans le
    fichier le nombre de fois ou m2 apparait apres m1.
    """
    suivants = {}
    mots = get_mots(nom_fichier)
    couples = get_couples(mots)
    for couple in couples:
        mot, mot_suivant = couple
        if not(mot in suivants):
            suivants[mot] = {mot_suivant : 1}
        elif mot_suivant in suivants[mot]:
            suivants[mot][mot_suivant] += 1
        else:
            suivants[mot][mot_suivant] = 1
    return suivants


def genere_graphe(suivants):
    """Genere le graphe dans les fichiers mots-suivants.dot et .png.

    Attention : il faut analyser des petits textes seulement car le
    layout du graph par l'outil dot peut vite coûter très cher en temps.
    """

    # On créer un fichier au format texte dot, utilisé pour
    # décrire un graphe.
    with open("mots-suivants.dot", "w") as fichier_dot:
        fichier_dot.write('digraph {\n')
        for mot in suivants.keys():
            for mot_suivant, nb_occurences in suivants[mot].items():
                fichier_dot.write(f'{mot} -> {mot_suivant} [label = {nb_occurences}]\n')
        fichier_dot.write('}')

    # On utilise l'outil dot pour convertir le fichier .dot en image
    system("dot -Tpng mots-suivants.dot -o mots-suivants.png")


def get_suivant_aleatoire(mot, suivants):
    """Tire aléatoirement un suivant du mot donné.

    Le tirage aléatoire doit être pondéré par le nombre d'occurrences.
    Si le mot donne n'a pas de suivant, retourne un mot aléatoire.
    """
    if mot in suivants:
        return choice(list(suivants[mot].keys()))
    else:
        return choice(list(suivants.keys()))


if __name__ == "__main__":
    analyse_texte()
