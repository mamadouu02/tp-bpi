#!/usr/bin/env python3

"""Operations sur les listes simplement chainees."""

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

    def __init__(self, iterable=()):
        self.taille = len(iterable)
        if self.taille:
            self.tete = Cellule(iterable[0])
            cellule = self.tete
            for valeur in iterable[1:]:
                cellule.suivant = Cellule(valeur)
                cellule = cellule.suivant
            self.queue = cellule
        else:
            self.tete = None
            self.queue = self.tete

    def __str__(self):
        return " --> ".join(map(str, recupere_cellules(self)))


def recupere_cellules(liste_chainee):
    """Renvoie un iterateur sur toutes les cellules de la liste donnee."""
    cellule = liste_chainee.tete
    while cellule is not None:
        yield cellule
        cellule = cellule.suivant


def remplace_valeurs(liste_chainee, transforme):
    """Remplace pour chaque cellule la valeur par la valeur renvoyee par transforme."""
    for cellule in recupere_cellules(liste_chainee):
        cellule.valeur = transforme(cellule.valeur)


def filtre_cellules(liste_chainee, filtre):
    """Renvoie un iterateur sur toutes les cellules de la liste pour lesquelles
    filtre(valeur) renvoie True. Lance une exception si filtre(valeur) ne renvoie pas un booleen."""
    for cellule in recupere_cellules(liste_chainee):
        if not isinstance(filtre(cellule.valeur), bool):
            raise TypeError("filtre doit renvoyer un booleen")
        if filtre(cellule.valeur):
            yield cellule


def supprime_cellules(liste_chainee, filtre):
    """Elimine de liste_chainee toutes les cellules pour lesquelles filtre(valeur) renvoie False."""
    if liste_chainee.taille:
        cellules = filtre_cellules(liste_chainee, filtre)
        liste_chainee.tete = next(cellules)
        liste_chainee.taille = 1
        derniere_cellule = liste_chainee.tete
        for cellule in cellules:
            derniere_cellule.suivant = cellule
            liste_chainee.taille += 1
            derniere_cellule = cellule
        liste_chainee.queue = derniere_cellule


def concatene(liste_chainee_1, liste_chainee_2):
    """Rajoute les cellules de liste_chainee_2 a la fin de liste_chainee_1.
    liste_chainee_2 doit devenir vide.."""
    if liste_chainee_2.taille:
        if liste_chainee_1.taille:
            liste_chainee_1.queue.suivant = liste_chainee_2.tete
        else:
            liste_chainee_1.tete = liste_chainee_2.tete
        liste_chainee_1.queue = liste_chainee_2.queue
        liste_chainee_1.taille += liste_chainee_2.taille
        liste_chainee_2 = ListeSimplementChainee()


def ajoute_en_queue(liste_chainee, cellule):
    """Ajoute une cellule en queue."""
    if liste_chainee.taille:
        liste_chainee.queue.suivant = cellule
        liste_chainee.queue = cellule
    else:
        liste_chainee.queue = cellule
        liste_chainee.tete = liste_chainee.queue
    liste_chainee.taille += 1


def decoupe(liste_chainee, fonction):
    """Cree et retourne deux listes simplement chainees decrites ci-dessous :
    - une liste chainee contient les cellules pour lesquelles la fonction fonction renvoie True
    - la seconde liste chainee contient les autres cellules."""
    liste_chainee_1 = ListeSimplementChainee()
    liste_chainee_2 = ListeSimplementChainee()
    for cellule in recupere_cellules(liste_chainee):
        if fonction(cellule.valeur):
            ajoute_en_queue(liste_chainee_1, cellule)
        else:
            ajoute_en_queue(liste_chainee_2, cellule)
    if liste_chainee_1.taille:
        liste_chainee_1.queue.suivant = None
    if liste_chainee_2.taille:
        liste_chainee_2.queue.suivant = None
    return liste_chainee_1, liste_chainee_2


def incremente(valeur):
    """Incremente la valeur de 1."""
    return valeur + 1


def est_pair(valeur):
    """Renvoie True si la valeur est paire."""
    return valeur % 2 == 0


def test_listes():
    """On teste les operations de base, dans differentes configurations."""

    liste_chainee = ListeSimplementChainee(range(6))
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_0"
    )
    print(liste_chainee)
    print()

    for cellule in recupere_cellules(liste_chainee):
        print(cellule)
    print()

    remplace_valeurs(liste_chainee, incremente)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_1"
    )
    print(liste_chainee)
    print()

    for cellule in filtre_cellules(liste_chainee, est_pair):
        print(cellule)
    print()

    supprime_cellules(liste_chainee, est_pair)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_2"
    )
    print(liste_chainee)
    print()

    concatene(liste_chainee, ListeSimplementChainee([1, 3, 5]))
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_3"
    )
    print(liste_chainee)
    print()

    liste_pairs, liste_impairs = decoupe(liste_chainee, est_pair)

    traceur.display_instance(
        liste_pairs, visualize=False, image_name="liste_chainee_4"
    )
    print(liste_pairs)
    print()

    traceur.display_instance(
        liste_impairs, visualize=False, image_name="liste_chainee_5"
    )
    print(liste_impairs)


if __name__ == "__main__":
    test_listes()
