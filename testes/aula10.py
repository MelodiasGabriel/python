"""nome = str(input('Qual seu nome? '))
if nome == 'Gabriel':
    print('Belo nome Melol!')
else:
    print('Nome muito normal esse seu hein')
print('Bom dia, {}!'.format(nome))"""

n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.5:
    print('Acima da média, nada mais que sua obrigação')
elif m == 6.0:
    print('Exatamente na média, fica esperto rapaz')
else:
    print('Tá abaixo da média hein, tem que estudar mais')

