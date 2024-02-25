def code(text):
    newlist = []

    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            if char.isupper():
                codes = chr((ord(char) + 1 -65) % 26 + 65)
                newlist.append(codes)

            elif char.islower():
                codes = chr((ord(char) + 1 - 97) % 26 + 97)
                newlist.append(codes)

        else:
            newlist.append(char)

    print(''.join(newlist))

code('Hello World! My number is 9182. hhjhjhhj')
