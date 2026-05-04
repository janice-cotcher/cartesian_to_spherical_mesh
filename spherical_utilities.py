import numpy as np
import trimesh

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

def get_vertices(points):
    unique_rows, indices = np.unique(points, axis=0, return_index=True)
    return unique_rows

def get_faces(vertices, points, rows):
    faces = np.zeros((rows), dtype="float64")
    for index in range(rows):
        try:
            match = np.where((vertices == points[index]).all(axis=1))
            faces[index] = match[0][0]
        except Exception as e:
            continue
    return np.reshape(faces, (16, 3))

def mesh_components(data):
    triangles = np.array(data)
    rows = triangles.size // 3
    points = np.reshape(triangles, (rows, 3))
    vertices = get_vertices(points)
    faces = get_faces(vertices, points, rows)

    return points, vertices, faces
