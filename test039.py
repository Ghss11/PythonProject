n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m{}'.format(c), end=' ')
        t += 1
    else:
        print('\033[33m{}'.format(c), end=' ')
if t == 2:
    print('\n\033[mO número {} é primo pois foi divisivel apenas {} vezes'.format(n, t))
else:
    print('\n\033[mO número {} não é primo pois foi divisivel {} vezes'.format(n, t))