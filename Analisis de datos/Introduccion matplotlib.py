import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = x

#crear una linea
plt.plot(x, y)
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Mi primera Grafica')
plt.show()

#grafica de barras
categoria = ['A', 'B', 'C', 'D', 'E', 'F']
valores = [1, 2, 3, 4, 5, 6,]

plt.bar(categoria, valores)
plt.show()

#estilos de graficos
plt.style.use('ggplot')
plt.style.available

x= [0, 1, 2, 3, 4, 5]
y= [0, 1, 4, 9, 16, 25]

plt.plot(x,y, color='red', linestyle= '--', marker= 'o')
plt.show()