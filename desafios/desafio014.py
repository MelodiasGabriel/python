t = float(input('Digite a temperatura atual em ºC: '))
f = (t * 1.8) + 32   # ou ((9*c)/5)+32 -> essa conta pode ser feita sem parenteses também
print('A temperatura atual {}ºC em Fahrenheit é {}ºF'.format(t, f))