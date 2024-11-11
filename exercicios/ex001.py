def classificar_numeros(lista_int):

    negativos = 0
    positivos = 0
    zeros = 0

    for numero in lista_int:
        
        if numero < 0:
            negativos += 1
        elif numero > 0:
            positivos += 1
        else:
            zeros += 1

    print(negativos, positivos, zeros)


classificar_numeros([2, 5, -2, 0, 0, -4, 1, -8, -6])
