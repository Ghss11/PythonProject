import datetime
t = 0
n1 = int(input('Em que ano a 1ª pessoa nasceu? '))
n2 = int(input('Em que ano a 2ª pessoa nasceu? '))
n3 = int(input('Em que ano a 3ª pessoa nasceu? '))
n4 = int(input('Em que ano a 4ª pessoa nasceu? '))
n5 = int(input('Em que ano a 5ª pessoa nasceu? '))
n6 = int(input('Em que ano a 6ª pessoa nasceu? '))
n7 = int(input('Em que ano a 7ª pessoa nasceu? '))
i1 = datetime.date.today().year - n1
i2 = datetime.date.today().year - n2
i3 = datetime.date.today().year - n3
i4 = datetime.date.today().year - n4
i5 = datetime.date.today().year - n5
i6 = datetime.date.today().year - n6
i7 = datetime.date.today().year - n7
I = [i1, i2, i3, i4, i5, i6]
t = 0
for i in I:
    t += 1
print(t)


