n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print('O número {} é o maior'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O número {} é o maior'.format(n2))
else:
    print('O número {} é o maior'.format(n3))

if n1 < n2 and n1 < n3:
    print('O número {} é o menor'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O número {} é o menor'.format(n2))
else:
    print('O número {} é o menor'.format(n3))
