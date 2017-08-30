lim=int(input("Digite hasta donde llegara la suma"))
y=0
x=0
n=0
for z in range(0,lim):
    x=(1+n)*(-1)**n
    y+=x
    n+=1
print("La suma es de: ",y)
