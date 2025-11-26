Ici on compte le pair de 1 du nombre en binaire 



def evil_Odious(num):
    count_bin1= bin(num).count("1")
    return "Evil" if count_bin1 % 2 == 0 else " Odious"
    
    
    
n = 15
print(evil_Odious(n)) #retourne evil 