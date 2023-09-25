nome = str(input('Digite o seu nome completo: ')).strip()  # pra tirar os espaços antes e depois

print('Nome em maisculo {}'.format(nome.upper()))
print('Nome em minusculo {}'.format(nome.lower()))
"""qtdLetras = nome.split()
print(len(qtdLetras))"""
nomenum = nome.replace(' ', '')  # ele fez assim
# ... .format(len(nome) - nome.count(' '))
qtdCarac = len(nomenum)
print('Quantidade de caracteres {}'.format(qtdCarac))

primNome = nome.split()
print('Quantidade de caracteres do primeiro nome {}'.format(len(primNome[0])))  # ele fez assim
# ... .format(nome.find(' '))
