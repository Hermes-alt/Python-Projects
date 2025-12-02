# leap Year en french qui veut dire une année bissextile 
# une année est biissextile si elle divisible par 4 ou 400 et non par 100

def Leap_Year(n:int):
    return (n % 4 == 0 and n % 100 != 0) or ( n % 400 == 0)


n = 2024
if Leap_Year(n):
    print(n, " is Leap Year")
else :
    print(n, " Is not leap Year")


