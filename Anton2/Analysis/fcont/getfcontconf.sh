# Create RBD -surfactant pdb file with fcont as bfactors 
# for visualization.

# load gromacs
#module use /projects/community/modulefiles
#module load gromacs/2021.6
f=../traj_Centered.xtc 
g=gmx_mpi # for mpi enabled , else gmx
tp=../md1.tpr 
t=398 # scaled final time 
prot=fr398.pdb # pdb file name with protein and sufactants only 
np=228
ns=5 # number of surfactants 


echo 16 | $g trjconv -f $f -s $tp -o $prot -n ../index.ndx   -dump $t -pbc mol
# make index file with protein_surfactant group (16 here)
awk 'NR>1' p.dat > ps
nr=$((np+ns))

echo $nr >ps.dat 
cat ps >> ps.dat 
echo '547   0' >>ps.dat  
echo '548   0' >>ps.dat  
echo '549   0' >>ps.dat  
echo '550   0' >>ps.dat  
echo '551   0' >>ps.dat  

$g editconf -f $prot -o rbdps.pdb -bf ps.dat  


