#!/usr/bin/env python3

"""Listes simplement chainees + quelques operations"""

import traceur


class Cellule:
    """Une cellule d'une liste."""

    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

    def __str__(self):
        return f"[{self.valeur}|·]"


class ListeSimplementChainee:
    """Une liste simplement chainee."""

    def __init__(self):
        self.tete = None
        self.queue = self.tete
        self.taille = 0

    def __str__(self):
        return " --> ".join(map(str, recupere_cellules(self)))


def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute une cellule en tete."""
    if liste_chainee.taille: # if liste_chainee.taille != 0
        liste_chainee.tete, liste_chainee.tete.suivant = Cellule(valeur), liste_chainee.tete
    else:
        liste_chainee.tete = Cellule(valeur)
        liste_chainee.queue = liste_chainee.tete
    liste_chainee.taille += 1


def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute une cellule en queue."""
    if liste_chainee.taille:
        liste_chainee.queue, liste_chainee.queue.suivant = Cellule(valeur), liste_chainee.queue
    else:
        liste_chainee.queue = Cellule(valeur)
        liste_chainee.tete = liste_chainee.queue
    liste_chainee.taille += 1


def recupere_cellules(liste_chainee):
    """Renvoie un vecteur contenant toutes les cellules de la liste_chainee"""
    if liste_chainee.taille:
        cellules = [liste_chainee.tete]
        while cellules[-1].suivant is not None:
            cellules.append(cellules[-1].suivant)
        return cellules
    return []


def recherche(liste_chainee, valeur):
    """Recherche une valeur dans la liste_chainee donnée.

    Renvoie la premiere cellule contenant la valeur donnée ou
    None si la valeur n'est pas trouvée dans la liste_chainee.
    """
    for cellule in recupere_cellules(liste_chainee):
        if cellule.valeur == valeur:
            return cellule


def supprime(liste_chainee, valeur):
    """Enleve la premiere cellule contenant la valeur donnée."""
    if liste_chainee.taille:
        cellule = liste_chainee.tete
        if cellule.valeur == valeur:
            if cellule.suivant is None:
                liste_chainee = ListeSimplementChainee()
            else:
                liste_chainee.tete = cellule.suivant
            liste_chainee.taille -= 1
        else:
            while cellule.suivant is not None:
                if cellule.suivant.valeur == valeur:
                    cellule.suivant = cellule.suivant.suivant
                    if cellule.suivant is None:
                        liste_chainee.queue = cellule
                    liste_chainee.taille -= 1
                    break
                cellule = cellule.suivant

def test_listes():
    """On teste les operations de base, dans differentes configurations."""
    liste_chainee = ListeSimplementChainee()
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_0"
    )
    ajoute_en_tete(liste_chainee, 3)
    ajoute_en_tete(liste_chainee, 5)
    ajoute_en_tete(liste_chainee, 2)
    ajoute_en_tete(liste_chainee, 4)
    print("liste_chainee : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_1"
    )
    print("recherche : ", recherche(liste_chainee, 3).valeur)
    supprime(liste_chainee, 5)
    print("apres suppression de 5 : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_2"
    )
    supprime(liste_chainee, 4)
    print("apres suppression de 4 : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_3"
    )


if __name__ == "__main__":
    test_listes()
