def main():
    matriz=[4,8,75,9,45]

    print (matriz)

    print("Maximo de matriz es: ",max(matriz))
    print("Minimo de matriz es: ",min(matriz))
    print("Primeros 3 numeros: ",matriz[0:3])
    print("Matriz en orden ascendente: ",matriz.sort(),matriz)
    print("Matriz en orden descendente: ",matriz.reverse(),matriz)
    print("Largo de matriz: ",len(matriz))
main()
