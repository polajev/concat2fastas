# concat2fastas
A tool to concatenate DNA sequences horizontally. 
The first fasta sequence from file 1 will be concatenated with the first sequence from file 2, the second with the second etc. 
The tool has both a graphical user interface (ui.py) and a terminal version (terminal.py). The terminal version prints the results to the screen. Unless they are redirected to a file, of course. 

Requires the Biopython package. It can be installed by running the command "pip install biopython". (pip3 for Python 3). For more information, go to https://biopython.org
Also requires PySimpleGUI, if the graphical user interface (ui.py) is desired. It can be installed by running the command "pip install PySimpleGUI". (pip3 for Python 3). For more information, go to https://github.com/PySimpleGUI/PySimpleGUI

Needs two files as input. Includes a test example. 

Example of usage in terminal: 
>python3 terminal.py example/test1.fa example/test2.fa > concats.fa

This will concatenate DNA sequences from file test1.fa and file test2.fa, and write the results to file concats.fa

To use the graphical UI, run the ui.py file: 
>python3 ui.py