aluno = dict()
aluno['Nome'] = input('Digite o nome do aluno: ')
aluno['média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['média'] >= 7 :
    aluno['situacao'] = 'Aprovado'
elif aluno['média'] >= 4 and aluno['média'] < 7 :
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-' * 40)
for k, v in aluno.items():
    print(f'-{k}: {v}')
