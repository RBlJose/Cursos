archivo = open('archivo.txt', 'w')
archivo.write('hola mundo!')
archivo.close()

archivo = open('archivo.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close()

archivo = open('archivo.txt', 'r')
for linea in archivo:
    print (linea)
archivo.close()

with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)