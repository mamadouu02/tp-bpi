#!/usr/bin/env python3

"""Pivot"""

import sys

def pivote(tableau, indice_pivot):
    """Partitionne un tableau en 2 autour du pivot"""
    tableau_1 = []
    tableau_2 = []
    pivot = tableau[indice_pivot]
    for i, elem in enumerate(tableau):
        if i == indice_pivot:
            continue
        if elem <= pivot:
            tableau_1.append(elem)
        else:
            tableau_2.append(elem)
    return tableau_1, tableau_2

def pivote_en_place(tableau, indice_pivot):
    """Partitionne en place un tableau en 2 autour du pivot"""
    pivot = tableau[indice_pivot]
    for i, elem in enumerate(tableau):
        if elem <= pivot:
            if i > indice_pivot:
                j = i
                while j > indice_pivot:
                    tableau[j] = tableau[j-1]
                    j -= 1
                tableau[indice_pivot] = elem
                indice_pivot += 1
        else:
            if i < indice_pivot:
                j = indice_pivot
                while j > i:
                    tableau[j] = tableau[j-1]
                    j -= 1
                tableau[i] = pivot
                indice_pivot = i
                
def main():
    """Pivot"""

    if len(sys.argv) != 3:
        sys.exit("utilisation : ./pivot indice_pivot nb_tableaux")

    indice_pivot = int(sys.argv[1])
    nb_tableaux = int(sys.argv[2])
    tableau = [3, 0, 10, 1, 6, 9, 5, 3, 9, 0, 5, 8, 9, 8, 4, 2, 0, 9, 6, 2]

    if nb_tableaux == 2:
        tableau_1, tableau_2 = pivote(tableau, indice_pivot)
        print(tableau_1)
        print(tableau_2)
    elif nb_tableaux == 1:
        pivote_en_place(tableau, indice_pivot)
        print(tableau)

if __name__ == "__main__":
    main()