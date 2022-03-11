def duplicate_count(text):
    # Your code goes here

    count = 0
    len_text = len(str(text))
    print(len_text)
    list_text = list(text)
    print(list_text)
    for i in range(1, len_text):
        b = list_text.pop()
        print(list_text)
        print(b)
        count += list_text.count(b)
        print(count)
        #for x in list_text:
        #    print(x)
        #    if x == b:
        #        count += 1
    print(count)
    return (count)

