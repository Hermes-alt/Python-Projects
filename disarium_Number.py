# un disarium number dont ses chiffres élevé a la 
#puissance de leur position est égal à lui meme 






def is_disarium(num):
    l = [ d for d in str(num) ] 
    s = 0
    for i in range(l): 
        s += int(l[i]) ** (i+1)
    return s == num 
    
n = 135 
if is_disarium(n):
    print(n, " is a disarium number " )
        