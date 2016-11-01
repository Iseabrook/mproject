import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


p = 6.2e-30  # Dipole moment of water molecule.
a = 275e-12  # Distance between Oxygen atoms along each bond.
au = 5.26e-11  # Atomic unit of length.
sqrt_3 = 1.73205  # Approximate sqrt(3) to identify duplicate rows correctly.


class Tile:

    __doc__ = """Tile class generates 6 vertices around a given origin.
                 Will form the eventual basis of the ice lattice.
                 a_1,2,3 are the (non-Bravais) unit lattice vectors of the
                 1H ice crystal."""

    # Define the vectors for the periodic lattice structure.
    a_1 = np.array([1,0,0])
    a_2 = np.array([0.5, 0.5*sqrt_3, 0])
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

class Molecule:

    __doc__ = """Molecule class contains all the methods required for a simple
                 representation of a water molecule in the lattice."""

    def __init__(self, location, mu=None):  
        self.location = location  # Insert vertex vector here?
        self.mu = mu  # Initialize with vector pointing in mu direction?

    def interation(self):  # Strength of interactions between Molecule objects.
        pass

    def align(self, vector):  # Align itself along a given lattice vector?
        pass

class Lattice(Tile):

    __doc__ = """Lattice class will generate a Tile for each origin. Number of
                 origins specified by the xdim & ydim arguments.
                 Lattice class can """

    def __init__(self, xdim, ydim, zdim):
        self.xdim = xdim
        self.ydim = ydim
        self.zdim = zdim
        self.grid = self.tessellate()  # Make grid upon instantiation.
        vals = self.generate_values()
        self.x_vals = vals[0]
        self.y_vals = vals[1]
        self.z_vals = vals[2]
        

    def tessellate(self):  # Generate an array of origins for tiles.
        origins = np.zeros(shape=(self.xdim, self.ydim, self.zdim, 3))

        for i in range(self.xdim):
            for j in range(self.ydim):
                for k in range(self.zdim):
                    origins[i, j, k] = i*(self.a_1 + self.a_2)    \
                                     + j*(-self.a_1 + 2*self.a_2) \
                                     + k*self.a_3
        return origins

    def get_vertices(self):  # Get all the vertices of points on grid.

        for i in range(self.xdim):
            for j in range(self.ydim):
                for k in range(self.zdim):
                    yield Tile(self.grid[i, j, k]).vertices

    def generate_values(self):  # Arrays of all x, y and z vertex positions.
        x_vals = np.array([])
        y_vals = np.array([])
        z_vals = np.array([])

        for vertices in self.get_vertices():
            x_vals = np.append(x_vals, vertices[:,0,])
            y_vals = np.append(y_vals, vertices[:,1,])
            z_vals = np.append(z_vals, vertices[:,2,])

        return np.array([x_vals, y_vals, z_vals])

    '''Function to remove duplicate vertex vectors, avoiding >1 Molecule at each
       vertex in lattice. See: http://stackoverflow.com/a/16971224/6731049'''
    def unique_rows(self, data):
        uniq = np.unique(data.view(data.dtype.descr * data.shape[1]))
        return uniq.view(data.dtype).reshape(-1, data.shape[1])
    # Should the above be a static method? Only used once. Investigate later.

    def populate(self):  #Generate list of Molecule objects; one at each vertex.
        vertices = np.array(zip(self.x_vals, self.y_vals, self.z_vals))
        molecules = [Molecule(vertex) for vertex in self.unique_rows(vertices)]
        return molecules

    def plot_lattice(self):  # Plot the lattice in 3D. Add 2D capacity as well?
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        plt.suptitle("1H ice lattice")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.scatter(self.x_vals, self.y_vals, self.z_vals)
        return plt.show()

if __name__ == "__main__":
    lattice = Lattice(3,3,1)
    #lattice.plot_lattice()
    print lattice.populate()
