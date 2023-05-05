class Nome():
    def __init__(self, nome):
        self.nome = nome
        print(f'{self.nome}', end='')
    def SobreNome(self, sobrenome):
        self.sobrenome = sobrenome
        print(self.sobrenome)
    def Idade(self, idade):
        self.idade = idade
        print(f'Idade: {self.idade} anos')
Pessoa = Nome('Sérgio')
Pessoa.SobreNome(' Lima')
Pessoa.Idade('32')
print(Pessoa.SobreNome)
