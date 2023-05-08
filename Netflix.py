class cliente():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def escolherFilmeSerie(serie):
        if serie == 1:
            print('The Chosen')
        elif serie == 2:
            print('Deus Não Está Morto 3')
        elif serie == 3:
            print('Five Nights At Freddy')
        else:
            print('Opção inválida! Tente novamente!')    

NomeCliente = str(input('Qual seu nome? > '))
IdadeCliente = int(input('Qual é a sua idade? > '))
SexoCLiente = str(input('Qual é o seu sexo? > '))
Escolha = int(input('Escolha uma das produções cinetográticas abaixo pelo número: > '))
print('1) The Chosen')
print('2) Deus Não Está Morto 3')
print('3) Five Nights At Freddy')
Cliente = cliente(NomeCliente, IdadeCliente, SexoCLiente)
cliente.escolherFilmeSerie(serie=Escolha)
print(f'Nome: {Cliente.nome}')
print(f'Idade: {Cliente.idade}')
print(f'Sexo: {Cliente.sexo}')
print(cliente.escolherFilmeSerie)

        