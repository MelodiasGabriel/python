nome = str(input('Digite seu nome completo: ')).strip()
primeiroNome = nome.split()
print('Seu primeiro nome é {}'.format(primeiroNome[0]))
print('Seu último nome é {}'.format(primeiroNome[len(primeiroNome)-1]))

