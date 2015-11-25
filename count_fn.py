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
def count_fn(string, search):
    # string - input string, search - search text

    import re
    
    count=0;
    position=list()
    for i in range(len(string)-len(search)):
#        print i
        if string[i:(i+len(search))]==search:
            count=count+1
            position.append(i)


    #print count
    #print position
    #print len(position)
    return count


