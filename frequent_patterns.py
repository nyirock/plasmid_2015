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
#\w only matches a single characterappendappendappend
#\w+
# \\ for methacharacters: \\. for dot

# ^X.*: 1Start of line 2'X' character .* any char any number of times 3':' character -> X______:

from count_fn import count_fn

def frequent_patterns(string, size):
    # string - input string, search - search text
 

    import re

    FrequentPatterns={};
    Patterns={}
    pattern=[];
    
    count=[];
    position=list()
    for i in range(len(string)-size):
        pattern.append(string[i:(i+size)])
        count.append(count_fn(string,string[i:(i+size)]))
#        print i
#        if string[i:(i+len(search))]==search:
#            count=count+1
#            position.append(i)
#    maxCount=max(count)*0.8
    maxCount=max(count)
    
    for i in range(len(string)-size):
        if count[i]>=maxCount:
            FrequentPatterns[pattern[i]]=count[i]

#    for i in range(len(pattern)):
#        print str(pattern[i])+':'+str(count[i])
	#print FrequentPatterns
	
    
	return FrequentPatterns



