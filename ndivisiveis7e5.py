numeros = []

for i in range(100, 301):
    if i % 7 == 0 and i % 5 != 0:
        numeros.append(str(i))

print(",".join(numeros))
