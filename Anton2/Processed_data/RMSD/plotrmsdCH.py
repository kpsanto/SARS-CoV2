# plot rmsd

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['axes.linewidth']=1.5
matplotlib.rcParams['lines.linewidth']=2.0

import pandas as pd


#WT

plt.figure(figsize=(5,4))

rmsch=np.loadtxt('./WT/CHOL/rmsd_chol.xvg',comments=['#', '@'])

t=rmsch[:,0]*5000+10
r=rmsch[:,1]
r_s=pd.Series(r).rolling(window=50).mean()

plt.plot(t,r, alpha=0.2, color='r')
plt.plot(t,r_s, color='r', label="WT")

# Delta
rmschd=np.loadtxt('./Delta/CHOL/rmsd_chol.xvg',comments=['#', '@'])

td=rmschd[:,0]*5000+10
rd=rmschd[:,1]
rd_s=pd.Series(rd).rolling(window=50).mean()

plt.plot(td,rd, alpha=0.2, color='b')
plt.plot(td,rd_s, color='b', label="Delta")


# Omicron

rmscho=np.loadtxt('./Omicron/CHOL/rmsd_chol.xvg',comments=['#', '@'])

to=rmscho[:,0]*5000+10
ro=rmscho[:,1]
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

plt.savefig('rmsdch.png', dpi=600)



## DPPC

