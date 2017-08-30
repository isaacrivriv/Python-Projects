def invers(lista):
    cont=len(lista)
    indice=-1
    invertida=''
    while cont>0:
        invertida+=lista[indice]
        indice-=1
        cont-=1
    print(invertida)
def palindromo(lista):
    inversa=invers(lista)
    indice=0
    cont=0
    for i in range(len(lista)):
        if (inversa[indice]==lista[indice]):
            indice+=1
            cont+=1
        else:
            print("No es palindromo.")
            break
    if cont==len(lista):
        print ("Es palindromo.")
lista=['o','s','o']
invers(lista)
palindromo(lista)
