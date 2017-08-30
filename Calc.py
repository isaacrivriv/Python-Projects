#Returns the addition of the numbers
def add(num1,num2):
    return num1+num2
#Returns the substraction of the numbers
def subs(num1,num2):
    return num1-num2
#Returns the multiplication of the numbers
def mult(num1,num2):
    return num1*num2;
#Return the divison of the numbers
def div(num1,num2):
    if(num2==0):
        print("Can't divide by 0")
    else:
        print(num1/num2)
def main():
    num1=int(input("Please enter the first number:"))
    num2=int(input("Please enter the second number:"))
    operation=input("What operation would you like to do?(+,-,*,/)")
    if(operation=='+'):
        print(add(num1,num2))
    elif(operation=='-'):
        print(subs(num1,num2))
    elif(operation=='*'):
        print(mult(num1,num2))
    elif(operation=='/'):
        div(num1,num2)
    else:
        print("Invalida input")

def repeat():
    repeat=input("Would you like to restart the program? (Y/N)")
    while(repeat!='Y' and repeat!='N' and repeat!='n' and repeat!='y'):
        repeat=input("Invalid answer! Please try again")
    if(repeat=='Y' or repeat=='y'):
        repetition()
def repetition():    
    main()
    repeat()

repetition()
