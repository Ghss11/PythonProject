valores = []
menor = 1000
maior = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {cont}: ')))
print(f'Você digitou os valores {valores}')
for n in valores:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()