#!/usr/bin/env python3

"""Un programme qui ne sert à pas grand chose."""

import sys


def teste():
    """Teste les fonctions :
        - `recupere_combinaisons_2`
        - `renverse`
        - `recupere_combinaisons`
        - `recupere_parametres`

    Ces trois fonctions testées seront écrites plus tard, mais c'est
    souvent une bonne chose de commencer par les tests, donc allons-y.
    En plus, écrire ce test vous obligera à réfléchir à l'algorithme
    général à appliquer pour générer les combinaisons, sur des séquences
    simples.

    Les spécifications du travail à réaliser sont données en commentaire
    dans le corps de la fonction ci-dessous.
    Vous devez rajouter une ou plusieurs lignes de code à chaque fois
    qu'il y a un TODO suivi de trois points.
    Pensez à bien enlever ces TODO et ces trois points dès que vous les
    avez implémentés.
    Merci de respecter les spécifications À LA LETTRE pour que la
    correction automatique soit possible.

    Pour rappel, en Python une séquence `seq` est un objet sur lequel on
    peut :
      - utiliser la fonction `len(seq)` pour connaître sa taille. Cette
        opération s'effectue en temps constant ;
      - utiliser une boucle `for` pour parcourir ses éléments ;
      - accéder au ième élément avec `seq[i]` (le premier élément est à
        l'indice `0`).
    """

    print('Résultats calculés dans ma tête pour la séquence "ABCD" et k=2')
    # affiche sur la sortie standard ces combinaisons calculées dans notre
    # tête (c'est à dire pour la séquence "ABCD" et k=2), avec une seule
    # combinaison par ligne, sous forme de chaîne de caractères,
    # par exemple AC
    print('AB','AC','AD','BC','BD','CD',sep='\n')

    print('Résultats calculés par recupere_combinaisons_2("ABCD")')
    # effectue l'appel à recupere_combinaisons_2('ABCD'), puis affiche
    # sur la sortie standard les combinaisons renvoyées par cet appel,
    # avec une seule combinaison par ligne. Une combinaison étant un
    # tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print``, c'est à dire de ne faire aucun
    # formatage. La combinaison AC sera donc affichée de la façon
    # suivante : ('A', 'C')
    combinaisons_2 = recupere_combinaisons_2('ABCD')
    for elem in combinaisons_2:
        print(elem)

    # affiche sur la sortie standard une ligne vide
    print()

    print("Résultat de renverse sur [1, 2, 3]")
    # effectue l'appel à renverse([1, 2, 3]), puis
    # puis affiche sur ce résultat
    print(renverse([1, 2, 3]))

    # affiche sur la sortie standard une ligne vide
    print()

    print("Résultats calculés dans ma tête pour la séquence [0, 1, 2, 3, 4] et k=3")
    # affiche sur la sortie standard ces combinaisons calculées dans notre
    # tête (c'est à dire pour la séquence [0, 1, 2, 3, 4] et k=3), avec
    # une seule combinaison par ligne, sous forme de chaîne de caractères,
    # par exemple 014
    print('012','013','014','023','024','034','123','124','134','234',sep='\n')

    print("Résultats calculés par recupere_combinaisons([0, 1, 2, 3, 4], 3)")
    # effectue l'appel à recupere_combinaisons([0, 1, 2, 3, 4], 3), puis
    # affiche sur la sortie standard les combinaisons renvoyées par cet
    # appel, avec une seule combinaison par ligne. Une combinaison étant
    # un tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print`, c'est à dire de ne faire aucun formatage.
    # La combinaison 014 sera donc affichée de la façon suivante : (0, 1, 4)
    # TODO
    combinaisons = recupere_combinaisons([0, 1, 2, 3, 4], 3)
    for elem in combinaisons:
        print(elem)

    # affiche sur la sortie standard une ligne vide
    print()

    # effectue l'appel recupere_parametres(x) avec x étant premier
    # argument de la ligne de commande puis affiche la séquence et
    # k renvoyés par cet appel.
    # Par exemple pour l'exécution de `python combinaisons.py input.txt`
    # x est `input.txt`
    print(
        "Résultats de recupere_parametres sur le fichier donné "
        "en paramètre sur la ligne de commande"
    )
    filename = sys.argv[1]
    sequence, k = recupere_parametres(filename)
    print(sequence, k, sep='\n')

    # affiche sur la sortie standard une ligne vide
    print()

    print(
        "Résultats calculés par recupere_combinaisons sur "
        "les paramètres dans le fichier"
    )
    # effectue l'appel à recupere_combinaisons en utilisant les paramètres
    # renvoyés par l'appel à recupere_parametres(x), puis affiche sur la
    # sortie standard les combinaisons renvoyées par cet appel, avec une
    # seule combinaison par ligne. Une combinaison étant un tuple, on vous
    # demande pour l'affichage de passer directement ce tuple à la fonction
    # `print`, c'est à dire de ne faire aucun formatage. La combinaison AC
    # sera donc affichée de la façon suivante : ('A', 'C')
    # TODO
    ...


def recupere_parametres(filename):
    """Renvoie un tuple à deux entrées contenant la séquence et
    le paramètre k, DANS CET ORDRE, lus à partir du fichier passé
    en paramètre.

    Spécifications PRÉCISES (pensons aux tests automatiques)
    sur le format du fichier :
       - la première ligne contient le nombre k
       - les lignes suivantes contiennent les éléments de la séquence

    Vous trouverez un fichier `input.txt` dans votre dossier `exam` à
    titre d'exemple.
    """
    file = open(filename, 'r')
    sequence = ''
    for i, line in enumerate(file):
        if i == 0:
            k = int(line[0])
        else:
            sequence = sequence + line.strip()
    return (sequence, k)


def recupere_combinaisons_2(sequence):
    """ "Renvoie toutes les combinaisons de taille 2 de la séquence donnée.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - les combinaisons renvoyées sont représentées par une
         `list` de `tuple`.
    """
    combinaisons_2 = []
    for i in range(len(sequence)):
        elem_1 = sequence[i]
        for j in range(i+1, len(sequence)):
            elem_2 = sequence[j]
            if elem_2 != elem_1:
                combinaisons_2.append((elem_1, elem_2))
    return combinaisons_2


def renverse(sequence):
    """
    Renvoie une nouvelle `list` contenant tous les éléments
    de la séquence donnée en paramètre mais dans l'ordre inverse.
    """
    reverse = []
    for elem in sequence[::-1]:
        reverse.append(elem)
    return reverse


def recupere_combinaisons(sequence, k):
    """
    Renvoie toutes les combinaisons de taille k de la sequence donnée.

    Attention, cette fonction est difficile à implémenter.
    Il est vivement conseillé de réfléchir à un algorithme sur le
    papier avant de se lancer dans le code.
    Vous pouvez utiliser la fonction `renverse` si besoin,
    mais ce n'est pas du tout une obligation.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - les combinaisons renvoyées sont représentées par
         une `list` de `tuple`.
    """
    combinaisons = []
    if k == 0:
        return [()]
    elif k == 1:
        return [(elem) for elem in sequence]
    elif k == 2:
        return recupere_combinaisons_2(sequence)
    else:
        sequence_2 = sequence[:]
        sequence_2 = recupere_combinaisons(sequence_2, k-1)
        for combinaison in sequence_2:
            combinaison = list(combinaison)
            for elem in sequence:
                if not(elem in combinaison):
                    combinaisons.append(tuple(sequence + [elem]))
    return combinaisons



def affiche_nombre_combinaisons():
    """Affiche le nombre de k-combinaisons d'une séquence de taille n.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - l'affichage se fera en fonction de n, la taille de la séquence,
         et du paramètre k
       - les seuls caractères autorisées dans la chaîne affichée sont :
           + `*`, `\` et `-`
           + les lettres `n` et `k`
           + des parenthèses
           + le caractère `!` (factorielle)
    """
    print('n!\(k!(n-k)!)')


# La fonction teste() est appelée uniquement dans
# le cas où le programme est invoqué comme programme
# principal avec `python combinaisons.py input.txt`
# ou avec `./combinaisons.py input.txt`
if __name__ == "__main__":
    teste()
