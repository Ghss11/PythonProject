from math import factorial
from time import sleep
print('Digite um número para')
n = int(input('calcular o fatorial: '))
fatorial = factorial(n)
print('Calculando... {}! ='.format(n), end=' ')
sleep(1)
for c in range(n, 0, -1):
    if c > 1:
        print('{} x '.format(c), end='')
    else:
        print('{}'.format(c), end=' ')
print('= {}'.format(fatorial))
