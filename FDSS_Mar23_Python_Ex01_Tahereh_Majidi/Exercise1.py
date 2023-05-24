text = input('Please Enter your text: ')
def table_counter(text):
    
    counter = {}
    for char in text:
        if char in counter and char.isalnum():
            counter[char] += 1
        elif not char.isalnum():
            continue
        else:
            counter[char] = 1

    
    print('+------+-----------+')
    print('| NAME | FREQUENCY |')
    print('+======+===========+')
    for char, count in counter.items():
        print(f'|   {char}  |     {count}     |')
        print('+------+-----------+')
table_counter(text)