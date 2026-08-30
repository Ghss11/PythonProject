from random import randint
v = 0
print('=-' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 13)
while True:
    n1 = int(input('Digite um valor: '))
    Pc = randint(0, 10)
    tip =  ' '
    tot = n1 + Pc
    while tip not in 'PI':
        tip = str(input('ímpar ou par (I/P): ')).strip().upper()[0]
    print(f'você jogou {n1} e o computador jogou {Pc}. Total de {tot}')
    if tip == 'P':
        if tot % 2 == 0:
            print('Você venceu!!!')
            v += 1
        else:
            print('Você perdeu!!!')
            break
    elif tip == 'I':
        if tot % 2 == 1:
            print('Você venceu!!!')
            v += 1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos jogar novamente...')
if v == 1:
    print(f'Gamer over!!! Você venceu {v} vez')
else:
    print(f'Gamer over!!! Você venceu {v} vezes')
