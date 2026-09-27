# Get residues in contact with surfactant as a function of time 

#------------------------------


# Loading gromacs in cluster
#module use /projects/community/modulefiles 
#module load gromacs/2021.6

f=../traj_Centered.xtc # anton2  trajectory  
g=gmx # gmx_mpi for mpi enabled 
tp=../md1.tpr 
rag=0.6  # distance for contact 
n=198 # number of frames / scaled time to be analysed 

echo ' ' > contres.dat 
echo '  ' > ncontres.dat 
for ((i=1;i<=$n;i++))
do
j=$((i+200)) # skip intial frames of 1 mu s 
echo  1 13 | $g mindist -f $f -s $tp -n ../index.ndx  -group -on  -o -or  -b $j -e $j
# group 1 is protein, 13- surfactant 
awk '!/@/&& !/#/' mindistres.xvg >mindres.dat 
awk '$2<'$rag' {print $1}' mindres.dat > contres
awk 'END{print NR}' contres > nc
nc=`cat nc`
echo $j '  '$nc >> ncontres.dat # number of contact residues vs tim  
cat contres >> contres.dat  # stores contact residues from all times 
rm \#*
done 

rm nc contres 
