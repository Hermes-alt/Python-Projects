def prime_numbers(n):
    if n < 2 :
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 :
          return False 
    return True

n = 10
for i in range(1,n+1):
  if prime_numbers(i):
    print(i,end=" ")