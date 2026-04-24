# cartesian_to_spherical_mesh

3D mesh transformations using spherical coordinates.

## Prerequisites

- Python 3.8 or newer
- `pip` package manager
- Required Python packages:
  - `numpy`
  - `numpy-stl`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/janice-cotcher/cartesian_to_spherical_mesh.git
   cd cartesian_to_spherical_mesh
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install numpy numpy-stl
   ```

## Usage

Run the transformation script with the example STL file:

### Mac or Linux
```bash
python3 spherical_transform.py
```
### Windows
```bash
python spherical_transform.py
```

The script reads `stl/cube.stl`, converts mesh vertices between Cartesian and spherical coordinates, and saves a new STL file called `output.stl`.
