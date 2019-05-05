def LetterChanges(str1):
    str1 = [ord(c)+1 for c in str1]
    for x in range(len(str1)):
        if chr((ord(chr(str1[x]))-1)).isspace():
            print(chr(str1[x]))
        else:
            str1[x] = chr(str1[x])
        if str1[x] == 'a' or str1[x] == 'e' or str1[x] == 'o' or str1[x] == 'i' or str1[x] == 'u':
            str1[x] = str1[x].upper()

    str1 = ''.join(str1)
    return str1


# keep this function call here
print(LetterChanges("hello world"))
