def LetterCapitalize(str):
    string = ['' for x in range(len(str))]
    string[0] = str[0].upper()
    spaced = False
    for sayac in range(1, len(str)):
        if str[sayac] == ' ' and not spaced:
            string[sayac] = str[sayac]
            string[sayac] = str[sayac].upper()
            spaced = True
        elif spaced:
            string[sayac] = str[sayac].upper()
            spaced = False
        else:
            string[sayac] = str[sayac]
    return ''.join(string)


# keep this function call here
str = input("String: ")
print(LetterCapitalize(str))


