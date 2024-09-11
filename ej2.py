import matplotlib.pyplot as plt

# Definir los puntos de la primera línea
x1 = [1, 2, 3]
y1 = [2, 4, 1]

# Definir los puntos de la segunda línea
x2 = [1, 2, 3]
y2 = [4, 1, 3]

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Graficar la primera línea con color morado
plt.plot(x1, y1, color='#00BFFF', linewidth=2, label='Línea 1')  # '#800080' es el código hexadecimal para morado

# Graficar la segunda línea con color verde oscuro
plt.plot(x2, y2, color='#FF69B4', linewidth=2, label='Línea 2')  # '#006400' es el código hexadecimal para verde oscuro

# Personalizar el gráfico
plt.title('Gráfico triangular con dos líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)

# Ajustar los límites de los ejes
plt.xlim(1.0, 3.0)
plt.ylim(1.0, 4.0)

# Marcar los puntos específicos de la primera línea
plt.plot(x1[0], y1[0], 'ro')  # Punto inicial Línea 1
plt.plot(x1[1], y1[1], 'ro')  # Punto medio Línea 1
plt.plot(x1[2], y1[2], 'ro')  # Punto final Línea 1

# Marcar los puntos específicos de la segunda línea
plt.plot(x2[0], y2[0], 'ms')  # Punto inicial Línea 2 (cuadrado magenta)
plt.plot(x2[1], y2[1], 'ms')  # Punto medio Línea 2
plt.plot(x2[2], y2[2], 'ms')  # Punto final Línea 2

# Agregar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
