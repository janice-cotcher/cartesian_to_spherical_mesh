import numpy as np

def cartesian_to_spherical(x, y, z):
    hypotenuse2d = np.hypot(x, y)
    # Calculate radius (r)
    r = np.hypot(hypotenuse2d, z)

    # Calculate azimuth angle (theta) in radians [-pi, pi]
    theta = np.arctan2(y, x)

    # Calculate inclination angle (phi) from the z-axis [0, pi]
    # Use hypot(x, y) to get the distance in the xy plane
    phi = np.arctan2(hypotenuse2d, z)


    return r, theta, phi


def spherical_to_cartesian(r, theta, phi):
    r_2D_phi =  r * np.sin(phi)
    x = r_2D_phi * np.cos(theta)
    y = r_2D_phi  * np.sin(theta)
    z = r * np.cos(phi)
    return x, y, z


def get_overhang(phi):
    """
    Calculates the unit normal vector for given spherical angles.
    phi: polar angle (0 to pi)
    """
    return phi > np.deg2rad(135)
