import random
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('quarto aluno:'))
n5 = str(input('quinto aluno:'))
lista = [n1, n2, n3, n4, n5]
sorteado = random.shuffle(lista)
print('A nova ordem será')
print(lista)