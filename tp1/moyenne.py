#!/usr/bin/env python3

"""Illustration de pylint"""


def affiche_moyenne(note_projet, note_exam):
    """Retourne la moyenne des notes du projet et de l'examen."""
    moyenne = (1 * note_projet + 3 * note_exam) / 4
    print(moyenne)


affiche_moyenne(12, 14)
