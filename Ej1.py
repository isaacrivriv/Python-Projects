print("Digite 3 numeros distintos")
num1=int(input("Digite el primer numero:"))
num2=int(input("Digite el segundo numero:"))
num3=int(input("Digite el tercer numero:"))
if(num1==num2 or num1==num3 or num2==num3):
    print("No es posible calcular el mayor ya que hay al menos dos iguales")
elif(num1>num2 and num1>num3):
    print("El mayor es: ",num1)
elif(num2>num1 and num2>num3):
    print("El mayor es: ",num2)
else:
    print ("El mayor es: ",num3)
