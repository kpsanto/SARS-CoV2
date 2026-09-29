## plot binding site distaances and contacts



import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
matplotlib.rcParams['axes.linewidth']=1.0
matplotlib.rcParams['lines.linewidth']=2.0

import numpy as np
import pandas as pd

# SBSA
bsa=np.loadtxt('bind_site_distD.dat')

ta=bsa[:,0]*5+10
distA=bsa[:,1]*0.1  # nm
distA_s=pd.Series(distA).rolling(window=50).mean()
distmax=np.max(distA)
print(distmax)
cont=np.loadtxt('contacts.dat')

tn=cont[:,0]*5+10
cn=cont[:,1]
cn_s=pd.Series(cn).rolling(window=50).mean()



fig,ax1=plt.subplots(figsize=(6,4))

ax1.plot(ta,distA,alpha=0.1, color='r')
ax1.plot(ta,distA_s, label='d$_{SBSD}$', color='r')


ax2=ax1.twinx()

ax2.plot(tn,cn, alpha=0.1, color='g')
ax2.plot(tn,cn_s, label='N$_{cont}$', color='g', linewidth=1.0)

lines1, labels1=ax1.get_legend_handles_labels()
lines2, labels2=ax2.get_legend_handles_labels()

ax1.legend(lines1+lines2, labels1+labels2, fontsize=15)


ax1.set_ylabel('d(nm)', fontsize=20)
ax2.set_ylabel('N$_{cont}$', fontsize=20)

ax1.set_xlabel('Time(ns)', fontsize=20)
ax1.tick_params(axis='x', labelsize=15)
ax1.tick_params(axis='y', labelsize=15)
ax2.tick_params(axis='y', labelsize=15)
ax1.set_xlim(0,3000)
ax1.set_ylim(0,14)
ax2.set_ylim(0,50)

plt.tight_layout()

plt.savefig('bindsite.png', dpi=600)




