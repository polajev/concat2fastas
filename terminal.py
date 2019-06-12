'''
Concatenate seqs in the terminal (command line). Prints result on the screen. Unless you redirect it to a file, of course.  

Example of usage: 
>python3 terminal.py example/test1.fa example/test2.fa > concats.fa
'''

import sys

#Load the Biopython package. If it is missing, tell user to install it.
try:
    from Bio import SeqIO
except ImportError:
    sys.exit("""You need the Biopython package for this. 
            Install it by running "pip install biopython" or go to https://biopython.org""")

#Import the function that does the concatenating work. 
from concat2fastas import concat

#Get input filenames from terminal. 
fastafile1=open(sys.argv[1],'r')
fastafile2=open(sys.argv[2],'r')

#Pass the input values to the function. 
out=concat(fastafile1, fastafile2)

#Print result onto screen, in fasta format. 
for i in range(len(out)):
	print(">%s" % out[i].id)
	print(out[i].seq)
