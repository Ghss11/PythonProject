sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Informação invalida, informe o sexo [M/F]: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))


