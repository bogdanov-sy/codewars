
def alphabet_position(text):
    ABC = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(ABC)
    code = []
    for i in text:
        if i.upper() in ABC:
            y = ABC.index(str(i))
            print(y)
            code.append(y)
    #print(code)
    return(code)
