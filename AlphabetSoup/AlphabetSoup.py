def AlphabetSoup(str):
    string = ['' for x in range(len(str))]
    array = [-1 for x in range(len(str)+1)]
    for sayac in range(len(str)):
        array[sayac] = ord(str[sayac])

    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            # Select the smallest value
            if array[j] < array[minimum]:
                minimum = j

        # Place it at the front of the
        # sorted end of the array
        array[minimum], array[i] = array[i], array[minimum]
    array.remove(-1)
    print(array)
    for sayac in range(len(str)):
        string[sayac] = chr(array[sayac])
    return ''.join(string)


# keep this function call here
str = input("String: ")
print(AlphabetSoup(str))
