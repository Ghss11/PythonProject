alunos = []
print('-'*40)
print('       CADASTRO DE ALUNOS')
print('-'*40)

while True:
    nome = input('Nome do aluno (ou ENTER para parar): ').strip()
    if nome == '':
        break
    nota1 = float(input(f'Nota 1 de {nome}: '))
    nota2 = float(input(f'Nota 2 de {nome}: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])
    print(f'{nome} cadastrado com sucesso!')
    print('-'*40)

if len(alunos) == 0:
    print('Nenhum aluno cadastrado.')
else:
    # Boletim geral
    print()
    print('='*40)
    print('              BOLETIM GERAL')
    print('='*40)
    print(f'{"ALUNO":<20} {"N1":>4} {"N2":>4} {"MÉDIA":>6}')
    print('-'*40)
    for aluno in alunos:
        situacao = 'AP' if aluno[3] >= 6 else 'RE'
        print(f'{aluno[0]:<20} {aluno[1]:>4.1f} {aluno[2]:>4.1f} {aluno[3]:>5.1f} {situacao}')
    print('='*40)

    # Consulta individual
    print()
    while True:
        print('Consulta individual (ENTER para sair)')
        busca = input('Digite o nome do aluno: ').strip().lower()
        if busca == '':
            break
        encontrado = False
        for aluno in alunos:
            if aluno[0].lower() == busca:
                encontrado = True
                print()
                print('='*30)
                print(f'  Aluno : {aluno[0]}')
                print(f'  Nota 1: {aluno[1]:.1f}')
                print(f'  Nota 2: {aluno[2]:.1f}')
                print(f'  Média : {aluno[3]:.1f}')
                print(f'  Sit.  : {"APROVADO" if aluno[3] >= 6 else "REPROVADO"}')
                print('='*30)
                print()
        if not encontrado:
            print(f'Aluno "{busca}" não encontrado.')
        print('-'*40)

    print('Programa encerrado. Até mais!')

