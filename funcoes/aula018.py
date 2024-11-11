# isinstance = para saber se o objeto é de determinado tipo

minha_lista = [
    42,                     # int
    3.14,                   # float
    "Hello, World!",        # str
    True,                   # bool
    [1, 2, 3],              # list
    (4, 5, 6),              # tuple
    {"chave": "valor"},     # dict
    {1, 2, 3},              # set
    None,                   # NoneType
    bytes([50, 100, 76])    # bytes
]

for item in minha_lista:
    if isinstance(item, str):
        print(item.upper())    

    if isinstance(item, (int, float)):
        print(item * 2)

    if isinstance(item, bool):
        print(item == False)
