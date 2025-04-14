input_str = iter('aaaabbcccccab')

output = []
count = 0
last_letter = ''
while True:
    try:
        letter = next(input_str)
        if letter != last_letter:
            if last_letter:
                output.append((last_letter,count))
            count = 1
        else:
            count += 1
        last_letter = letter
    except StopIteration:
        output.append((last_letter,count))
        break
    
print(input_str)
print(output)