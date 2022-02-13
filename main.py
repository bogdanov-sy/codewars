a = [1, 2, 3, 4, 4]
b = [2, 4]

def array_diff(a, b):
    #your code here
    z = 0
    c = a
    print(c)
    for x in c:
        print(x)
        for y in b:
            print('--' + str(y))
            if x == y:
                del a[z]
                print(a)
        z = z + 1
    return(a)

print(array_diff(a, b))