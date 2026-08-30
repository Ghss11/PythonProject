print('\033[33m-=-\033[m' * 12)
print('       \033[34m10 TERMOS DE UMA PA\033[m')
print('\033[33m-=-\033[m' * 12)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
m = r * 10
s = 0
for c in range(n, m, r):
    print(f'{c}', end=' ➡ ')
    s += c
print('FIM')
print('A soma dessa PA é {}'.format(s))

