import mdtraj as md
import numpy as np


traj=md.load('traj_Centered.xtc', top='topology.pdb')

native=md.load('native.pdb')

# parameters 

cutoff=0.8
atom_selection='name CA'
min_seq_sep=4

# selct atoms 
atoms=native.topology.select(atom_selection)

pairs=[]

# define native contacts from a reference strucutre 

for i in range(len(atoms)):
    for j in range(i+min_seq_sep,len(atoms)):
        d=md.compute_distances(native,[[atoms[i], atoms[j]]])[0,0]
        if d<0.8:
            pairs.append([atoms[i], atoms[j]])

pairs=np.array(pairs)

# total native contacts 
N_native_ref=len(pairs)
print(f"Total native contacts in reference: {N_native_ref}")

# distances in trajctory  for native contacts 

distances=md.compute_distances(traj,pairs)
contact_counts=np.sum(distances < cutoff, axis=1)

# write ouput 

with open( 'native_contacts.dat', 'w') as f:
    f.write(f"# Total_native_contacts: {N_native_ref}\n")
    f.write("#Frame Native_contacts\n")

    for i, count in enumerate(contact_counts):
        f.write(f"{i} {count}\n")


print("Output written to native_contacts.dat")


