import matplotlib.pyplot as plt
import numpy as np

# Definimos el rango de x
x = np.linspace(0, 2, 21)

# Definimos la paleta de colores inspirada en TV Girl
colors = {'linea': '#FAD02E', 'cuadrado': '#F28D35', 'triangulo': '#6D28D9'}

# Creamos la figura
plt.figure()

# Graficamos con los colores especificados y tipos de líneas y marcadores correctos
plt.plot(x, x-x, color=colors['linea'], linestyle='-', marker='o', label='y = linea')           
plt.plot(x, x**2, color=colors['cuadrado'], linestyle='-', marker='s', label='y = cuadrado')      
plt.plot(x, x**3, color=colors['triangulo'], linestyle='-', marker='^', label='y = triangulo')    

# Añadimos título y etiquetas
plt.title('Gráficos')
plt.xlabel('x')
plt.ylabel('y')

# Añadimos la leyenda y la cuadrícula
plt.legend()
plt.grid(True)

# Mostramos el gráfico
plt.show()
