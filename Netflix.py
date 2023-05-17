class cliente():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def escolherFilmeSerie(self, producao):
        if producao == 1:
            print('The Chosen')
        elif producao == 2:
            print('Deus Não Está Morto 3')
        elif producao == 3:
            print('Five Nights At Freddy')        

NomeCliente = str(input('Qual seu nome? > '))
IdadeCliente = int(input('Qual é a sua idade? > '))
SexoCLiente = str(input('Qual é o seu sexo? > '))
print('1) The Chosen')
print('2) Deus Não Está Morto 3')
print('3) Five Nights At Freddy')
Escolha = int(input('Escolha uma das produções cinetográticas acima pelo número: > '))
Cliente1 = cliente(NomeCliente, IdadeCliente, SexoCLiente)
print(f'Nome: {Cliente1.nome}')
print(f'Idade: {Cliente1.idade}')
print(f'Sexo: {Cliente1.sexo}')
print(f'Produção escolhida: ', end='')
Cliente1.escolherFilmeSerie(Escolha)
        