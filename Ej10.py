import random
def ejercicio(cantidad):
    if cantidad<=100:
        print("Lo sentimos no cualifica para la promocion.")
    else:
        rando=random.randrange(0,5)
        if rando==0:
            print("Aleatoriamente obtuvo la blanca!\n\nLo sentimos no gano un descuento.")
        elif rando==1:
            print("Aleatoriamente obtuvo la roja!\n\nSu descuento es de 10%\n\n Su nuevo total es de: ",cantidad*1.10)
        elif rando==2:
            print("Aleatoriamente obtuvo la azul!\n\nSu descuento es de 20%\n\n Su nuevo total es de: ",cantidad*1.20)
        elif rando==3:
            print("Aleatoriamente obtuvo la verde!\n\nSu descuento es de 30%\n\n Su nuevo total es de: ",cantidad*1.30)
        elif rando==4:
            print("Aleatoriamente obtuvo la amarilla!\n\nSu descuento es de 50%\n\n Su nuevo total es de: ",cantidad*1.50)
cant=float(input("Digite la cantidad del cliente: "))
ejercicio(cant)
