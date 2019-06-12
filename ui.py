'''
Script for the user interface. Takes two input files and name of output file. This script calls the function inside concat2fastas.py to perform the actual sequence concatenation. 
'''
import sys
#Import the module necessary for window-based interface. If it is missing, tell user to install it. 
try:
    import PySimpleGUI as sg
except ImportError:
    sys.exit("""You need the PySimpleGUI package for this. 
            Install it by running "pip install PySimpleGUI" or go to https://github.com/PySimpleGUI/PySimpleGUI""")

#Load the Biopython package. If it is missing, tell user to install it. 
try:
    from Bio import SeqIO
except ImportError:
    sys.exit("""You need the Biopython package for this. 
            Install it by running "pip install biopython" or go to https://biopython.org""")
#Import the function that does the concatenating work. 
from concat2fastas import concat

#The main window, where you input the values. 
event, filenames = sg.Window('Get filename example'). Layout([[sg.Text('First file')], [sg.Input(), sg.FileBrowse()], [sg.Text('Second file')], [sg.Input(), sg.FileBrowse()], [sg.Text('Output file (incl. extension)')], [sg.InputText()], [sg.OK(), sg.Cancel()] ]).Read()

#Pass the input values to the function. 
out=concat(filenames[0], filenames[1])

#Write out the resulting concatenated seqs. 
SeqIO.write(out, filenames[2], "fasta")