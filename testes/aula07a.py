""" n1 = pow(4,3)
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^100}!'.format(nome))
{:20}
{:>20}
{:<20}
{:^20}
{:=^20}"""

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a subtração é {} o produto é {}, e a divisão é {:.3f}'.format(s, su, m, d), end=' -> ')
print('Divisão inteira {}, e potência {}'.format(di, e))

# :.3f -> está formatando o valor da divisão pra aparecer só três casas decimais depois do ponto
# : \n -> quebra linha
# : end=' ' faz com que no final da execução a linha não seja quebrada



