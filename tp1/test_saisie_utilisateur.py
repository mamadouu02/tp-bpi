#!/usr/bin/env python3

from saisie_utilisateur import demande_chaine, demande_entier

n = demande_entier()
s = demande_chaine()

print(f"L'entier saisi est : {n}.")
print(f"La chaîne de caractère saisie est : {s}.")
