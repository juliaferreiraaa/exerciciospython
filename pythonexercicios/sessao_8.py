# Exercícios Sessão 8
'''
# 1

def dobro(nu):
    print(nu * 2)
dobro(6)
'''


# 2

def data_nascimento():
lista_de_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
                      'outubro', 'novembro', 'dezembro']
dias = list(range(32))
ano = list(range(2001))
if 2000 in ano:
    print(dias[1], '/', lista_de_meses[0], end="")
    print("/", 2000)

data_nascimento()

