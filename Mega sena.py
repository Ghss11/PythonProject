from random import randint
from time import sleep
lista = []
jogos = []
print('-'*30)
print('     JOGUE NA MEGA SENA      ')
print('-'*30)
quant = int(input('Quantos jogos você quer sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-'*30)
print(f'-=-=-= SORTEANDO {quant} JOGOS -=-=-=')
for j in range(quant):
    sleep(1)
    print(f'Jogo {j+1}: {jogos[j]}')
    sleep(1)
print('=-=-=-=- BOA SORTE =-=-=-=-')