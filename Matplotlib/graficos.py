import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Documentación en matplotlib.com

# Valores
x = np.linspace(1,150,200)
y = x + x**2

# Preparar gráfica
plt.plot(x,y,'blue') 
plt.title('Gráfico')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

# Subplots
plt.subplot(1,2,1)
plt.plot(x,y,'green')
plt.subplot(1,2,2)
plt.plot(x,y,'red')
plt.show()