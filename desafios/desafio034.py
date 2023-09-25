salario = float(input('Qual seu salário atual? R$ '))
aumento1 = salario * 10 / 100
aumento2 = salario * 15 / 100
if salario > 1250.99:
    salario = salario + aumento1
else:
    salario = salario + aumento2
print('Seu salário com aumento é {:.2f}'.format(salario))
