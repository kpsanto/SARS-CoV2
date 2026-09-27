### secondary structure analysis

import MDAnalysis as mda 
from MDAnalysis.analysis.dssp import DSSP
import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

plt.rcParams['axes.linewidth']=1.5
plt.rcParams['lines.linewidth']=1.5

import pandas as pd 


trj="../traj_Centered.xtc"
gro="../topology.pdb" 
u=mda.Universe(gro,trj)

protein=u.select_atoms("protein")

dssp=DSSP(protein).run()

ss=dssp.results.dssp

print(ss.shape)

## plots 


#print(ss)


ss_num = np.zeros(ss.shape, dtype=int)
ss_num[ss == 'H'] = 1
ss_num[ss == 'E'] = 2

# Residue IDs
resids = protein.residues.resids

# Time in microseconds
# MDAnalysis trajectory time is normally in ps
times = np.array([
    u.trajectory[i].time for i in range(len(u.trajectory))
]) / 2.0/100


# Plot
cmap = ListedColormap(["white", "green", "red"])

plt.figure(figsize=(8, 4))


plt.imshow(
    ss_num.T,
    aspect="auto",
    origin="lower",
    interpolation="nearest",
    extent=[times[0], times[-1], resids[0], resids[-1]],
    cmap=cmap,
    vmin=0,
    vmax=2
)

cbar = plt.colorbar(ticks=[0, 1, 2])
cbar.ax.set_yticklabels(["Coil", "Helix", "Beta"])

plt.xlabel("Time ($\\mu$s)", fontsize=15)
plt.ylabel("Residue",fontsize=15)
plt.tight_layout()

plt.savefig("secondary_structure.png", dpi=300)
plt.show()



Helix=np.sum(ss=='H',axis=1)/ss.shape[1]*100
sheet=np.sum(ss=='E',axis=1)/ss.shape[1]*100

total=np.add(Helix,sheet)
ssdata=np.column_stack((times,total))
np.savetxt('totalss.dat',  ssdata , delimiter='  ')

Helix_av=pd.Series(Helix).rolling(window=100, center=True).mean()
sheet_av=pd.Series(sheet).rolling(window=100, center=True).mean()

nres=ss.shape[1]*0.01

n=len(Helix)
Helixr=Helix*nres
H_ave=np.mean(Helixr)
H_dev=np.std(Helixr)
H_init=np.mean(Helixr[0:500])
H_fin=np.mean(Helixr[-500:n])
print('Average helix content:',H_ave, 'std:', H_dev)
print('Initial helix content:', H_init)
print('Final helix content:', H_fin)

DH=H_fin-H_init

print('Difference in Helix content:', DH)

sheetr=sheet*nres
S_ave=np.mean(sheetr)
S_dev=np.std(sheetr)
S_init=np.mean(sheetr[0:500])
S_fin=np.mean(sheetr[-500:n])
print('Average helix content:',S_ave,'std:',S_dev)
print('Initial helix content:', S_init)
print('Final helix content:', S_fin)

DS=S_fin-S_init

print('Difference in Sheet content:', DS)

Hdata=[H_ave, H_dev, DH]
Sdata=[S_ave, S_dev, DS]

ssave=np.array(np.column_stack((Hdata,Sdata)))

print(ssave)


np.savetxt('ssave.dat',  ssave , delimiter='  ')




plt.figure(figsize=(5,4))

plt.plot(times, Helix_av, color='green',label="Helix")
plt.plot(times, Helix, color='green', alpha=0.2)
plt.plot(times, sheet_av, color='red', label="Sheet")
plt.plot(times, sheet, color='red', alpha=0.2)

plt.xlabel(f'Time($\mu$s)', fontsize=15)
plt.ylabel(f'Secondary structure(%)',fontsize=15)

plt.xlim(0,2)
plt.ylim(0,50)


plt.legend(fontsize=15)
plt.tight_layout()

plt.savefig('ss.png', dpi=300)




