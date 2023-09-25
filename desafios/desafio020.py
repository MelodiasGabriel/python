import random
al1 = input('Primeiro Aluno: ')
al2 = input('Segundo Aluno: ')
al3 = input('Terceiro Aluno: ')
al4 = input('Quarto Aluno: ')
grupo = [al1, al2, al3, al4]
# random.shuffle(grupo)
# Fiz da forma abaixo no primeiro print, mas na resolução, ele embaralhou a lista no .shuffle
# E depois chamou ela, tentei usar esse método, mas direto no print, por isso não deu certp
# Então a solução dele é receber os valores, embaralhar e depois mostrar na tela,
# Na que eu fiz a única diferença é que ele embaralha junto com o print pra mostrar na tela
print('A ordem de apresentação será \n{}'.format(random.sample(grupo, k=len(grupo))))
# print(grupo)
