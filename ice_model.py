import numpy as np
import matplotlib.pyplot as plt


p = 6.2e-30  # Dipole moment of water molecule.
a = 275e-12  # Distance between Oxygen atoms along each bond.
au = 5.26e-11  # Atomic unit of length.


class Tile:

    __doc__ = """Tile class generates 6 vertices around a given origin.
                 Will form the eventual basis of the ice lattice.
                 a_1,2,3 are the (non-Bravais) unit lattice vectors of the
                 1H ice crystal."""

    # Define the vectors for the periodic lattice structure.
    a_1 = np.array([1,0,0])
    a_2 = np.array([0.5, 0.5*np.sqrt(3), 0])
    a_3 = np.array([0, 0, 1])

    def __init__(self, origin=np.array([0, 0, 0])):
        self.origin = origin
        # Define location of vertices in clockwise fashion about origin.
        self.vertices = np.array((self.origin + self.a_2,
                                  self.origin + self.a_1,
                                  self.origin + self.a_1 - self.a_2,
                                  self.origin - self.a_2,
                                  self.origin - self.a_1,
                                  self.origin - self.a_1 + self.a_2))


class Lattice(Tile):

    __doc__ = """Lattice class will generate a Tile for each origin. No. origins
                 specified by the xdim & ydim arguments."""

    def __init__(self, xdim, ydim, zdim=None):
        self.xdim = xdim
        self.ydim = ydim
        self.zdim = zdim               # Restrict to 2D for now.
        self.grid = self.tessellate()  # Make grid upon instantiation.

    def tessellate(self):
        # Generate an array of origins for tiles. Nominally 3D at the moment.
        origins = np.zeros(shape=(self.xdim, self.ydim, 3))

        for i in range(self.xdim):
            for j in range(self.ydim):
                origins[i, j, ] = i*(self.a_1 + self.a_2)    + \
                                  j*(-self.a_1 + 2*self.a_2)
        
        return origins

    def get_vertices(self):  # Get all the vertices of points on grid.

        for i in range(self.xdim):
            for j in range(self.ydim):
                yield Tile(self.grid[i, j, ]).vertices

    def plot_lattice(self):  # Plot the lattice in the z=0 plane. 
        x_vals = np.array([])
        y_vals = np.array([])
        
        for vertices in self.get_vertices():
            x_vals = np.append(x_vals, vertices[:,0,])
            y_vals = np.append(y_vals, vertices[:,1,])
        
        plt.scatter(x_vals, y_vals)
        plt.show()

"""for vertex in a.vertices:
      if vertex in b.vertices:
        intercept = True"""

if __name__ == "__main__":
    lattice = Lattice(5,5)
    lattice.plot_lattice()
