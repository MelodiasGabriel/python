frase = str(input('Digite uma frase aleatória: ')).strip().lower()
print('A letra "A", aparece {} vezes'.format(frase.count('a')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('E aparece pela última vez na posição {}'.format(frase.rfind('a')+1))

