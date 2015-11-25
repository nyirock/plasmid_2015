def addDimension(input_Dim):
    dntps=['A','C','G','T'];
    output=[];
    for i in input_Dim:
        for j in dntps:
            output.append(i+j)
    return output
    


