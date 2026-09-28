## RMSF

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
matplotlib.rcParams['axes.linewidth']=1.5
matplotlib.rcParams['lines.linewidth']=2.0
import numpy as np

import pandas as pd

#WT

plt.figure(figsize=(5,4))

rmsfch=np.loadtxt('./WT/DPPC/rmsf1.xvg',comments=['#', '@'])

res=rmsfch[:,0]
r=rmsfch[:,1]
plt.plot(res,r, color='r', label="WT")

rmsfch2=np.loadtxt('./WT/DPPC2/rmsf1.xvg',comments=['#', '@'])

res2=rmsfch2[:,0]
r2=rmsfch2[:,1]
plt.plot(res2,r2, color='c', label="WT run 2")



# Delta
rmschd=np.loadtxt('./Delta/DPPC/rmsf1.xvg',comments=['#', '@'])

resd=rmschd[:,0]
rd=rmschd[:,1]
plt.plot(resd,rd, color='b', label="Delta")


# Omicron
rmscho=np.loadtxt('./Omicron/DPPC/rmsf1.xvg',comments=['#', '@'])

reso=rmscho[:,0]
ro=rmscho[:,1]
plt.plot(reso,ro, color='g', label="Omicron")

plt.xlabel('Residue Index', fontsize=15)
plt.ylabel('RMSF(nm)', fontsize=15)
plt.xlim(319,546)
plt.ylim(0,2.0)
plt.xticks([350,400,450,500],fontsize=15)
plt.yticks([0, 0.5,1.0, 1.5,2,0],fontsize=15)


plt.legend(fontsize=15)
plt.tight_layout()


plt.savefig('rmsfpc.png', dpi=600)


