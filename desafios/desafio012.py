p = float(input('Digite o preço do produto: R$'))
d = p - (p * 5 / 100)
print('O valor original do produto era R${}, e agora com desconto é R${:.2f}'.format(p, d))
