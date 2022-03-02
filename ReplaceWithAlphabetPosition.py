
def alphabet_position(text):
    ABC = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(ABC)
    code = ''
    for i in text:
        print(i)
        if i.upper() in ABC:
            print(i.upper())
            index = ABC.index(i.upper()) + 1
            print(index)
            code += ' ' + str(index)
    #code_str = ''.join(code)
    print(code)
    return(code)
