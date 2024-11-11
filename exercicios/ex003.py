def soma_digitos(num):

    '''num_lista = str(num)
    total = 0

    for digito in num_lista:

        n_int = int(digito)

        total += n_int
    
    print(total)'''

    total = sum(int(digito) for digito in str(num))
    return total        


num1 = soma_digitos(223)
print(num1)