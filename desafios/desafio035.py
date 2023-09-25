reta1 = float(input('Digite a primeira reta do triângulo: '))
reta2 = float(input('Digite a segunda reta do triângulo: '))
reta3 = float(input('Digite a terceira reta do triângulo: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Essas retas formam um triângulo')
else:
    print('Essas retas não formam um triângulo')


