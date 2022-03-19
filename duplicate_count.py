def duplicate_count(text):
    # Your code goes here

    count = 0
    text_lower = text.lower()
    print(text_lower)
    list_text = list(text_lower)
    set_text = set(list_text)
    print(set_text)
    print(list_text)
    for i in set_text:
        list_text_count = list_text.count(i)
        if list_text_count > 1:
            count += 1
            print(count)
    print(count)
    return (count)