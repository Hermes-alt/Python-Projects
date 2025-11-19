# =============================================================================
# Un nombre est heureux si :

#Tu prends ses chiffres

#Tu fais la somme de leurs carrés

#Tu recommences avec le résultat

#Si tu finis par obtenir 1, alors le nombre est heureux

 # =============================================================================

def is_happyNum(num : int):
    s = set() # ici on cree l'ensemble
    while num != 1 and num not in s : # on verifie si num est different de 1 et qu'il ne se trouve ppqs dans l'ensemble
         s.add(num) # on ajoute num a l'ensemble 
         num = sum(int(d)**2 for d in  str(num))
    return num  == 1 

# une autre fonction plus simple 

def is_happyNum2(n : int):
     s = set() # on cree l'ensemble
     while n != 1 and n not in s : # verifie si n est different de 1 et n'appartient deja pas a s
          s.add(n) # om ajoute a chaque fois le n dans l'ensemble
          t = 0 # on initialise la variable t a 0
          for i in str(n) : # on parcour le n qui est converti en chaine de caractere
               t += int(i)**2 # on met au carre le i converti en entier
          n = t # on attribur a la fin le t a n
     
     return n == 1 # return le resultat si a la fin le n == 1 


n = 50 
for i in range(1,51):
    if is_happyNum2(i) :
         print(i,end=" ")
