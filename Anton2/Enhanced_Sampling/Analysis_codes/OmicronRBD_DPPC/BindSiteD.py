# Binding analysis

import MDAnalysis as mda
from MDAnalysis.analysis import distances 
from MDAnalysis.analysis.distances  import distance_array
import numpy as np
from collections import defaultdict

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd

#------------------------------
# load trjactory 


u=mda.Universe("md1.gro", "md1.xtc")

protein=u.select_atoms("protein")

dppc=u.select_atoms("resname DPPC and not name H*")

#print(dppc)
#print(protein)

if len(dppc)==0:
    raise ValueError(" No dppc atoms found.")


cutoff=5.0

residue_contact_counts=defaultdict(int)
n_frames=0

for ts in u.trajectory:
     n_frames+=1
     
     contacting_atoms=u.select_atoms(f"protein and around { cutoff } group dppc", dppc=dppc)
     #print(contacting_atoms)

     contacting_residues= contacting_atoms.residues
 
     for res in contacting_residues:
         key = (res.resid, res.resname)
         residue_contact_counts[key] += 1

# identifying residues with occupancy >=0.6

print("Residues with occupancy >=0.6")

site_residues =[]
sorted_contacts=sorted (
     residue_contact_counts.items(),
     key= lambda x: x[1],
     reverse=True
)

for (resid, resname), count in sorted_contacts:
     occupancy =count/n_frames
     if occupancy >=0.6:
         site_residues.append((resid,resname))
         print(f"{resid:5d} {resname:>6s} {count:6d} {occupancy:8.3f}")


# The  intial binding site

resid_list= [resid for resid, resname in site_residues]

site_sel= "protein and not name H* and resid " +" ".join(str(r) for r in resid_list)
binding_site=u.select_atoms(site_sel)

#print(binding_site)
#print(binding_site.residues)

## Calculation of COM distances 

times=[]
distances=[]

for ts in u.trajectory:
    dppc_com=dppc.center_of_mass()
    site_com=binding_site.center_of_mass()
    #print(dppc_com)
    d=np.linalg.norm(dppc_com-site_com)

    times.append(ts.time)
    distances.append(d)


dist_data=np.column_stack((times, distances))
np.savetxt("bind_site_dist0.dat", dist_data)


# Calcualte on the extented trajectory 

u_ext=mda.Universe("md1.gro", "traj_Centered1.xtc")
dppc=u_ext.select_atoms("resname DPPC and not name H*")

site_sel="protein and not name H* and resid " + " ".join(str(r) for r in resid_list)
binding_site=u_ext.select_atoms(site_sel)

#print(binding_site.residues)

time=[]
distance=[]

for ts in u_ext.trajectory[0:6000:20]:
     dppc_com=dppc.center_of_mass()
     site_com=binding_site.center_of_mass()
     

     d=np.linalg.norm(dppc_com-site_com)
     time.append(ts.time)
     distance.append(d)

dist_data=np.column_stack((time, distance))
np.savetxt("bind_site_dist1.dat", dist_data)

print('Distance data is saved to bind_site_dist.dat')



