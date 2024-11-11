def soma_lista(list1, list2):

    lista_completa = []

    for n in range(min(len(list1), len(list2))):

        lista1 = list1[n]
        lista2 = list2[n]

        soma = lista1 + lista2

        lista_completa.append(soma)

    print(lista_completa)


lista_a = [1, 2, 5, 3, 7]
lista_b = [3, 4, 2, 7, 9, 4, 3, 1]

soma_lista(lista_a, lista_b)
