a = [1, 2, 3, 4, 4]
b = [2, 4]

def array_diff(a, b):
    #your code here
    c = []
    for x in a:
        print(x)
        if x not in b:
            c.append(x)
            print(c)
    return(c)

print(array_diff(a, b))