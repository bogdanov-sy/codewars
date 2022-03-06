
def alphabet_position(text):
    ABC = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(ABC)
    code = ''
    counter = 0
    for i in text:
        print(i)
        if i.upper() in ABC:
            print(i.upper())
            index = ABC.index(i.upper()) + 1
            print(index)
            if counter == 0:
                code += str(index)
            else:
                code += ' ' + str(index)
        counter += 1
        print(counter)
    #code_str = ''.join(code)
    print(code)
    return(code)
