#Exercícios sessão 7
'''
#1
a = [1, 0, 5, -2, -5, 7]
soma = a[0] + a[1] + a[5]
print(f'a soma dos vetores na posição 0,1,5 é {soma}')
a[3]= 100


for index, item in enumerate(a):
    print(f'index: {index} | valor: {item}')

#2
vet=[]
nu = 6
while nu > 0:
    vet.append(int(input("digite um numero:")))
    nu = nu - 1
print(vet)


#3

vet =[]
quadrado= []

for i in range(10):
      vet.append(float(input('Digite um numero Real: ')))
      quadrado.append(float(vet[i]**2))
print('o quadrado é ',quadrado, end = " ," )
print('o vetor é :' ,vet)



#4

vet= []
limite = 8
while limite > 0:
    vet.append(int(input("digite um numero:")))
    limite = limite - 1
print(vet)

x = vet[2]
y= vet[5]
print(x+y)


#5
vet = [2, 5, 6, 4, 9, 8, 7, 10, 50, 44, 73]
pares = []
quantidade = 0

for i in vet:
    if (i % 2 == 0):
      pares.append(i)
print(f'numeros pares encontrados{pares} ')


#6
vet = []
limite = 11
while limite > 0:
    vet.append(input('digite um numero:'))
    limite = limite - 1
print(min(vet),max(vet))



#7
vet = []
limite = 10
while limite > 0:
    vet.append(input('digite um número:'))
    limite = limite -1
for indice,valor in enumerate(vet):
    print(indice,valor)



#8

vet = [2, 10, 55, 66, 44, 96]
print(vet)

vet.reverse()
print(vet)


#10
vet = []
limite = 5
while limite > 0:
    vet.append(int(input('digite a nota:')))
    limite = limite - 1
soma=0
media = 0
for i in vet:
    soma = sum(vet)
    media = soma / 5
print(media)

'''

