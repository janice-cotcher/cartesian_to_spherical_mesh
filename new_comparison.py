import numpy as np
# from stl import mesh
from spherical_utilities import *
from new import data
import trimesh


points, vertices, faces = mesh_components(data)
mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
mesh.show()
# Slicing: array[row_start:row_end, column_index]
# x = points[:,0]
# y = points[:,1]
# z = points[:,2]

# r, theta, phi = cartesian_to_spherical(x, y, z)
# phi += np.deg2rad(45)
# new_x, new_y, new_z = spherical_to_cartesian(r, theta, phi)
# new_data = np.stack([new_x, new_y, new_z], axis=-1)
# new_points, new_vertices, new_faces = mesh_components(new_data)
# new_mesh = trimesh.Trimesh(vertices=new_vertices, faces=new_faces)
# new_mesh.show()