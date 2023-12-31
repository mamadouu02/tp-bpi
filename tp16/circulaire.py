#!/usr/bin/env python3

"""Listes simplement chaînées, triées, circulaires et avec sentinelle."""

import traceur


class Cellule:
    """Implémentation de la classe Cellule."""

    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

    def __str__(self):
        return f"[{self.valeur}|·]"


class ListeSimplementChaineeTriee:
    """Listes simplement chaînées, triées, circulaires et avec sentinelle."""

    def __init__(self, valeur_sentinelle, nombres=None):
        """Construit la liste avec le range de nombres donné.

        `valeur_sentinelle` precise la valeur de la cellule sentinelle.
        pre-condition: le range de nombres donné est trié si il est
                       différent de None.
        Si le range est différent de None, on créera directement les cellules
        ici dans le constructeur. Autrement dit, on n'utilisera pas la fonction
        ajoute.
        """
        self.tete = Cellule(valeur_sentinelle)
        cellule = self.tete
        if nombres is not None:
            for nombre in nombres:
                cellule.suivant = Cellule(nombre)
                cellule = cellule.suivant
        cellule.suivant = self.tete


    def __str__(self):
        """Renvoie la chaîne de caractères "val1 --> val2 --> val3 ..." """
        
        def generator(self):
            cellule = self.tete
            while cellule.suivant != self.tete:
                yield cellule.suivant
                cellule = cellule.suivant

        return " --> ".join(map(str, generator(self)))




def ajoute(liste_chainee, valeur):
    """Ajoute la valeur donnée à la bonne place dans la liste chaînée.

    pre-condition : `valeur` n'est pas la valeur de la sentinelle.
    """
    cellule = liste_chainee.tete
    while valeur > cellule.suivant.valeur:
        cellule = cellule.suivant
    cellule.suivant = Cellule(valeur, cellule.suivant)


def supprime(liste_chainee, valeur):
    """Supprime la première cellule de la liste chaînée avec la valeur donnée.

    pre-condition : `valeur` n'est pas la valeur de la sentinelle.
    """
    cellule = liste_chainee.tete
    while cellule.suivant != liste_chainee.tete:
        if cellule.suivant.valeur == valeur:
            cellule.suivant = cellule.suivant.suivant
            break
        cellule = cellule.suivant


def decoupe(liste_chainee):
    """Découpe la liste chaînée en deux, une cellule sur 2.

    Par exemple (1,2,3,4,5) produit (1,3,5) et (2,4).
    Renvoie les deux nouvelles listes.
    Aucune nouvelle cellule n'est créée hormis les sentinelles
    des deux nouvelles listes.
    En sortie `liste_chainee` est vide.
    """
    liste_chainee_1 = ListeSimplementChaineeTriee(float("inf"))
    liste_chainee_2 = ListeSimplementChaineeTriee(float("inf"))

    index = 0
    cellule = liste_chainee.tete
    while cellule.suivant != liste_chainee.tete:
        index += 1
        valeur = cellule.suivant.valeur
        if index % 2:
            ajoute(liste_chainee_1, valeur)
        else:
            ajoute(liste_chainee_2, valeur)
        supprime(liste_chainee, valeur)

    return liste_chainee_1, liste_chainee_2


def test():
    """Tests simples des différentes fonctions (à compléter)"""

    # On crée une liste simplement chaînée triée circulaire et l'on affiche
    liste_chainee = ListeSimplementChaineeTriee(float("inf"), range(1, 6))
    print("liste_chainee :", liste_chainee)

    # On ajoute et on supprime puis on affiche
    ajoute(liste_chainee, 0)
    ajoute(liste_chainee, 7)
    ajoute(liste_chainee, 6)
    ajoute(liste_chainee, 5)
    supprime(liste_chainee, 5)
    ajoute(liste_chainee, 8)
    supprime(liste_chainee, 8)
    print("liste_chainee :", liste_chainee)

    # On trace notre liste
    liste_chainee_variable = traceur.Variable("liste_chainee", liste_chainee)
    traceur.display_vars(
        liste_chainee_variable, visualize=False, image_name="liste_chainee_0_a_7"
    )

    # On découpe notre liste
    resultat_decoupe = decoupe(liste_chainee)
    pairs, impairs = resultat_decoupe  # ce qu'on fait ici s'appelle du unpacking

    # On trace le résultat de la découpe
    resultat_decoupe_variable = traceur.Variable("res_decoupe", resultat_decoupe)
    traceur.display_vars(
        resultat_decoupe_variable, visualize=False, image_name="resultat_decoupe"
    )

    # On affiche
    print("pairs   :", pairs)
    print("impairs :", impairs)
    print("liste_chainee :", liste_chainee)

    # On refait quelques suppressions et ajouts pour le plaisir
    # puis on affiche
    supprime(pairs, 4)
    supprime(pairs, 0)
    supprime(pairs, 2)
    supprime(pairs, 6)
    ajoute(impairs, 6)
    ajoute(impairs, 0)
    print("impairs après ajout de 6 et 0 :", impairs)
    print("pairs après suppression de tous les éléments :", pairs)


if __name__ == "__main__":
    test()
