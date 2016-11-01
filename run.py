from Lattice import Lattice
from MoleculeSet import MoleculeSet

if __name__ == "__main__":
    lattice = Lattice(3,3,1)
    #lattice.plot_lattice()
    mset = MoleculeSet(lattice.vertices)
    print mset.moleculeset[0].location
