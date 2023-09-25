frase = 'é o Melol do python'
print(frase[6])
print(frase[6:10])
print(frase[:10])
print(frase[6:])
print(frase[2:19:2])
print(frase[1::3])
print(frase[:2])

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed mi turpis, porta at neque sit amet, tincidunt ultricies tellus. Nunc congue mi sed nisi blandit pulvinar. 
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
Integer aliquam nisi a dolor efficitur varius. Cras sit amet urna sapien. Suspendisse tempus elementum laoreet. 
Sed pretium maximus libero, vitae scelerisque lectus aliquet non. Aliquam sit amet enim eros.
Mauris ac dui tempus, malesuada neque ac, scelerisque augue. Duis vulputate nisi eu pulvinar dapibus. 
Duis iaculis suscipit erat. Etiam pellentesque nunc sit amet luctus gravida. Phasellus sit amet purus et sem dictum facilisis. 
Nunc quis elit mattis, euismod arcu eget, rutrum magna. Vivamus a finibus tortor. Praesent tortor purus, venenatis in mattis non, sollicitudin non odio. 
Integer semper justo tortor, et pulvinar erat auctor congue. Nulla vel elit lectus. Vestibulum molestie ac nibh ut tempor.""")

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('python', 'php'))
print('melol' in frase)
print(frase.find('Melol'))
print(frase.find('melol'))
print(frase.lower().find('melol'))
print(frase.strip())

print(frase.split())
dividido = frase.split()
print(dividido[2])
print(dividido[2][3])

