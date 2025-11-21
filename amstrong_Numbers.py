""" un ombre est amstrong si le nombre est égale à la somme de ces chiffres élevés a la 
puissance du nombre de chiffres """
def is_Amstrong(n):
    l = [int(d) for d in str(n)]
    power = len(l)
    return n == sum(int(d)**power for d in l )

num = 153
if is_Amstrong(num):
    print(num, "is the Amstrong Numbers")
else:
     print(num, "is'nt  the Amstrong Numbers")