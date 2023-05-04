class Nome():
    def __init__(self, nome):
        self.nome = nome
        print(f'{self.nome}', end='')
    def SobreNome(self, sobrenome):
        self.sobrenome = sobrenome
        print(self.sobrenome)
Pessoa = Nome('Sérgio')
Pessoa.SobreNome(' Lima')
print(Pessoa.SobreNome)
