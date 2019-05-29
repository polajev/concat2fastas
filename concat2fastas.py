'''
A script to concatenate sequnences from two fasta files, horizontally. 
The first fasta sequence from file 1 will be concatenated with the first sequence from file 2, the second with the second etc. 
Dumps the resulting fasta entries onto the screen. Can be redirected to a file.

Needs two files as input. 

Example of usage: 
>python3 concat2fastas.py example/test1.fa example/test2.fa > concats.fa
'''

import sys
#Load the Biopython package. If it is missing, tell user to install it. 
try:
    from Bio import SeqIO
except ImportError:
    sys.exit("""You need the Biopython package for this. 
                Install it by running "pip install biopython" or go to https://biopython.org""")


fastafile1=open(sys.argv[1],'r')
fastafile2=open(sys.argv[2],'r')

#Prepare some variables. Lists of sequence names and the sequences themselves.
name1=[]
name2=[]
seq1=[]
seq2=[]

#Read and record the data from both files
for rec1 in SeqIO.parse(fastafile1,'fasta'):
	name1.append(rec1.id)                                                                                        
	seq1.append(rec1.seq)	

for rec2 in SeqIO.parse(fastafile2,'fasta'):
	name2.append(rec2.id)                                                                                         
	seq2.append(rec2.seq)                                                                                         

#Concatenate and print to screen
for i in range(len(name1)):
	print(">Concatenated_%s_%s" % (name1[i], name2[i]))
	print(seq1[i]+seq2[i])

fastafile1.close()
fastafile2.close()
