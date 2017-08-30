def menu():
    numero=int(input("Digite un numero entero"))
    print("\n1. Calcular el cubo del numero \n2. Calcular si es par o impar \n3. Salir")
    opcion=int(input("Digite la opcion que desee correr:"))
    if opcion==1:
        print(numero)
        print("El cubo del numero es: ",numero**3)
    elif opcion==2:
        print(numero)
        calc=numero%2
        if(calc==0):
            print("El numero es par")
        else:
            print("El numero es impar")
    elif opcion!=3:
        print("La opcion no es valida")
        
menu()
