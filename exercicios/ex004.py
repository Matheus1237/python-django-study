def ordenar_lista(lista):
    lista_ordenada = []

    while lista:
        menor = lista[0]  # Assume que o primeiro elemento é o menor

        for num in lista:
            if num < menor:
                menor = num  # Atualiza o menor número encontrado
        
        lista_ordenada.append(menor)  # Adiciona o menor à lista ordenada
        lista.remove(menor)  # Remove o menor da lista original

    return lista_ordenada

lista1 = ordenar_lista([2, 6, 1, 3, 9, 7, 4, 0])
print(lista1)
