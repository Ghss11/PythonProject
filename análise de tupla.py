n1 = int(input('Qual é o primeiro valor: '))
n2 = int(input('Qual é o segundo valor: '))
n3 = int(input('Qual é o terceiro valor: '))
n4 = int(input('Qual é o quarto valor: '))
t = (n1, n2, n3, n4)
maior = 0
menor = t[0]
print(f'Você digitou os valores {t} ')
for n in t:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
print(f'O valor 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 apareceu a primeira vez na posição {t.index(3)+1}')
else:
    print('O valor 3 não foi encontrado na lista')
print(f'Os valores pares digitados foram ', end = '')
for n in t:
    if n % 2 == 0:
        print(n, end=' ')

