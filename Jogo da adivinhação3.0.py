from random import randint
from time import sleep
n = randint(0,50)
baixo, alto = 0, 50
print('\033[1;33m-=-\033[m' * 20)
print('\033[1;34mVou pensar em número entre 0 e 50. Tente adivinhar...\033[m')
print('\033[1;33m-=-\033[m' * 20)
print('PROCESSANDO...')
acertou = False
T = 0
sleep(3)
while not acertou:
    j = int(input('Em que número eu pensei? '))
    T += 1
    if j == n:
        acertou = True
    else:
        if j < n:
            print('Mais... Tente novamente!')
        elif j > n:
            print('Menos... Tente novamente!')

    chute_pc = (baixo + alto) // 2
    print('Eu acho que o número que você pensou foi {}'.format(chute_pc))
    dica = input("Dica: (A)certou, (M)aior ou (m)enor: ")[0]
    if dica == 'A':
        acertou = True
        print('O PC VENCEU!!!')
    elif dica == 'M':
        baixo = chute_pc + 1
    elif dica == 'm':
        alto = chute_pc - 1
print('Acertou com {} tentativas, Parabéns!'.format(T))
