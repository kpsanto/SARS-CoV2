#

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
matplotlib.rcParams['axes.linewidth']=1.0
matplotlib.rcParams['lines.linewidth']=2.0

import numpy as np
import pandas as pd

# WT

plt.figure(figsize=(5,4))

nsurf=np.loadtxt('./WT/POPG/nsurfcont.dat')

t=nsurf[:,0]*5+10
ns=nsurf[:,1]
ns_s=pd.Series(ns).rolling(window=50).mean()

plt.plot(t,ns, alpha=0.2, color='r')
plt.plot(t,ns_s, label="WT", color='r')

ns_wt=np.mean(ns[3000:4000])
ns_wt_std=np.std(ns[3000:4000])
print(ns_wt)
print(ns_wt_std)

# WT 2
nsurf=np.loadtxt('./WT/POPG2/nsurfcont.dat')

t=nsurf[:,0]*5+10
ns=nsurf[:,1]
ns_s=pd.Series(ns).rolling(window=50).mean()

plt.plot(t,ns, alpha=0.2, color='c')
plt.plot(t,ns_s, label="WT run 2", color='c')

ns_wt2=np.mean(ns[3000:4000])
ns_wt2_std=np.std(ns[3000:4000])
print(ns_wt2)
print(ns_wt2_std)

# Delta

nsurf=np.loadtxt('./Delta/POPG/nsurfcont.dat')

t=nsurf[:,0]*5+10
ns=nsurf[:,1]
ns_s=pd.Series(ns).rolling(window=50).mean()

plt.plot(t,ns, alpha=0.2, color='b')
plt.plot(t,ns_s, label="Delta", color='b')

ns_dl=np.mean(ns[3000:4000])
ns_dl_std=np.std(ns[3000:4000])
print(ns_dl)
print(ns_dl_std)

# Omicron

nsurf=np.loadtxt('./Omicron/POPG/nsurfcont.dat')

t=nsurf[:,0]*5+10
ns=nsurf[:,1]
ns_s=pd.Series(ns).rolling(window=50).mean()

plt.plot(t,ns, alpha=0.2, color='g')
plt.plot(t,ns_s, label="Omicron", color='g')

ns_om=np.mean(ns[3000:4000])
ns_om_std=np.std(ns[3000:4000])
print(ns_om)
print(ns_om_std)


plt.xlabel('Time(ns)', fontsize=15)
plt.ylabel('No of Adsorbed Surfactants', fontsize=15)
plt.xlim(0,2010)
plt.ylim(0,5.5)
plt.xticks([0,500,1000,1500,2000],fontsize=15)
plt.yticks(fontsize=15)

plt.legend(fontsize=15)
plt.tight_layout()


plt.savefig('nsurfPG.png', dpi=600)




