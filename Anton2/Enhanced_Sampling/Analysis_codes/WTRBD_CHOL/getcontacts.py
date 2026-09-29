import MDAnalysis as mda
import numpy as np
from MDAnalysis.lib.distances import capped_distance

# Load system
u = mda.Universe("md1.tpr", "traj_Centered3.xtc")   # or gro/pdb + xtc

# Selections
protein = u.select_atoms("protein")
surf = u.select_atoms("resname CHL1")   #  surfactant 

cutoff = 5.0   # Angstrom; 0.6 nm = 6.0 A

times = []
n_res_contacts = []

for ts in u.trajectory:
    # find all atom pairs within cutoff
    pairs = capped_distance(
        protein.positions,
        surf.positions,
        max_cutoff=cutoff,
        box=u.dimensions,
        return_distances=False
    )
    if len(pairs) > 0:
        # protein atom indices involved in contacts
        prot_atom_idx = pairs[:, 0]

        # map atoms → residues
        contacting_resids = np.unique(protein[prot_atom_idx].resids)

        n_res_contacts.append(len(contacting_resids))
    else:
        n_res_contacts.append(0)

    times.append(ts.time)

# Convert
times = np.array(times)
n_res_contacts = np.array(n_res_contacts)

# Save
np.savetxt(
    "contacts.dat",
    np.column_stack((times, n_res_contacts))
)

print("Done")
