def max3(num1,num2,num3):
    if(num1==num2 or num2==num3 or num1==num3):
        print("Hay dos o mas numeros repetidos.")
    elif (num1>num2 and num1>num3):
        print(num1)
    elif (num2>num1 and num2>num3):
        print(num2)
    else:
        print(num3)
num1=int(input("Digite el valor del primer numero: "))
num2=int(input("Digite el valor del segundo numero: "))
num3=int(input("Digite el valor del tercer numero: "))
max3(num1,num2,num3)
