#plot hbonds 


import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
matplotlib.rcParams['axes.linewidth']=1.0
matplotlib.rcParams['lines.linewidth']=2.0
import numpy as np

import pandas as pd

#WT
hmchol=[]
hbonds=np.loadtxt('./WT/CHOL/hbnumchol.xvg',comments=['#', '@'])

t=hbonds[:,0]*5
h=hbonds[:,1]

hmean=np.mean(h)
hmchol.append(hmean)

hbondsd=np.loadtxt('./Delta/CHOL/hbnumchol.xvg',comments=['#', '@'])

td=hbondsd[:,0]*5

hd=hbondsd[:,1]

hmeand=np.mean(hd)
hmchol.append(hmeand)

hbondso=np.loadtxt('./Omicron/CHOL/hbnumchol.xvg',comments=['#', '@'])

to=hbondso[:,0]*5

ho=hbondso[:,1]

hmeano=np.mean(ho)
hmchol.append(hmeano)

print(hmchol)



#DPPC
hmdppc=[]
hbondspc=np.loadtxt('./WT/DPPC/hbnumdppc.xvg',comments=['#', '@'])
tpc=hbondspc[:,0]*5
hpc=hbondspc[:,1]
hmeanpc=np.mean(hpc)

hbondspc2=np.loadtxt('./WT/DPPC2/hbnumdppc.xvg',comments=['#', '@'])

tpc2=hbondspc2[:,0]*5
hpc2=hbondspc2[:,1]
hmeanpc2=np.mean(hpc2)
hmeanWT=0.5*(hmeanpc+hmeanpc2)
hmdppc.append(hmeanWT)

hbondspcd=np.loadtxt('./Delta/DPPC/hbnumdppc.xvg',comments=['#', '@'])
tpcd=hbondspcd[:,0]*5
hpcd=hbondspcd[:,1]
hmeanpcd=np.mean(hpcd)
hmdppc.append(hmeanpcd)

hbondspco=np.loadtxt('./Omicron/DPPC/hbnumdppc.xvg',comments=['#', '@'])
tpco=hbondspco[:,0]*5
hpco=hbondspco[:,1]
hmeanpco=np.mean(hpco)
hmdppc.append(hmeanpco)

print(hmdppc)




#POPG
hmpopg=[]
hbondspg=np.loadtxt('./WT/POPG/hbnumpopg.xvg',comments=['#', '@'])
tpg=hbondspg[:,0]*5
hpg=hbondspg[:,1]
hmeanpg=np.mean(hpg)

hbondspg2=np.loadtxt('./WT/POPG2/hbnumpopg.xvg',comments=['#', '@'])

tpg2=hbondspg2[:,0]*5
hpg2=hbondspg2[:,1]
hmeanpg2=np.mean(hpg2)
hmeanWT=0.5*(hmeanpg+hmeanpg2)
hmpopg.append(hmeanWT)


hbondspgd=np.loadtxt('./Delta/POPG/hbnumpopg.xvg',comments=['#', '@'])
tpgd=hbondspgd[:,0]*5
hpgd=hbondspgd[:,1]
hmeanpgd=np.mean(hpgd)
hmpopg.append(hmeanpgd)

hbondspgo=np.loadtxt('./Omicron/POPG/hbnumpopg.xvg',comments=['#', '@'])
tpgo=hbondspgo[:,0]*5
hpgo=hbondspgo[:,1]
hmeanpgo=np.mean(hpgo)
hmpopg.append(hmeanpgo)

print(hmpopg)






plt.figure(figsize=(6.5,5.7))

rbd=['WT', 'Delta', 'Omicron']

#rbd=['WT','WT2', 'Delta', 'Omicron']

x=np.arange(len(rbd))
w=0.5
w2=0.25
plt.bar(x-w/3, hmchol, w2, label='CHOL')
plt.bar(x, hmdppc, w2 , label='DPPC')
plt.bar(x+w/3, hmpopg, w2 , label='POPG')
#plt.xlabel(fontsize=20)
plt.ylabel('Average H-bonds', color='b', fontsize=20)



plt.yticks(fontsize=20)
plt.xticks(x,rbd, color='r',fontsize=20)

plt.legend(fontsize=20)

plt.savefig('hmean.png', dpi=600)



