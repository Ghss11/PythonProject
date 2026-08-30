n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
m = (n1 + n2) / 2
if m >= 7:
    print('''Sua media foi {} 
    \033[32mParabéns você foi APROVADO!'''.format(m))
elif m < 4:
    print('''Sua media foi {}
     \033[31mVocê foi REPROVADO!'''.format(m))
else:
    print('''Sua media foi {}
    \033[34mVocê ficou de recuperação!'''.format(m))