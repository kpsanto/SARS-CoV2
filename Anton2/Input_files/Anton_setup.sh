# Atomistic systems for Anton 2 
# kp santo
#
##############################
#  RBD CHOL systems 
# original spike RBD by I-TASSER
##
## charmm 36m force field, created by charmm gui builder 
##
module use /projects/community/modulefiles
module load gromacs/2021.6
g=gmx_mpi # gromacs prefix 

fp=drbd_charm.pdb    # Delta RBD file
sf=chol.pdb        # surfactant file (CHOL)
top=rbdchol.top  # topology file 
# system size as per the proposal
L=15.0            # nm  all dimensions 
cL=7.5 	          # RBD placed in the center 
#----------------------------------------
# Place RBD in the center and add 5 surfactant at random positions 
#
#
function make_prot_surf {
       $g  editconf -f $fp -o rbd.gro -box $L $L $L -center $cL $cL $cL 
       $g  editconf -f $sf -o surf.gro -box 4.0 4.0 4.0  -center 2.0 2.0 2
       $g  insert-molecules -f rbd.gro -ci surf.gro -o protsurf.gro -nmol 5
}
#make_prot_surf 

## First minimization 
function first_min {
	$g grompp -f min.mdp -c protsurf.gro -r protsurf.gro  -p $top -o min.tpr -maxwarn 1
	$g mdrun -v -deffnm min 
}
#first_min
function solvation {
	$g  solvate -cp min.gro -cs spc216.gro -o sol.gro -p $top 
}
#solvation
function addions {
          $g  grompp -f ion.mdp -c sol.gro -p $top -o ion.tpr -maxwarn 2
          $g  genion -s ion.tpr -p $top -pname POT -nname CLA -neutral -o system.gro 
}
#addions

# Minimization of the solvated system

function minsolv {	
	$g grompp -f min.mdp -c system.gro -r system.gro  -p $top -o minsol.tpr -maxwarn 1
 	$g mdrun -v -deffnm minsol
}
#minsolv

## NVT equilibration

# index file
function getndx {
	$g make_ndx -f minsol.gro -o index.ndx 
}
#getndx 

function  runnvt1 {
	$g grompp -f nvteq.mdp -c minsol.gro -r minsol.gro  -p $top -o nvt1.tpr -maxwarn 1
}
#runnvt1

#### NPT equilibration  

function  runnpt1 {
	$g grompp -f npteq.mdp -c nvt1.gro -r nvt1.gro  -p $top -o npt1.tpr -maxwarn 1
}
#runnpt1
function  runnpt2 {
	$g grompp -f npteq2.mdp -c npt1.gro -r npt1.gro  -p $top -o npt2.tpr -maxwarn 1
}

#runnpt2 

function  runnpt3 {
	$g grompp -f npteq2.mdp -c npt2.gro -r npt2.gro  -p $top -o npt3.tpr -maxwarn 1
}

#runnpt3 
#Production run 10 ns  
function  md1 {
	$g grompp -f md1.mdp -c npt2.gro   -p $top -o md1.tpr -maxwarn 1
}
md1


         
