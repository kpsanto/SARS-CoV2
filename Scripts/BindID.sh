#----------------------------------------
# BindID  - Ligand binding site identitfication 
##----------------------
# units :
# time : ns 

# The folowing parameters are inputs specific to the system
# Set them  accordingly
## 
t1=$1
t2=$2    # time span obtained from Ns (number of residues in contact)  vs time plots 
ligand=POPI
ind=indexf.ndx  # an indexfile that contains only protein and ligand 
# 
t_start=5000  # start of the trajectory file in ns  
t_end=20000    # end time  of the trajectory in ns
dt=5	       # frame-frame interval - ns 
n_res=228      # total number of protein residues- for RBD 
res0=0         # ID of the first residue

g=gmx_mpi          # gromacs prefix 
trj=../r3.xtc     # gromacs trajectory file to analuze 
tp=../md.tpr      # run input file 
r_cont=0.6     # defining the maximun distance for contact 

# number of frames to analze 
n=$((($t2-$t1)/5))
#
bs=$((n/3))  # cretaria for binding site identifiation - 1/3 of the time span
bp=$(((t2-t1)/2*1000+t1*1000))  # frame for bound pose   

# get index file -  specific to the system - can do without this code 
function getndx {
$g make_ndx -f $tp -o $ind <<EOF
1|13
del0-15
q
EOF
}
getndx 

#--------------------
# Get the number of contacts and resdues of contacts frame by frame 
#------------------------------


function getcontdist {
	echo ' Number of frames to analzye : ' $n
	echo Residues in contact  > cont_res.dat 	
	echo Number of contacts > n_cont_res.dat  
	for ((i=1;i<=$n;i++))
	do 
		j=$((i*dt*1000+$t1*1000))
		echo 1 13 | $g mindist -f $trj -s $tp -group -on -o -or -b $j -e $j 
		awk '!/@/&& !/#/' mindistres.xvg > mindres.dat 
		awk '$2<'$r_cont' {print $1}' mindres.dat > temp1
		awk 'END{print NR}' temp1 >nc
		nc=`cat nc`
		echo $j ' ' $nc >> n_cont_res.dat
	        cat temp1 >> cont_res.dat 
	        rm \#*
	done

	rm nc temp1 *.xvg mindres.dat  
}

getcontdist 

function BindSite {
	# get bound pose as the snapshot at the middl time frame 
        $g trjconv -f $trj -s $tp -n indexf.ndx  -o BoundPose.gro -dump $bp
	awk 'NR>2{print $1}' BoundPose.gro > temp0
	uniq temp0 >temp10
	awk 'NR>1' cont_res.dat > temp2 
	echo 'Residue    Occurence ' > Res_ocur.dat
	nbf=$((n_res+1))
        echo $nbf  > bf.dat 	
	for ((i=1;i<=$n_res;i++))
	 do
		 awk '$1=='$i'' temp2 >res
		 awk 'END{print NR}' res >nres
		 nres=`cat nres`
		 awk 'NR=='$i'' temp10 > resnam
		 resnam=`cat resnam`
		 echo $resnam '   ' $((i+res0)) '   ' $nres >>Res_ocur.dat
		 echo $((i+res0)) '    ' $nres >> bf.dat 
	 done
	 rm temp2 res nres resnam temp0 temp10  
	 awk 'NR>1 && $3>'$bs'' Res_ocur.dat > BindSite.dat
	 awk 'END{print NR}' BindSite.dat > nbindres
	 nbindres=`cat nbindres`
	 rm nbindres
	# add a visualization based on beta values representing contact frequency
	echo $nbf '   0' >> bf.dat 
	$g editconf -f BoundPose.gro -o BoundPose.pdb -bf bf.dat 
	rm BoundPose.gro
	echo "=====================================" 
	echo 'Number of frames :' $n
	echo 'Minimum number of frames for binding: ' $bs
	echo 'Number of residues in the binding site : ' $nbindres 
	echo "==========================================="	
 }
BindSite

