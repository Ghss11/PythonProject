v = float(input('Valor da casa: R$ '))
s = float(input('Salário do comprador: R$ '))
f = int(input('Quantos anos de financiamento: '))
m = v / (f * 12)
p = (m / s) * 100
if m>= 0.3 * s:
    print('Emprestimo NEGADO!!!')
else:
    print('Parabéns emprestimo concebido')
print('Para pagar uma casa de R${} em {} ano a prestação será de R${:.2f}, oque equivale a {:.1f}% do seu salário!'.format(v, f, m, p))