# This simulation is for tempered binding run 2 
# The configuration is from the 4 us Anton simulation

f=drbdCH1.pdb
top=rbdchol.top
module purge 
module use /projects/community/modulefiles
module load gromacs/2021.6
g=gmx_mpi   # gromacs prefix 

ed=editconf
tr=trjconv
sol=solvate
gr=grompp
ge=genion

#define box
function defbox {
$g $ed -f $f -o rbdch.gro -box 12.5 12.5 12.5 -c 
}

#defbox 
 

# Solvate 

function solv {
$g $sol -cp rbdch.gro -cs spc216.gro -o solv.gro  -p $top 
}

#solv 

#Addions 
function addions {
#$g $gr -f ion.mdp -c solv.gro -p $top -o ions.tpr -maxwarn 2 
$g $ge -s ions.tpr -p $top -o system.gro -nname CLA -pname POT -neutral  
}

#addions


#------------------------
#Energy minimization
#


function min {
mdp=min.mdp
$g $gr -f $mdp -c system.gro -r system.gro -p $top -o min.tpr -maxwarn 1
}

#min

#---------------------------------------------------
# NVT equilbration 
function getndx {
	$g make_ndx -f min.gro -o index.ndx 
}
#getndx 

function  runnvt1 {
	$g grompp -f nvteq.mdp -c min.gro -r min.gro  -p $top -o nvt1.tpr -maxwarn 1
}
#runnvt1

#--------------------------------
#NPT equilibration  

function  runnpt1 {
	$g grompp -f npteq.mdp -c nvt1.gro -r nvt1.gro  -p $top -o npt1.tpr -maxwarn 1
}
#runnpt1

function  runnpt2 {
	$g grompp -f npteq2.mdp -c npt1.gro -r npt1.gro  -p $top -o npt2.tpr -maxwarn 1
}

#runnpt2 

#Production run 10 ns  
function  md1 {
	$g grompp -f md1.mdp -c npt2.gro   -p $top -o md1.tpr -maxwarn 1
}
md1










 

