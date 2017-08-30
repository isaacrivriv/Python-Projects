lim=int(input("Digite hasta donde llegara la serie"))
y=0
x=1
print (x,end=" ")
for i in range(0,lim):
    z=y+x
    y=x
    x=z
    print(z,end=" ")
