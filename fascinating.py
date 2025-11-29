""" Un nombre est fascinant si, quand on écrit :
ce nombre
ce nombre × 2
ce nombre × 3
et qu’on colle tout ensemble,
on obtient tous les chiffres de 1 à 9 exactement une seule fois. """

def is_fascing(num):
    resultat = str(num) + str(num*2) + str(num*3)
    return "-".join(sorted(resultat)) == "1-2-3-4-5-6-7-8-9"

n = 192
if is_fascing(n) :
    print(n, "is fascing number")
else :
    print(n, "is not fascing Number")