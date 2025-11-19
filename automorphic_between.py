#un nombre automorphe est un nombre dont son carré se termine par lui même exple de 5
def is_automorphic(num : int):
  return str(num*num).endswith(str(num))


def is_automorphic2(n:int):
  x = str(n)
  squart = str(n*n)
  if squart.endswith(x) is True :
    return x
  


n = 5
for i in range(1,6):
 print(is_automorphic2(i))
 

