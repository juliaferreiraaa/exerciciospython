
#Exercícios Sessão 6




#1 lista 6
for multiplo in range(1,16):
     if multiplo % 3 == 0:
         print(multiplo,'é multiplo de 3 ')
"""
"""
#2 lista 6 #usando for
for i in range(1,101):
    print(i)
    
#usando while    
doce = 1
while doce < 101:
    print(doce," ", end="")
    doce += 1
    print()
    
#3 lista 6

numb = 11
while numb > -1:
    numb = numb - 1
    print(numb, ' ', end='')
    if numb == 0:
        print('FIM !')
        break
print('0',end =" ")
print('ju')


#4 lista 6
nu= 0
limite= 100000
while nu <= limite:
    nu += 1000
    print(nu)
   

    
#5 lista 6
lista = []
limite = 10
while limite > 0:
   lista.append(int(input('digite um numero')))
   limite -= 1
print(f'a soma é : {sum(lista)}')


#6 lista 6
lista = []
limite = 3
while limite > 0:
   lista.append(float(input('digite um numero')))
   soma = sum(lista)
   limite = limite - 1

limite=3
media = soma/ limite
print('média é = ',media)





















