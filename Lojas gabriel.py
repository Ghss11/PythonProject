print('\033[33m==\033[m' * 10,'\033[7;30;47mLOJAS GABRIEL\033[m', '\033[33m==\033[m' * 10)
v = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro ou cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input('Qual opcção deseja pagar? '))
if o==1:
    p = v - (v * 10 / 100)
    print('Com o pagamento a vista você ganhou um desconto, Parabéns sua compra no valor de R${} vai sair por R${}'.format(v, p))
elif o == 2:
    p = v - (v * 5 / 100)
    print('Parabéns você ganhou um desconto, sua compra no valor de R${} vai sair por R${} '.format(v, p))
elif o == 3:
    p = v + (v * 4 / 100)
    u = p / 2
    print('O valor da compra dividido em 2x no cartão sofre um acrescimo devido ao juros da maquineta, sua compra de R${} vai ficar em 2 parcelas de {:.2f}R$ \nResultando em um total de R${} '.format(v, u, p))
else:
    q = int(input('Quantas parcelas? '))
    p = v + (v * 7 / 100)
    u = p / q
    print('O valor da compra dividido em {}x no cartão sofre um acrescimo devido ao juros da maquineta, sua compra de R${} vai ficar em {} parcelas de {:.2f}R$ \nResultando em um total de R${} '.format(q, v, q, u, p))
