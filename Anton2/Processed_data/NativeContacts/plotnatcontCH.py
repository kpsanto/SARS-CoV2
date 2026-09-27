# # Native contacts 


import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
matplotlib.rcParams['axes.linewidth']=1.5
matplotlib.rcParams['lines.linewidth']=2.0

import numpy as np
import pandas as pd

# WT
plt.figure(figsize=(5,4))

nc=np.loadtxt('./WT/CHOL/native_contacts.dat', comments=['#'])
t=nc[:,0]*0.5+10
ncont=nc[:,1]
ncont_s=pd.Series(ncont).rolling(window=50).mean()

plt.plot(t,ncont, alpha=0.2, color='r')
plt.plot(t,ncont_s, label="WT", color='r')

# Delta

nc=np.loadtxt('./Delta/CHOL/native_contacts.dat', comments=['#'])
t=nc[:,0]*0.5+10
ncont=nc[:,1]
ncont_s=pd.Series(ncont).rolling(window=50).mean()

plt.plot(t,ncont, alpha=0.2, color='b')
plt.plot(t,ncont_s, label="Delta", color='b')

# omicron

nc=np.loadtxt('./Omicron/CHOL/native_contacts.dat', comments=['#'])
t=nc[:,0]*0.5+10
ncont=nc[:,1]
ncont_s=pd.Series(ncont).rolling(window=50).mean()

plt.plot(t,ncont, alpha=0.2, color='g')
plt.plot(t,ncont_s, label="Omicron", color='g')



plt.xlabel('Time(ns)', fontsize=15)
plt.ylabel('No of Native Contacts', fontsize=15)
plt.xlim(0,2010)
plt.ylim(200,550)
plt.xticks([0, 500, 1000, 1500,2000],fontsize=15)
plt.yticks([200,300,400,500],fontsize=15)

plt.legend(fontsize=15)

plt.tight_layout()


plt.savefig('natcontCH.png', dpi=600)







