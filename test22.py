
n = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maisculas é:{}'.format(n.upper()))
print('seu nome em minisculas é:{}'.format(n.lower()))
print('Seu nome tem {} letras:'.format(len(n)-n.count(' ')))
print('Seu primeiro nome tem {} letras:'.format(n.find(' ')))
