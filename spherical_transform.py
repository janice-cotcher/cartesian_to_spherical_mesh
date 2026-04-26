import numpy as np
from spherical_convert import *
from stl import mesh

file = "stl/corner.stl"
file2 = "stl/cube.stl"
data = mesh.Mesh.from_file(file)
data2 = mesh.Mesh.from_file(file2)

x = data.x
y = data.y
z = data.z
x2 = data2.x
y2 = data2.y
z2 = data2.z
# polarize points — shape (N_triangles, 3, 3): [triangle, vertex, r/theta/phi]
r, theta, phi = cartesian_to_spherical(x, y, z)
r2, theta2, phi2 = cartesian_to_spherical(x2, y2, z2)

polarized = np.stack([r, theta, phi], axis=-1)
polarized2 = np.stack([r2, theta2, phi2], axis=-1)
print(polarized-polarized2)







# convert back to Cartesian
# new_r     = polarized[:, :, 0]
# new_theta = polarized[:, :, 1]
# new_phi   = polarized[:, :, 2]

# new_x, new_y, new_z = spherical_to_cartesian(new_r, new_theta, new_phi)

# # save the stl file
# new_mesh = mesh.Mesh(np.zeros(N, dtype=mesh.Mesh.dtype))
# new_mesh.vectors = np.stack([new_x, new_y, new_z], axis=-1)
# new_mesh.save('output.stl')
