#!/usr/bin/env python3

"""Incrémente."""

def incremente(number, increment):
    """Renvoie number + increment."""
    if increment == 0:
        return number
    return incremente(number, increment - 1) + 1

if __name__ == "__main__":
    print(incremente(22, 20))
