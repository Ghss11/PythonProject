print('\033[33m-=-\033[m' * 12)
print('       \033[34mTERMOS DE UMA PA\033[m')
print('\033[33m-=-\033[m' * 12)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
m = n + (r * 10)
s = 0
c = n
total = 0
for c in range(n, m, r):
    s += c
    print('{}'.format(c), end=' ➡ ')
print('PAUSA')
h = 1
total += 1
while h != 0:
    h = int(input('\nQuantos termos você quer mostrar a mais? '))
    if h !=0:
        h1 = h + 1
        m2 = c + (r * h1)
        n2 = c + r
        for o in range(n2, m2, r):
            print('{} ➡ '.format(o), end='')
            c = o
            total += 1
        print('PAUSA')
print('Progressão finalizada com {} termos'.format(total + 9))