# plasmid_2015
##Structure
Main script plasmid_2015_main.py two other files containing its functions - frequent_patterns.py and tcount_fn.py to be placed in the same directory

##Input
Program expects input DNA to be stored in the file input_DNA.txt as a default parameter. Script only accepts plain letters of DNA alphabet: A(a), T(t), G(g), C(c)

##Output
Program outputs the occurence of the most frequent DNA pattern of the desired lenth and its sequence

##Usage

###Example of using the file with default parameters
python plasmid_2015_main.py

input_DNA.txt is used as input DNA sequence, length of the motif is equal to 10-bp
###Getting help
python plasmid_2015_main.py -h
Usage: test.py -i <inputfile> -k <k-mer length>
###Custom parameters
plasmid_2015_main.py -i input_DNA_pCMMB549_rep_region_140_180_kb.txt -k 14
###Note
Operating large DNA datasets requires more time and computing resourses. For training purposes 64 bp file representinf pOZ172 OriV in the file input_DNA_pOZ172_rep_reigion.txt could be used.
