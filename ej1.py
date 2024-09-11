import matplotlib.pyplot as plt

# Definir los puntos
x = [1, 2, 3]
y = [2, 4, 1]  # El punto medio (2.5, 2) forma la punta del "triángulo"

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)  # 'b-' significa línea azul continua

# Personalizar el gráfico
plt.title('Gráfico triangular abierto')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)

# Ajustar los límites de los ejes
plt.xlim(1.0, 3.0)
plt.ylim(1.0, 4.0)

# Marcar los puntos específicos
plt.plot(x[0], y[0], 'ro')  # Punto inicial
plt.plot(x[1], y[1], 'ro')  # Punto medio (punta)
plt.plot(x[2], y[2], 'ro')  # Punto final


# Mostrar el gráfico
plt.show()