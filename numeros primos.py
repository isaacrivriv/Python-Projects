num=int(input("Digite el numero que desee descomponer a factores primos: "))
x=0
while(True):
    prime=num
    for z in range (2,10):
        if (num%z==0):
            print(z,end=" ")
            num=num-(num%z)
    
    if prime==num:
        break
