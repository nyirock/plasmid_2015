from addDimension import addDimension
from out_text import out_text



text=out_text()



k=10


#print type(p),type(text)
#re-initialization for the file input
#text=p


frequencyArray=[]
dntps=['A','C','G','T']
d1=['A','C','G','T']
out=[]

        
#print len(q)

a=d1
for i in range(k-1):
    a=addDimension(a)

#test for k=7
#print a[5437]

#Frequent patterns of dimension k initialization
for i in range(4**k):
    frequencyArray.append(0)
#print len(p)
#print a

ind=[]
cnt=[]
srt_ind=[]

for i in range(len(text)-k+1):
    pttrn=text[i:(i+k)]
    ind.append(a.index(pttrn))
    cnt.append(1)
#    j=a.index(pttrn)

    #print pttrn
    #print j
    #print a[j]
    
ind.sort()
    #frequencyArray[j]=frequencyArray[j]+1
    #print frequencyArray[j]
    #print i
for i in range(1, len(text)-k+1):
    if ind[i]==ind[i-1]:
        cnt[i]=cnt[i-1]+1
max_count=max(cnt)

for i in range(len(text)-k+1):
    if cnt[i]==max_count:
        pattern=a[ind[i]]
        print ind[i]

print pattern
print max_count
