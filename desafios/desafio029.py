velocidade = float(input('Digite a velocidade do seu carro: '))
multa = (velocidade - 80.0)*7.0

if velocidade > 80.9:
    print('Você foi multado! O valor total da multa é {}!'.format(multa))
else:
    print('Tudo tranquilo por aqui')
