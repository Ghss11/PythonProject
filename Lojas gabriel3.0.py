print('\033[33m==\033[m' * 10, '\033[7;30;47mLOJAS GABRIEL\033[m', '\033[33m==\033[m' * 10)

menor = 0
barato = ''
total = 0     
cont = 0

while True:
    n = input('Nome do produto: ')
    p = float(input('Preço: R$ '))
    total += p
    cont += 1

    if cont == 1:
        menor = p
        barato = n
    else:
        if p < menor:
            menor = p
            barato = n

    resp = ''
    while resp not in ('S', 'N'):
        resp = input('Quer continuar comprando? (S/N) ').strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' RESUMO DA COMPRA '))
print(f'Você comprou {cont} produto(s).')
print(f'O total da compra foi R${total:.2f}')
print(f'O produto mais barato foi "{barato}" e custou R${menor:.2f}.')

v = total

print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro ou cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input('Qual opção deseja pagar? '))

if o == 1:
    p_final = v - (v * 10 / 100)
    print('Com o pagamento à vista você ganhou um desconto! Sua compra no valor de R${:.2f} vai sair por R${:.2f}'.format(v, p_final))
elif o == 2:
    p_final = v - (v * 5 / 100)
    print('Parabéns, você ganhou um desconto! Sua compra no valor de R${:.2f} vai sair por R${:.2f}'.format(v, p_final))
elif o == 3:
    p_final = v + (v * 4 / 100)
    parcela = p_final / 2
    print('O valor da compra dividido em 2x no cartão sofre um acréscimo devido aos juros da maquineta.\nSua compra de R${:.2f} vai ficar em 2 parcelas de R${:.2f}\nResultando em um total de R${:.2f}'.format(v, parcela, p_final))
else:
    q = int(input('Quantas parcelas? '))
    p_final = v + (v * 7 / 100)
    parcela = p_final / q
    print('O valor da compra dividido em {}x no cartão sofre um acréscimo devido aos juros da maquineta.\nSua compra de R${:.2f} vai ficar em {} parcelas de R${:.2f}\nResultando em um total de R${:.2f}'.format(q, v, q, parcela, p_final))