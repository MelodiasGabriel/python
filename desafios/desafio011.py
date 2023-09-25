h = float(input('Digite a altura da parede em metros: '))
la = float(input('Digite a largura da parede em metros: '))
a = h * la
t = a / 2
print('A Altura da parede é {}, sua largura é {},\na área é {}m² \ne para pintar vai precisar de {:.1f} litros de tinta'.format(h, la, a, t))
