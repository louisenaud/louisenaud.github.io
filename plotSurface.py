import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

def fun(x, y):
  return x**2 + y**2

fig = plt.figure()


ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-5.0, 5.0, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
ax.set_axis_bgcolor("#3E3E3E")
img = ax.plot_surface(X, Y, Z, alpha=0.75, color="#ADD8E6")
#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')
plt.axis('off')
plt.savefig("paraboloid.png", bbox_inches='tight')
plt.show()
