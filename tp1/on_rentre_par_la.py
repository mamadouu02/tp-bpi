#!/usr/bin/env python3

"""Un programme pour comprendre la notion de point d'entrée en python"""

# START CORRECTION
# En python, l'interpréteur commence par lire la première ligne, en ignorant
# les commentaires. Il va donc commencer par lire la ligne "def fait_un_bidule():"
# ci dessous. Comme cette ligne est une définition, le code n'est pas exécuté
# à ce moment là mais simplement "lu".
# END CORRECTION
def fait_un_bidule():
    """Affiche un message de bienvenue"""
    print("ترحيب  en BPI")


# START CORRECTION
# La première ligne vraiment exécutée est donc la ligne suivante qui
# crée la variable globale message
# END CORRECTION
message = "bienvenue"

# START CORRECTION
# Ici nous avons encore une définition donc rien à éxecuter.
# END CORRECTION
def fait_un_truc():
    """Affiche un message de bienvenue"""
    print(message + " à l'Ensimag")


# START CORRECTION
# Ensuite, l'interpréteur appelle la fonction print. Le message
# associé va donc être affiché sur la sortie standard.
# END CORRECTION
print("on vous souhaite la " + message)

# START CORRECTION
# Ici nous avons encore une définition donc rien à éxecuter.
# END CORRECTION
def fait_un_autre_truc():
    """Affiche un autre message de bienvenue"""
    print(message + "à Grenoble, la plus belle ville du monde")


# START CORRECTION
# Ici nous avons encore une définition donc rien à éxecuter. Le fait que
# la fonction s'appelle main ne change rien. Cette fonction est donc une
# fonction comme les autres. A la différence de langages comme le C, où
# le point d'entrée du programme est identifié par une fonction s'appelant
# toujours main, en python le point d'entrée est toujours la première ligne
# du fichier, quelle qu'elle soit.
# END CORRECTION
def main():
    """LA fonction principale"""
    print("Je suis le MAIN, et j'appelle ... fait_un_autre_truc")
    fait_un_autre_truc()


# START CORRECTION
# Ensuite l'interpréteur affecte une nouvelle valeur à la variable message
# END CORRECTION
message = "welcome"

# START CORRECTION
# L'interpréteur rencontre un appel de fonction, il va donc sauter à la
# première ligne de celle-ci, exécuter les lignes de cette fonction
# jusqu'à l'instruction return, puis se déplacer dans le code "juste après"
# l'appel de fonction. Une fonction ne disposant pas d'instruction return
# se comporte comme la même fonction à laquelle on ajoute en dernière ligne :
# return None
# END CORRECTION
fait_un_bidule()
# START CORRECTION
# On se trouve ici "juste après" l'appel fait_un_bidule()
# La dernière instruction à avoir été exécutée était le retour de fonction (ici,
# return None ajouté implicitement puisque la fonction ne retourne rien).
# END CORRECTION

# START CORRECTION
# Enfin, l'interpréteur rencontre un deuxième appel de fonction, qui est exécuté
# selon le même mécanisme que l'appel de fonction précédent.
# END CORRECTION
fait_un_truc()
