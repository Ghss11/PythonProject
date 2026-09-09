p = float(input('Qual é seu peso em Kg?'))
a = float(input('Qual é sua altura em metros?'))
i = p / (a**2)
print('Seu indíce de massa corporal é {:.2f}'.format(i))
if i < 18.5:
    print('Você estar a baixo do peso adequado')
elif 18.5 <= i < 25:
    print('Você estar dentro da normalidade')
elif 25 <= i < 30:
    print('Você estar na categoria de pré obesidade')
elif 30 <= i < 35:
    print('Você estar na categoria de obesidade grau 1')
elif 35 <= i < 40:
    print('Você estar na categoria de obesidade grau 2')
else:
    print('\033[31mVocê estar em obesidade extrema')