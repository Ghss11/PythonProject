
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
     break
    for c in range(1, 11):
        t = n * c
        print('{} x {} = {}'.format(n, c, t))
    print('-' * 30 )
print('FIM DO PROGRAMA')