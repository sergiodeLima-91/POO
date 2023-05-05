class cliente():
    def __init__(self, nome, idade, sexo, genero_favorito):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.genero = genero_favorito

NomeCliente = str(input('Qual seu nome? > '))
IdadeCliente = int(input('Qual é a sua idade? > '))
SexoCLiente = str(input('Qual é o seu sexo? > '))
GeneroCliente = str(input('Qual seu gênero favorito de filmes? > '))
Cliente = cliente(NomeCliente, IdadeCliente, SexoCLiente, GeneroCliente)
print(Cliente.nome)
print(Cliente.idade)
print(Cliente.sexo)
print(Cliente.genero)        