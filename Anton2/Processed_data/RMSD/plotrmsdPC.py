# plot rmsd

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
matplotlib.rcParams['axes.linewidth']=1.5
matplotlib.rcParams['lines.linewidth']=2.0
import numpy as np

import pandas as pd


#WT


plt.figure(figsize=(5,4))
rmspc=np.loadtxt('./WT/DPPC/rmsd_dppc.xvg',comments=['#', '@'])

t=rmspc[:,0]*5000+10
r=rmspc[:,1]
r_s=pd.Series(r).rolling(window=50).mean()

plt.plot(t,r, alpha=0.2, color='r')
plt.plot(t,r_s, color='r', label="WT")

# WT 2
rmspc2=np.loadtxt('./WT/DPPC2/rmsd_dppc.xvg',comments=['#', '@'])

t2=rmspc2[:,0]*5000+10
r2=rmspc2[:,1]
r2_s=pd.Series(r2).rolling(window=50).mean()

plt.plot(t2,r2, alpha=0.2, color='c')
plt.plot(t2,r2_s, color='c', label="WT run 2")



# Delta
rmspcd=np.loadtxt('./Delta/DPPC/rmsd_dppc.xvg',comments=['#', '@'])

td=rmspcd[:,0]*5000+10
rd=rmspcd[:,1]
rd_s=pd.Series(rd).rolling(window=50).mean()

plt.plot(td,rd, alpha=0.2, color='b')
plt.plot(td,rd_s, color='b', label="Delta")


# Omicron

rmspco=np.loadtxt('./Omicron/DPPC/rmsd_dppc.xvg',comments=['#', '@'])

to=rmspco[:,0]*5000+10
ro=rmspco[:,1]
ro_s=pd.Series(ro).rolling(window=50).mean()

plt.plot(to,ro, alpha=0.2, color='g')
plt.plot(to,ro_s, color='g', label="Omicron")




plt.xlabel('Time(ns)', fontsize=15)
plt.ylabel('RMSD(nm)', fontsize=15)
plt.xlim(0,2010)
plt.ylim(0,2.0)
plt.xticks([0, 500,1000,1500,2000],fontsize=15)
plt.yticks([0., 0.5,1.0, 1.5, 2.0],fontsize=15)

plt.legend(fontsize=15)
plt.tight_layout()

plt.savefig('rmsdpc.png', dpi=600)



## DPPC

