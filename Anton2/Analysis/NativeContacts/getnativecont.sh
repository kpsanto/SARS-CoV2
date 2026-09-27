# Get native contacts 

module use /projects/community/modulefiles
module load gromacs/2021.6
f=traj_Centered.xtc
#f1=traj.trr
g=gmx_mpi
tp=md1.tpr

echo 0 | $g trjconv -f $f -s $tp -o topology.pdb -dump 0 
echo 1 | $g trjconv -f npt2.xtc -s npt2.tpr  -o native.pdb -dump 0 

python NativeContacts.py 

