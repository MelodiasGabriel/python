import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
