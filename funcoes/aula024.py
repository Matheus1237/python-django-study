# try, except, else e finally

a = 20
b = 0
# d = a / b

try: # Tente isso, se ocorrer um erro...
    a / b
    print('Não serei executada')

except ZeroDivisionError: # Executará isso
    print('Dividiu por zero')


print('CONTINUAR')

# Exception trata qualquer erro

