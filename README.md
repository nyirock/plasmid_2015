# plasmid_2015
##Structure
Main script **plasmid_2015_main.py** requires two other files containing its functions - **frequent_patterns.py** and **count_fn.py** to be placed in the same directory to provide the functionality. Program also requires input DNA file to be in the same directory as the script files. All the required files are provided in the folder of the repository.

##Input
With no input DNA file specified, program uses i the file **input_DNA.txt** for input as a default parameter. Any input file could be specified with the parameter -i providing it has plain DNA text. Script only accepts plain letters of DNA alphabet: A(a), T(t), G(g), C(c).

##Output
Program outputs the occurence of the most frequent DNA pattern of the desired lenth and its sequence

##Usage
Script requires python2 interpreter to be installed and added to the system PATH.
###Example of using the file with default parameters
**$python plasmid_2015_main.py**

Using default inputfile: input_DNA.txt

Using default k-mer length of 10 bp

We are working with the dataset of 40001 characters....

Single most frequent pattern found

10 bp motif ACCGGAATTT occurs 7 times in the input DNA sequence

###Getting help
**$python plasmid_2015_main.py -h**

Usage: plasmid_2015_main.py -i \<inputfile\> -k \<k-mer length\>
###Custom parameters
**$python plasmid_2015_main.py -i input_DNA_pCMMB549_rep_region_140_180_kb.txt -k 12**

Using DNA inputfile: input_DNA_pCMMB549_rep_region_140_180_kb.txt

Length of k-mer is 12 bp

We are working with the dataset of 40001 characters....

No single most frequent pattern found

12 bp motif GGACCGGAATTT occurs 3 times in the input DNA sequence

12 bp motif CGCGCTCGAGGA occurs 3 times in the input DNA sequence

###Note
Operating large DNA datasets requires more time and computing resources. For training purposes could be used a file  containing 64-bp sequence OriV sequence of  pOZ172.
