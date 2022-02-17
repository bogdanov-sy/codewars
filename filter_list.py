def filter_list(l):
    'return a new list with the strings filtered out'

    global c
    c = []
    for x in l:
        print(x)

        print(type(x))
        print(type(''))
        if type(x) != type(''):
            c.append(x)
    return (c)
