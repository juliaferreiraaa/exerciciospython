# Exercícios Sessão 16
'''
#1
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def mostra_cliente(self):
        print(f'o cliente é {self.nome}')

cc = Pessoa('julia','27 anos','1,57')
print(cc.__dict__)
'''

#2
