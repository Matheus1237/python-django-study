def zipper(list1, list2):

    lista_completa = []

    for n in range(min(len(list1), len(list2))):

        cidade = list1[n]
        estado = list2[n]
        
        lista_completa.append((cidade, estado))

    print(lista_completa)


zipper(['Salvador', 'Ubatuba', 'Belo Horizonte'], ['BA', 'SP', 'MG', 'RJ'])

# zip faz isso sem precisar dessa função - usa a lista menor

# zip_longest também, mas usa a lista maior, se nao tiver valor, retorna None