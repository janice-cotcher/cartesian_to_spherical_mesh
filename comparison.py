import numpy as np
from stl import mesh
from spherical_utilities import *
from new import data
import matplotlib.pyplot as plt
# import plotly
# import trimesh
# from scipy.spatial import Delaunay

triangles = np.array(data)

points = [(point for point in triangle) for triangle in triangles]
print(points)
# x = []
# y = []
# z = []
# for triangle in data:
#     triangles.append(triangle)
#     for point in triangle:
#         points.append(point)
#         x.append(point[0])
#         y.append(point[1])
#         z.append(point[2])
# x = np.array(x)
# y = np.array(y)
# z = np.array(z)
# r,theta,phi = cartesian_to_spherical(x,y,z)
# new_phi = phi + np.deg2rad(45)
# new_x, new_y, new_z = spherical_to_cartesian(r, theta, new_phi)
# old_mesh = np.stack([x,y,z], axis=-1)
# new_mesh = np.stack([new_x, new_y, new_z], axis=-1)


# X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
# New_x, New_y, New_z = np.meshgrid(new_x, new_y, new_z)
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.plot_surface(x, y, z)
# ax.set_aspect('equal')

# plt.show()
# # ax2 = fig.add_subplot(111, projection='3d')
# # ax2.plot(new_x, new_y, new_z)

# plt.savefig("comparison.png")

# Flatten data for processing
# points = np.vstack((x.flatten(), y.flatten(), z.flatten())).T

# # 2. Triangulate the 2D grid points (X, Y)
# points2d = np.vstack((x.flatten(), y.flatten())).T
# tri = Delaunay(points2d)

# # 3. Create the mesh
# mesh = trimesh.Trimesh(vertices=points, faces=tri.simplices)

# # 4. Export to STL
# mesh.export("surface.stl")