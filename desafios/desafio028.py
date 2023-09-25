import random
from time import sleep  # serve pra simular um carregamento, só escrever sleep(3)
n = random.randint(0,5)
u = int(input('Escolha um número de 0 a 5: '))

if u == n:
    print('Você acertou o número que o computador pensou')
else:
    print('Você errou o número')