import math
n1 = float(input('Digite o angulo:'))
seno = math.sin(math.radians(n1))
cosseno = math.cos(math.radians(n1))
tangente = math.tan(math.radians(n1))
print(" o SENO É:{:.2f}\n o COSSENO É:{:.2f}\n a TANGENTE é:{:.2f} ".format(seno, cosseno, tangente))