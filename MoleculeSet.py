import numpy as np
from Lattice import Lattice


class Molecule:

    __doc__ = """Molecule class contains all the methods required for a simple
                 representation of a water molecule in the lattice."""

    def __init__(self, location, mu=None):  
        self.location = location  # Insert vertex vector here?
        self.mu = mu  # Initialize with vector pointing in mu direction?
        self.nn = []  # List of nearest neighbours for Molecule

    def interation(self):  # Strength of interactions between Molecule objects.
        pass

    def align(self, vector):  # Align itself along a given lattice vector?
        pass


class MoleculeSet:

    def __init__(self, vertices):
        self.vertices = vertices
        self.moleculeset = self.generate_mset()

    '''Function to remove duplicate vertex vectors, avoiding >1 Molecule at each
       vertex in lattice. See: http://stackoverflow.com/a/16971224/6731049'''
    def unique_rows(self, data):
        uniq = np.unique(data.view(data.dtype.descr * data.shape[1]))
        return uniq.view(data.dtype).reshape(-1, data.shape[1])
    # Should the above be a static method? Only used once. Investigate later.

    def generate_mset(self):
        vertices = np.array(zip(self.vertices[0], 
                                self.vertices[1], 
                                self.vertices[2]))
        molecules = [Molecule(vertex) for vertex in self.unique_rows(vertices)]
        return molecules
