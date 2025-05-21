import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Crea alcuni punti casuali in 2D
points = np.random.rand(10, 2)

# Calcola la triangolazione
tri = Delaunay(points)

# Grafico
plt.figure(figsize=(12, 6))
plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.plot(points[:,0], points[:,1], 'o')
plt.tick_params(axis='both', which='major', labelsize=26)
plt.title('Esempio di triangolazione di Delaunay ', fontsize=30)
plt.show()