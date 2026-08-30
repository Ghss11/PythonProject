from time import sleep
from random import choice
print('''Suas opcções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
o = int(input('Qual é sua jogada? '))
print('JO')
sleep (1)
print('KEN')
sleep (1)
print('PO!!!')
l = ['PEDRA','PAPEL','TESOURA']
c = choice(l)
print('-=-' * 10)
print('Computador jogou {}'.format(c))
print('Jogador jogou {}'.format(l[o]))
print('-=-' * 10)
if c == 'PEDRA' and o == 0 or c == 'PAPEL' and o == 1 or c == 'TESOURA' and o == 2:
    print('EMPATE')
elif c == 'PEDRA' and o == 1:
    print('JOGADOR VENCE')
elif c == 'PEDRA' and o == 2:
    print('COMPUTADOR VENCE')
elif c == 'PAPEL' and o == 0:
    print('COMPUTADOR VENCE')
elif c == 'PAPEL' and o == 2:
    print('JOGADOR VENCE')
elif c == 'TESOURA' and o == 0:
    print('JOGADOR VENCE')
elif c == 'TESOURA' and o == 1:
    print('COMPUTADOR VENCE')