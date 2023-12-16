#!/usr/bin/env python3
"""Un exemple de références vers des fonctions"""


def multiplie_par_deux(un_nombre):
    """Renvoie un_nombre multiplié par deux"""
    return un_nombre * 2


def ajoute_42(un_nombre):
    """Renvoie un_nombre + 42"""
    return un_nombre + 42


def applique_operation(un_nombre, operation):
    return operation(un_nombre)


def main():
    """Test de nos fonctions"""
    entier = 17
    fonc1 = multiplie_par_deux
    fonc2 = ajoute_42
    print(multiplie_par_deux(entier))
    print(fonc1(entier))
    print(applique_operation(entier, multiplie_par_deux))
    print(applique_operation(entier, fonc2))
    print(applique_operation(entier, fonc1(entier)))


if __name__ == "__main__":
    main()
