
#Exercícios Sessão 5


#1

Numero = int(input("digite um numero:"))
Numero2 = int(input("digite um numero:"))
if Numero > Numero2:
    print(Numero,'é maior que ',Numero2)
else:
    print(Numero2,"é maior que ", Numero)

#2

nu= int(input("digite um numero:"))
if nu > 0:
    raiz = float(nu)**0.5
    print(  'a raiz de ', nu, 'é', raiz)
elif nu < 0:
    print("número inválido")

#3
num= int (input('Digite um número:'))
if num > 0 :
    qua= num * 2
    RaizQ= float(num)**0.5
    print('o numero digitado ao quadrado é ', qua , 'e a raiz é ',RaizQ)
elif num < 0:
    print('numero inválido')

#5
Nume= int (input("Digite um número:"))
if Nume % 2 == 0 :
    print('numero é par')
else:
    print('numero é impar')

#6

num1 = int(input('digite um número:'))
num2 = int(input('digite um número :'))
if num1 > num2:
    print(num1, 'é maior que ', num2)
else:
    print(num2,'é maior que', num1)
dif = num1 - num2
print('diferença é igual',dif)



#21 lista 05

print("escolha a opção")
print('1-soma de numeros')
print('2- Diferença entre dois numeros')
print('3-produto entre dois numeros')
print('4- divisao entre dois numeros')
op= int(input("Escolha a opção:"))

if op == 1:
    nu= int(input('escolha um numero para somar'))
    nu2 = int(input('escolha um numero para somar'))
    print(' o resultado da soma é' ,nu+nu2)
elif  op == 2:
    nu = int(input('escolha um numero:'))
    nu2 = int(input('escolha um numero:'))
    print('a diferença entre eles é ',nu-nu2)
elif op == 3:
    nu = int(input('escolha um numero:'))
    nu2 = int(input('escolha um numero:'))
    print('o produto entre eles é :',nu*nu2)
elif op == 4 :
    nu = int(input('escolha um numero:'))
    nu2 = int(input('escolha um numero:'))
    print('a divisao entre eles é', nu/nu2)
