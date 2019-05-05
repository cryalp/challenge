def FirstReverse(str):
    sayac = len(str)
    string = ["" for x in range(sayac)]

    """for x in range(sayac, 0, -1):
        string[sayac-x] = str[x-1]"""
    string = reversed(str)
    return ''.join(reversed(str))


# keep this function call here
string = input("haha: ")

print(FirstReverse(string))
