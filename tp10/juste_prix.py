#!/usr/bin/env python3

"""Juste prix"""

def main():
    """Juste prix"""
    n = eval(input("Saissisez un nombre : "))
    while n != 42:
        if n < 42:
            print("C'est plus !")
            n = eval(input("Saissisez un nombre : "))
        else:
            print("C'est moins !")
            n = eval(input("Saissisez un nombre : "))
    print("Vous avez trouvé !")

if __name__ == "__main__":
    main()
