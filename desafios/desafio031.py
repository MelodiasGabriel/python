distancia = float(input('Digite a distância total da viagem: '))
passagem1 = distancia * 0.50
passagem2 = distancia * 0.45

if distancia <= 200.9:
    print('O valor da passagem1 é {}'.format(passagem1))
else:
    print('O valor da passagem2 é {}'.format(passagem2))
