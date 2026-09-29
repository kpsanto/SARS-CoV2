# bind E vs contact distance 


import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
matplotlib.rcParams['axes.linewidth']=2.5
matplotlib.rcParams['lines.linewidth']=2.5

import numpy as np
import pandas as pd

plt.figure(figsize=(5,4))

be=np.loadtxt('./trajC/IE_Normal_PB_Delta_TOTAL.csv', delimiter=',', skiprows=1)

#t=be[:,0]*1+510
E=be[:,1]
E_s=pd.Series(E).rolling(window=10).mean()

r=np.loadtxt('bind_site_distC1.dat')

#t1=r[:,0]*0.2+10
rc=r[:,1]
rc_s=pd.Series(rc).rolling(window=10).mean()

rcE=np.column_stack((rc,E))
rcEsort=rcE[rcE[:,0].argsort()]

rc1=rcEsort[:,0]*.1
E1=rcEsort[:,1]
E1_s=pd.Series(E1).rolling(window=2).mean()

mask=rc1<1.21
E11=E1_s[mask]
print(np.mean(E11))
print(np.std(E11))

mask=rc1<0.61
E11=E1_s[mask]
print(np.mean(E11))
print(np.std(E11))

plt.plot(rc1, E1, alpha=0.8,color='blue')
#plt.plot(rc1, E1_s,color='purple')
plt.xlim(0,4)

plt.xlabel('$d_{SBSC}$(nm)', fontsize=20)
plt.ylabel('$\Delta$ H(Kcal/mol)', fontsize=20)

plt.tight_layout()

#plt.legend(fontsize=15)
plt.savefig('beA1000_1300ns.png')
