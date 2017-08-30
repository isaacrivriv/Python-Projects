import random
rando=random.randrange(1,101)
n=0
while(True):
    n+=1
    num=int(input("Digite su numero de 1 a 100: "))
    if num==rando:
        print("Felicidades ha ganado! \nNumero de intentos %d" %(n))
        break
    elif num>rando:
        print("Intente con uno menor")
    else:
        print("Intente con uno mayor")
    
