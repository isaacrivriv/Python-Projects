lim=int(input("Digite hasta cuanto llega la suma: "))
z=0
n=1
for i in range (0,lim):
    x=2*n-1
    z+=x
    n+=1
print("El valor hasta el limite es: ",z)
