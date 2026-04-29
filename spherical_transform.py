import numpy as np
from spherical_utilities import *
from stl import mesh
import pandas as pd


file = "stl/corner.stl"
data = mesh.Mesh.from_file(file)

x = data.x
y = data.y
z = data.z

r, theta, phi = cartesian_to_spherical(x, y, z)

polarized = np.stack([r, theta, phi], axis=-1)


        
    



