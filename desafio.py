from random import randint
s = randint(1, 20)
t = 0
while True:
    t += 1
    n = int(input('Adivinhe o número de 1 a 20: '))
    if n == s:
        break
    if n > s:
        print('Dica: O número é menor')
        print('Tente mais uma vez')
    if n < s:
        print('Dica: O número é maior')
        print('Tente mais uma vez')
    if t == 5:
        print('Acabou suas tentativas!')
        break
if t == 5:
    print('Você perdeu!')
else:
    print(f'Parabéns você acertou com {t} tentativas')
