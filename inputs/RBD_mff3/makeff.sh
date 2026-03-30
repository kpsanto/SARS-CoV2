fl=rbdAA.pdb 
fo=RBDCG.pdb 
ft=RBD.top
ss=rbdAA.ssd  
./martinize -f $fl -ff martini303v.partition -x $fo -ss $ss -o $ft  -elastic
