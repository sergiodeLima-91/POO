class Personalidade():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

Pessoa = Personalidade('Sérgio',' dos Santos Lima', '32 anos')
print(f'{Pessoa.nome}', end='')
print(Pessoa.sobrenome)
print(f'Idade: {Pessoa.idade}')

Pessoa2 = Personalidade('Antônio',' Veranês', '26 anos')
print(f'{Pessoa2.nome}', end='')
print(Pessoa2.sobrenome)
print(f'Idade: {Pessoa2.idade}')        
