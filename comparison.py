import numpy as np
from stl import mesh
from spherical_utilities import *
from new import data
import matplotlib.pyplot as plt
# import plotly
cut = np.array(data)
triangles = []
points = []
x = []
y = []
z = []
for triangle in data:
    triangles.append(triangle)
    for point in triangle:
        points.append(point)
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])

r,theta,phi = cartesian_to_spherical(np.array(x),np.array(y),np.array(z))
new_phi = phi + np.deg2rad(45)
new_x, new_y, new_z = spherical_to_cartesian(r, theta, new_phi)
old_mesh = np.stack([x,y,z], axis=-1)
new_mesh = np.stack([new_x, new_y, new_z], axis=-1)



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
ax.set_aspect('equal')

# plt.show()
# ax2 = fig.add_subplot(111, projection='3d')
# ax2.plot(new_x, new_y, new_z)

plt.savefig("comparison.png")