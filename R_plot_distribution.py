# ^ Matches the beginning of a line
# $ Matches the end of a line 
# . Matches any character
# \s Matches whitespace
# \S Matches any non-whitespace character
# * Repeats a character zero or more times
# *? Repeats a character zero or more times (non-greedy)
# + Repeats a characater one or more times
# +? Repeats a character one or more times (non-greedy)
# [aeiou] Matches a single character in the listed set
# [^XYZ] Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# ( Indicates where string extraction is to start
# ) Indicates where string extraction is to end
#\w only matches a single character
#\w+
# \\ for methacharacters: \\. for dot

# ^X.*: 1Start of line 2'X' character .* any char any number of times 3':' character -> X______:
import re
from count_position_fn import count_position_fn
import rpy2
import rpy2.robjects as ro
import time


import time, os
# from methanotrophs_fasta_count import 
# from methanotrophs_fasta_count import 

file_name='input_DNA_pCMMB549_entire.txt'

r=ro.r
#r.plot(r.rnorm(100),xlab="x", ylab="y")
time.sleep(5)

hand=open(file_name)
p=hand.read()
hand.close()

#counting genera


dataset="AGAACTTAATACTTAATAGCACTTAATCACTTAATACTTAATTCCTGACTTAATACTTAATACTTAATCCCTACTAATCCTCTGAGACTTAATGGTACTTAATGATTTTCTGCGCGTTAGAGCTACTTAATAACTTAATCTTTACTTAATCAACTTAATGACTTAATGACTTAATAACTTAATACTTAATCACTTAATCACTTAATTACACTTAATACTTAATGCTCGACTTAATTTACTTAATTGCAGACTTAATCTGACTTAATAACTTAATCGCACTTAATTCGCTACAACTTAATTTTATGACTTAATACTTAATCCGCAACTTAATCTACTTAATACTTAATAGATACACTTAATAATGACTTAATTTTCGACTTAATGGCAACTTAATCGACTTAATCATTCACTTAATTCATGAACTTAATATCACTTAATACTTAATGCACTTAATTTACTTAATACTTAATACTTAATGACTTAATACTTAATACTTAATCGATAAAACACTTAATACTTAATACTTAATAACTTAATTTCTCTTTAACTTAATTACTTAATCCTTTATACTTAATGCAATACTGACTTAATTCGTCACTTAATACTTAATGCACTTAATACTTAATCGAGGACTTAATACTTAATACTTAATACTTGACCAGACTTAATCCTCCGTAACTTAATAGCACTTAATAATGACTTAATGCACTTAATAGAGTACTTAATATATACTTAATACTTAATCCTACTTAATGCTTACTTAATAGTTTCCGACTTAATTACACACTTAATCGTTACCAGTGGTGAACTTAATACTTAATAACTTTGACTTAATAGGACTTAATACTTAATTTACTTAATATTGCCTCGCACTTAATACTTAATACTTAATACTTAATCCTCCCGACAGTGGGACTTAATACTTAATAGTGATACACTTAATACGACTTAATAATTGTCACTTTCACTTAATTCAGCGGACTTAATTACTTAATTGAGACTTAATTTCAGACAACTTAAT"
a=count_position_fn(p,'ACCGGAATTT');
R_vector=ro.IntVector(a)
r.pdf("ACCGGAATTT_pCMMB549_distribution.pdf")
r.hist(R_vector, main="Distribution of ACCGGAATTT-sequence in pCMMB549", xlab="Position, bp", xlim=r.c(0, len(p)))
time.sleep(50)


fout=open('positions','w')

for i in range(len(a)):
    #print a[i];
    fout.write(str(a[i])+'\n')

fout.close()



