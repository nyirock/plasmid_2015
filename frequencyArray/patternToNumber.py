from addDimension import addDimension

k=4
patterns=[]
dntps=['A','C','G','T']
d1=['A','C','G','T']
out=[]
    
a=d1
for i in range(k-1):
    a=addDimension(a)

print a.index('ACAC')
