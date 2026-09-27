# Calculates fcont( pcont)  from contres.dat  


#
module use /projects/community/modulefiles # specific to Rutgers cluster 
module load gromacs/2021.6
f=../traj_Centered.xtc 
g=gmx_mpi
tp=../md1.tpr 
prot=../rbd399.pdb 


nr=228  # number of residues 
nf=198 # number of frames analysed
f=contres.dat  # contains contact residues from $nf times  
res0=318

echo $nr >p.dat 
for (( i=1; i<=$nr;i++))
do
awk '$1=='$i'' $f >ires
awk 'END{print NR}' ires > nres  
nres=`cat nres`
echo 'n='$nres'.0' > p.py 
echo 'nf='$nf >> p.py
echo  'p=n/nf' >> p.py
echo  'print(p)' >> p.py

python p.py > p
p=`cat p`

echo $((i+res0)) ' ' $p >> p.dat 
done
awk 'NR>1' p.dat > pcont.dat  # fcont data  
   
$g editconf -f $prot -o rbdp.pdb -bf p.dat  # makes the bfactor pdb file of RBD based on fcont

