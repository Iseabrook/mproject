# mproject
Repository storing code written during final year MSci project, "Electric Fields in Controlled Freezing". 

## Current Task:
Investigate pertubations to water molecules in 1H ice under influence of (weak) external electric field. 

### To be Implemented:

- ~~Generate single hexagonal tile, where vertices represent locations of water molecules.~~
- ~~Have method for generating tessellating structures.~~
- ~~Generalise current 2D configuration to 3D.~~
- ~~Have tiles know when their vertices intercept (this will avoid placing multiple molecules at each vertex).~~
- ~~Add a blob (a 'dummy' `Molecule` - characterstics to be added later) at each vertex in the lattice.~~
- ~~Find out where dipoles point in 1H ice.~~ -> They all cancel due to symmetry.
- Have `Molecule` objects identify nearest neighbours for subsequent interactions.
- Implement Pauling's two rules for bonding in ice?
- Inlcude required molecule characteristics in `Molecule`.
- Add correct scales to `Tile` vectors (investigate meaning of a/c ratio).
- Include strength of dipole interactions.
- Include effect of weak electric field.
- Measure resulting polarizations and rotational perturbations.
- Sanity check results.

### Possible Implementations:
- Add in thermal fluctuations - impose Boltzmann distrbution on orientations. 
- Consider thermal expansion of lattice. 
- Include optional molecular defects.
