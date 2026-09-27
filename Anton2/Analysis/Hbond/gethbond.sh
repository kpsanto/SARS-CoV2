# Calculate hydrogen bonds using gmx hbond 

# load gromacs - specific to the computer/HPC used  
module use /projects/community/modulefiles
module load gromacs/2021.6
#
f=traj_Centered.xtc
tp=md1.tpr
b=200 # scaled time - 1 mus 
e=398 # scaled time -1990 ns 
function gethb {
n=$1
m=$2
echo $m 1 | gmx_mpi hbond -f ../$f -s ../$tp -n ../index.ndx -dist hbdist$n\.xvg  -num hbnum$n\.xvg   -b $b -e $e -hbn hbond$n\.ndx  
}

gethb chol 13 
#gethb 547 18 
#gethb 548 19 
#gethb 549 20 
#gethb 550 21 
#gethb 551 22
