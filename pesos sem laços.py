n1 = float(input('Qual é o peso da 1ª pessoa?: '))
n2 = float(input('Qual é o peso da 2ª pessoa?: '))
n3 = float(input('Qual é o peso da 3ª pessoa?: '))
n4 = float(input('Qual é o peso da 4ª pessoa?: '))
n5 = float(input('Qual é o peso da 5ª pessoa?: '))
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print('O maior peso é {}'.format(n1))
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print('O maior peso é {}'.format(n2))
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print('O maior peso é {}'.format(n3))
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print('O maior peso é {}'.format(n4))
else:
    print('O maior peso é {}'.format(n5))

if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
    print('O menor peso é {}'.format(n1))
elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    print('O menor peso é {}'.format(n2))
elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    print('O menor peso é {}'.format(n3))
elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    print('O menor peso é {}'.format(n4))
else:
    print('O menor peso é {}'.format(n5))
