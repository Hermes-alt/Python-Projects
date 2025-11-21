""" un spy_Numbers est un nombre dont le produit de ses chiffres sont = à la somme dezs chiffres """
from math import *

def spy_Numbers(num):
    liste = [ int(d) for d in str(num) ]
    if sum(liste) == prod(liste) :
        return True

n = 200
for i in range(1,n+1):
    if spy_Numbers(i):
        print(i, end=" ")