import math
num = float(input('Digite o ângulo que você deseja: '))
# Quando eu tava fazendo esse exercício, surgiu um erro relacionado ao math.sin,
# Nessas funções importados, eles fazem os calculos, retornando o x(número digitado)
# Em radianos, então tive problemas e só entendi que deveria converter o número digitado
# Pelo usuário em radianos, depois que vi o vídeo e para isso existe a função math.radians
cos = math.cos(math.radians(num))
sen = math.sin(math.radians(num))
tan = math.tan(math.radians(num))
print('O ângulo de {} tem o Seno de {:.2f}'.format(num, sen))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(num, cos))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(num, tan))

