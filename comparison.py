import numpy as np
from stl import mesh
from spherical_utilities import *
from new import data
import matplotlib.pyplot as plt

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

fig, ax = plt.plot()