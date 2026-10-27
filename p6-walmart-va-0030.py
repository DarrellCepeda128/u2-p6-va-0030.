import matplotlib.pyplot as plt
import numpy as np
# Cepeda Darrell NC = 0030

cant_productos=[100,150,200,300,500]
precio = [4000, 7000, 9000, 12000, 18000]

#plt.plot(cant_productos)
#plt.show()

# personalizando graficas
plt.plot(cant_productos,precio,color="green",marker="o",linestyle="dashed",linewidth=2,markersize=14)
plt.title("Ventas de Walmart")
plt.xlabel("precios")
plt.ylabel("cant productos")
plt.show()