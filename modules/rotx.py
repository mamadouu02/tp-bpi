"""Module d'encodage/décodage par rotation"""


def rot(decalage, lettre):
    """Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractères de taille 1 ;
       - lettre est un soit une lettre majuscule
         soit une lettre minuscule.
    """

    ord_lettre = ord(lettre)

    if len(lettre) != 1:
        return None

    if ord_lettre in range(97, 123):
        ord_lettre = (ord_lettre + decalage - 97) % 26 + 97
        return(chr(ord_lettre))
    elif ord_lettre in range(65, 91):
        ord_lettre = (ord_lettre + decalage - 65) % 26 + 65
        return(chr(ord_lettre))
    else:
        return None


def rot13(lettre):
    """Encode la lettre donnée par rotation de 13 caractères
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
    return(rot(13, lettre))
