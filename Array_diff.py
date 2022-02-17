def array_diff(a, b):
    #your code here
    c = []
    for x in a:
        #print(x)
        if x not in b:
            c.append(x)
            #print(c)
    return(c)