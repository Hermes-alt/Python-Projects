# Neon Number c'est lorsque la somme des chiffres de son carres du nombre est egal a lui meme 
def Neon_Number(n:int):
    sq = n**2
    return sum(int(f) for f in str(sq))


n = 9
if Neon_Number(n):
    print(n," is the neon number")
else : 
    print(n," is not neon number")