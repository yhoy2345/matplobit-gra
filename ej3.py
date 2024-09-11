import matplotlib.pyplot as plt

# Definir los puntos
x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]  # El punto medio (2.5, 2) forma la punta del "triángulo"

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)  # 'b-' significa línea azul continua

# Graficar la línea con estilo entrecortado
plt.plot(x, y, color='#00BFFF', linestyle='--', linewidth=2, marker='o', label='Línea 1')

# Personalizar el gráfico
plt.title('Gráfico triangular abierto')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)

# Ajustar los límites de los ejes
plt.xlim(1.0, 8.0)
plt.ylim(1.0, 8.0)

# Marcar los puntos específicos
plt.plot(x[0], y[0], 'ro')  # Punto inicial
plt.plot(x[1], y[1], 'ro')  # Punto medio (punta)
plt.plot(x[3], y[3], 'ro')  # Punto medio (punta)
plt.plot(x[4], y[4], 'ro')  # Punto medio (punta)
plt.plot(x[2], y[2], 'ro')  # Punto final


# Mostrar el gráfico
plt.show()