'''
A module to concatenate sequnences from two fasta files, horizontally. 
The first fasta sequence from file 1 will be concatenated with the first sequence from file 2. 
Provides a function that takes the names of two fasta files and returns the concatenated seqs. 

'''
def concat(input1,input2):
    import sys
    #Load the Biopython package. If it is missing, tell user to install it. 
    try:
        from Bio import SeqIO
    except ImportError:
        sys.exit("""You need the Biopython package for this. 
                Install it by running "pip install biopython" or go to https://biopython.org""")


    fastafile1=input1
    fastafile2=input2

    #Prepare some variables. 	
    entries1=[]
    entries2=[]

	#Read in the sequence data. 
    for rec1 in SeqIO.parse(fastafile1,'fasta'):
        entries1.append(rec1)
    for rec2 in SeqIO.parse(fastafile2,'fasta'):
        entries2.append(rec2)
		
    for i in range(len(entries1)):
        entries1[i].id="Concatenated_%s_%s" % (entries1[i].id, entries2[i].id)
        entries1[i].seq=entries1[i].seq+entries2[i].seq

    return entries1