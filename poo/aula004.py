# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar.')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print('Não pode fotografar enquanto filma.')
            return
        print(f'{self.nome} está fotografando...')



c1 = Camera('Sony')
c1.filmar()
c1.fotografar()
c1.filmar()
c1.parar_filmar()
c1.fotografar()