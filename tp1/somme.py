#!/usr/bin/env python3

def demande_entier():
    """Renvoie l'entier saisi par l'utilisateur."""
    return int(input("Saisir un entier : "))

n, m = demande_entier(), demande_entier()
print(f"La somme des deux entiers saisis vaut {n + m}.")
