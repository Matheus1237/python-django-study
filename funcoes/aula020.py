# dir, hasattr e getattr em python

string = 'Matheus'

print(dir(string))
metodo_up = 'upper'

if hasattr(string, metodo_up):
    print('Existe o método upper')
    print(getattr(string, metodo_up)())

# dir retorna uma lista de atributos de um objeto

# hasattr(obj, nome) verifica se o objeto possui um atributo chamado nome
