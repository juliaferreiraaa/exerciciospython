# Exercícios Sessão 13
'''
#1
with open('arq.txt','w') as arquivo:
    while True:
        escreva= input('escreva ou digite 0 para sair: ')
        if escreva != '0':
            arquivo.write('escreva')
        else:
            break


#2

import rlcompleter
batata = open('arq.txt')
sacolao = batata.readlines()
print(sacolao)
'''


#3



def acharVogal():
    arquivo = open('arq.txt')
    for letra in arquivo == 'a', 'e', 'i', 'o' or 'u':
        print('achei uma vogal')
    else:
        print('não achei vogal')
    print(acharVogal(arquivo))

#4


