def duplicate_count(text):
    # Your code goes here
    count = 0
    for i in text:
        for b in text:
            if i.lower() == b.lower():
                count += 1
    print(count)
    return (count)

