def collatz(number):
    if number%2==0:
        number=number//2
        return number
    elif number%2!=0:
        number=number*3+1
        return number

numero=int(input("Digite un numero para usar en la funcion: "))
while numero!=1:
    collatz(numero)
    numero=collatz(numero)
    print (numero)
