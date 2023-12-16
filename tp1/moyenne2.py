#!/usr/bin/env python3

maths = (17, 9)
physique = (15, 6)
histoire_info = (4, 1)

n, m = 0, 0

for matiere in (maths, physique, histoire_info):
    n += matiere[0]*matiere[1]
    m += matiere[1]

moyenne = n/m

print(f"Moyenne : {moyenne}")
