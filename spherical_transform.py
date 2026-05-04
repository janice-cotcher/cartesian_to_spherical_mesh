import numpy as np
from spherical_utilities import *
from stl import mesh
import trimesh

file = "stl/corner.stl"
data = mesh.Mesh.from_file(file)

x = data.x
y = data.y
z = data.z

r, theta, phi = cartesian_to_spherical(x, y, z)
phi += np.deg2rad(135)
new_x, new_y, new_z = spherical_to_cartesian(r, theta, phi)
new_data = np.stack([new_x, new_y, new_z], axis=-1)
new_points, new_vertices, new_faces = mesh_components(new_data)
new_mesh = trimesh.Trimesh(vertices=new_vertices, faces=new_faces)
new_mesh.show()
