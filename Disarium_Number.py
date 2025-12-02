#un disarium number est un nombte dont ces chiffree elevés a la puissance de leur position est egal au nombre 




def is_disarieum(num):
    l = [d for d in str(num)]
    s = 0 
    for i in range(len(l)):
        s += int(l[i])** (i+1)
    return s == num 
    
    
    
n = 135
if is_disarieum(n):
    print(n, " is disarium number ")