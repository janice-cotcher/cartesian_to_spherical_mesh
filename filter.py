import numpy as np
from spherical_convert import *
from stl import mesh


def filter_by_phi(data, phi):

    # filter by a specific phi, angle between the positive z-axis and the radial vector
    phi_vals = data[:, :, 2]
    mask   = np.isclose(phi_vals, phi)
    return data[mask]

def filer_by_theta(data, theta):
    # filter by a specific theta, angle of rotation in the xy-plane
    theta_vals = data[:,:,1]
    mask = np.isclose(theta_vals, theta)