
# Exercícios Sessão 8
'''
# 1

def dobro(nu):
    print(nu * 2)
dobro(6)



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




#3

def positivo_ou_negativo(a):
    if a > 0:
        print('1')
    elif a < 0:
        print("-1")
    else:
        print("0")

positivo_ou_negativo(-55)

'''

#4

def quadrado_perfeito():
    valor = int(input('Entre com um número, para saber o quadrado perfeito: '))

    raizQ = int(valor ** (1 / 2))

    if ((raizQ ** 2) == valor):
        print('O número {0} é um quadrado perfeito!!!'.format(int(valor)))
    else:
        print('O número {0} não é quadrado perfeito!!!'.format(valor))

quadrado_perfeito()
