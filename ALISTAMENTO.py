import datetime
n = int(input('Ano de nascimento: '))
h = datetime.date.today().year
i = h - n
f = 18 - i
g = n + 18
j = i - 18
print('Quem nasceu em {} tem {} anos em {}'.format(n, i, h))
if i < 18:
    print('Ainda faltam {} para seu alistamento \nSeu alistamento sera em {}'.format(f, g))
elif i == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado a {} anos \nSeu alistamento foi em {}'.format(j, g))