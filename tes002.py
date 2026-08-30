n = str(input('Digite um a frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(n.count('A')))
print('A letra A apareceu a primeira vez na posição {}'.format(n.find('A')+1))
print('A letra A apareceu a ultima vez na posição {}'.format(n.rfind('A')+1))