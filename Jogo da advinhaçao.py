from random import randint
from time import sleep
n: int = randint(0,5)
print('\033[1;33m-=-\033[m' * 20)
print('\033[1;34mVou pensar em número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;33m-=-\033[m' * 20)
j = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if j == n:
    print('PARABÉNS VOCÊ ACERTOU!!! eu realmente pensei no número {}'.format(n))
else:
    print('EU GANHEI!!!, pensei no número {} não no número {}, tente outra vez'.format(n, j))
