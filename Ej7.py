lim=int(input("Digite hasta donde desea realizar la suma: "))
x=1
z=0
y=1
while (x<=lim):
    y*=x
    x+=1
    z+=y
print("La suma es de: ",z) 
