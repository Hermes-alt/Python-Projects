def changeVariable(a,b):
    c=a
    a=b
    b=c
    return a,b
    
    
    
    
    def inverseList(L):
        n=len(L) // 2
        for i in range(n):
            changeVariable(L[i], L[n-1-i])
        return L 
        
        
u=[1,4,8,6]
print(inverseList(u))
