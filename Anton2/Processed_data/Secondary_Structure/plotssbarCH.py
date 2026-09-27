# secondary struture analysis 
# for anton 2 trajectories 

#
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

plt.rcParams['axes.linewidth']=1.5
plt.rcParams['lines.linewidth']=1.5

variants = ['WT', 'Delta', 'Omicron']
n_residues=228
percent=100/n_residues
print(percent)
wtdata=np.loadtxt('./WT/CHOL/ssave.dat')

helix_wt=wtdata[0,0]
helixstd_wt=wtdata[1,0]
deltahelix_wt=wtdata[2,0]

sheet_wt=wtdata[0,1]
sheetstd_wt=wtdata[1,1]
deltasheet_wt=wtdata[2,1]


deltadata=np.loadtxt('./Delta/CHOL/ssave.dat')

helix_delta=deltadata[0,0]
helixstd_delta=deltadata[1,0]
deltahelix_delta=deltadata[2,0]

sheet_delta=deltadata[0,1]
sheetstd_delta=deltadata[1,1]
deltasheet_delta=deltadata[2,1]

omdata=np.loadtxt('./Omicron/CHOL/ssave.dat')

helix_om=omdata[0,0]
helixstd_om=omdata[1,0]
deltahelix_om=omdata[2,0]

sheet_om=omdata[0,1]
sheetstd_om=omdata[1,1]
deltasheet_om=omdata[2,1]

Hmean=np.array([helix_wt, helix_delta, helix_om])*percent 
Hstd=np.array([helixstd_wt, helixstd_delta, helixstd_om])*percent 
Hdiff=np.array([deltahelix_wt, deltahelix_delta, deltahelix_om])*percent 

Smean=np.array([sheet_wt, sheet_delta, sheet_om])*percent
Sstd=np.array([sheetstd_wt, sheetstd_delta, sheetstd_om])*percent
Sdiff=np.array([deltasheet_wt, deltasheet_delta, deltasheet_om])*percent



# plots 

x=np.arange(len(variants))
width=0.3

fig,ax=plt.subplots(figsize=(5,4))


ax.bar(x-width/2, Hmean, width, alpha=0.5, color='green', yerr=Hstd,label='Helix')
ax.bar(x-width/2, Hdiff, width-0.1, color='blue',label='$\Delta$ Helix')
ax.bar(x+width/2, Smean, width, alpha=0.5, color='orange', yerr=Sstd,label='Sheet')
ax.bar(x+width/2, Sdiff, width-0.1, color='red',label='$\Delta $ Sheet')

ax.set_xticks(x)
ax.set_xticklabels(variants)
ax.tick_params(axis='x',labelsize=15)

ax.legend(frameon=False, ncol=2, fontsize=15)

ax.set_ylim(-10,50)
ax.spines['bottom'].set_position(('data',0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


plt.ylabel('SS content (%)', fontsize=15)


plt.tight_layout()
plt.savefig('CHOLss.png', dpi=600)





