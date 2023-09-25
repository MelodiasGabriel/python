d = int(input('Esse carro foi alugado por quantos dias? '))
k = float(input('Quantos KM foram percorridos com o carro? '))
total = (60 * d) + (k * 0.15)  # 60 * d + k * 0.15 -> conta pode ser feita sem parenteses
print('O total a pagar é R${:.2f}'.format(total))
