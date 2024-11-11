# try, except, else e finally

try:
    print(8 / 0)

except ZeroDivisionError:
    print('Dividiu por zero')

else:
    print('Não deu erro')

finally:
    print('Executei !!!')

# finally sempre será executado
# Pode ter vários except
# else vai executar se não houver error
