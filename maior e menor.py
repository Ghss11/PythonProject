from random import randint
t = (randint(1, 10,),randint(1, 10,),randint(1, 10,),
         randint(1, 10,),randint(1, 10,))
menor = t[0]
maior = 0
print(f'Os valores sorteados foram: {t}')
for n in t:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('O maior valor sorteado foi {}'.format(maior))
print('O menor valor sorteado foi {}'.format(menor))
