from addDimension import addDimension

file_name='vibrio'

hand=open(file_name)
p=hand.read()
hand.close()

k=9
p.strip()

#print type(p),type(text)
#re-initialization for the file input
#text=p

patterns=[]
frequencyArray=[]
dntps=['A','C','G','T']
d1=['A','C','G','T']
out=[]
q=''
for i in range(len(p)):
    if p[i] in dntps:
        q=q+p[i]
        
#print len(q)

a=d1
for i in range(k-1):
    a=addDimension(a)

#test for k=7
#print a[5437]

for i in range(4**k):
    frequencyArray.append(0)
#print len(p)
#print a
for i in range(len(text)-k+1):
    pttrn=text[i:(i+k)]

    j=a.index(pttrn)

    #print pttrn
    #print j
    #print a[j]
    frequencyArray[j]=frequencyArray[j]+1
    #print frequencyArray[j]
    #print i

#print frequencyArray
out=''
for i in range(len(frequencyArray)):
    out=out+str(frequencyArray[i])+' '

fout=open('frequencyArray_out','w')

print max(frequencyArray)
pt_ind=frequencyArray.index(max(frequencyArray))
print pt_ind
print a[pt_ind]
for i in range(len(frequencyArray)):
    #print a[i];
    fout.write(str(frequencyArray[i])+' ')
fout.close()

print sum(frequencyArray)
print len(text)
#print len(frequencyArray),len(a)
#print len(text),(len(frequencyArray)+k)



# ^ Matches the beginning of a line
# $ Matches the end of a line 
#text="TCTCAGAACTCTCCGTGGAGACAGCACAGACAGCACCACTGCGTGACCAAAACAGACCAAAACACTCTCCGTGGGACCAAAACATCTCAGAATCTCAGAATCTCAGAATCTCAGAAAGACAGCACAGACAGCACGACCAAAACAAGACAGCACCACTGCGTCTCTCCGTGGAGACAGCACCACTGCGTCACTGCGTAGACAGCACAGACAGCACAGACAGCACCTCTCCGTGGAGACAGCACAGACAGCACCTCTCCGTGGCTCTCCGTGGTCTCAGAAAGACAGCACCACTGCGTCTCTCCGTGGCACTGCGTCACTGCGTCTCTCCGTGGTCTCAGAAAGACAGCACAGACAGCACTCTCAGAACTCTCCGTGGCTCTCCGTGGAGACAGCACCACTGCGTGACCAAAACACTCTCCGTGGCACTGCGTAGACAGCACAGACAGCACCACTGCGTGACCAAAACAAGACAGCACGACCAAAACACACTGCGTTCTCAGAACTCTCCGTGGCACTGCGTCTCTCCGTGGCACTGCGTCACTGCGTAGACAGCACGACCAAAACAGACCAAAACAGACCAAAACACTCTCCGTGGGACCAAAACACTCTCCGTGGCACTGCGTAGACAGCACAGACAGCACCACTGCGTCTCTCCGTGGCTCTCCGTGGAGACAGCACTCTCAGAACACTGCGTCACTGCGTGACCAAAACACACTGCGTAGACAGCACTCTCAGAACTCTCCGTGGCACTGCGTCACTGCGTTCTCAGAACACTGCGTCACTGCGTAGACAGCACCTCTCCGTGGCTCTCCGTGGAGACAGCACTCTCAGAACTCTCCGTGGCACTGCGTGACCAAAACATCTCAGAACACTGCGTTCTCAGAAGACCAAAACACACTGCGTTCTCAGAAAGACAGCACTCTCAGAACTCTCCGTGGAGACAGCAC" . Matches any character
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

# from methanotrophs_fasta_count import 
# from methanotrophs_fasta_count import 

#file_name='frequent_words_data.txt'

#r=ro.r
#r.plot(r.rnorm(100),xlab="x", ylab="y")
#time.sleep(5)


#hand=open(file_name)
#p=hand.read()
#hand.close()

#counting genera


#text="TCTCAGAACTCTCCGTGGAGACAGCACAGACAGCACCACTGCGTGACCAAAACAGACCAAAACACTCTCCGTGGGACCAAAACATCTCAGAATCTCAGAATCTCAGAATCTCAGAAAGACAGCACAGACAGCACGACCAAAACAAGACAGCACCACTGCGTCTCTCCGTGGAGACAGCACCACTGCGTCACTGCGTAGACAGCACAGACAGCACAGACAGCACCTCTCCGTGGAGACAGCACAGACAGCACCTCTCCGTGGCTCTCCGTGGTCTCAGAAAGACAGCACCACTGCGTCTCTCCGTGGCACTGCGTCACTGCGTCTCTCCGTGGTCTCAGAAAGACAGCACAGACAGCACTCTCAGAACTCTCCGTGGCTCTCCGTGGAGACAGCACCACTGCGTGACCAAAACACTCTCCGTGGCACTGCGTAGACAGCACAGACAGCACCACTGCGTGACCAAAACAAGACAGCACGACCAAAACACACTGCGTTCTCAGAACTCTCCGTGGCACTGCGTCTCTCCGTGGCACTGCGTCACTGCGTAGACAGCACGACCAAAACAGACCAAAACAGACCAAAACACTCTCCGTGGGACCAAAACACTCTCCGTGGCACTGCGTAGACAGCACAGACAGCACCACTGCGTCTCTCCGTGGCTCTCCGTGGAGACAGCACTCTCAGAACACTGCGTCACTGCGTGACCAAAACACACTGCGTAGACAGCACTCTCAGAACTCTCCGTGGCACTGCGTCACTGCGTTCTCAGAACACTGCGTCACTGCGTAGACAGCACCTCTCCGTGGCTCTCCGTGGAGACAGCACTCTCAGAACTCTCCGTGGCACTGCGTGACCAAAACATCTCAGAACACTGCGTTCTCAGAAGACCAAAACACACTGCGTTCTCAGAAAGACAGCACTCTCAGAACTCTCCGTGGAGACAGCAC"
#a=count_fn(dataset,'AGA');
#R_vector=ro.IntVector(a)
#r.pdf("ACTAT_histogram_.pdf")
#r.hist(R_vector, main="Distribution of ACTAT-sequence in V.cholerae genome", xlab="Position")
#time.sleep(50)


#fout=open('positions','w')

#for i in range(len(a)):
    #print a[i];
#    fout.write(str(a[i])+'\n')

#fout.close()

#frequent_patterns(dataset,11)



