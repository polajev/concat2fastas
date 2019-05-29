# concat2fastas
A script to concatenate DNA sequences horizontally. 
The first fasta sequence from file 1 will be concatenated with the first sequence from file 2, the second with the second etc. 
Dumps the resulting fasta entries onto the screen. The results can be redirected to a file.

Needs two files as input. Includes a test example. 

Example of usage: 
>python3 concat2fastas.py example/test1.fa example/test2.fa > concats.fa

This will concatenate DNA sequences from file test1.fa and file test2.fa, and write the results to file concats.fa
