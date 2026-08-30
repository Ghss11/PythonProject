n1 = float(input('Qual é a largura da parede?: '))
n2 = float(input('Qual é a altura da parede?: '))
A = n1 * n2
T = A / 2
V = T * 4.5
print('A aréa pintada é {}, e vai ser gasto {} tintas, sendo gasto um valor de {} reais'.format(A, T, V))