import random 
r = 1
while r != 0 :
    n = int(random.randint(1, 100))
    
    compteur = 1
    
    c = int(input("choisis le niveau de jeu \n1:facile \n 2: normal \n 3: difficile \n "))
    if c == 1:
       limite = 10
    elif c == 2 :
        limite = 5
    else :
        limite = 3
    
    
    x = int(input("deviner le nombre :")) 
    while x != n and compteur < limite :
        if x > n :
            x = int(input("un peu plus petit :"))
        elif x < n :
            x = int(input("plus grand :"))
        compteur += 1
       
    if x == n :
      print(f"félicitation, vous avez gagnez en {compteur} essaies")
    else :
        print(f"vous avez perdu en {compteur} essaies")
    r = int(input(" 1 : CONTINUER LE JEU \n 0 : QUITTER "))
        



    
   
    
    
        

