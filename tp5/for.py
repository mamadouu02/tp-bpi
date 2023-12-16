#!/usr/bin/env python3

"""Programme affichant les éléments des structures"""

def var_1d(var):
    for element in var:
        print(element)

def var_2d(var):
    for element in var:
        var_1d(element)

def var_3d(var):
    for element in var:
        var_2d(element)

def main():
    var1 = "123"
    var2 = [1, 2, 3]
    var3 = (1, 2, 3)
    var4 = range(1, 4)
    var5 = ["toto", range(3), ["t", "o", "t", "o"]]
    var6 = ([1, 2, 3], [4, 5, 6])
    var7 = [[[1, 2], [3, 4]], [[5, 6]]]
    var_1d(var1)
    var_1d(var2)
    var_1d(var3)
    var_1d(var4)
    var_2d(var5)
    var_2d(var6)
    var_3d(var7)

main()
