s = float(input('Digite o seu salário atual: R$'))
ns = s + (s * 15 / 100)
print('Seu salário era R${:.2f}, e agora com aumento é R${:.2f}'.format(s, ns))
