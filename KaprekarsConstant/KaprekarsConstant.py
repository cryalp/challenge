def sort(num):
    sayac = len(str(num))
    array = [0 for x in range(sayac)]
    for x in range(sayac):
        array[x] = num[x]
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[minimum], array[i] = array[i], array[minimum]
    array = ''.join(array)
    print(array)
    return array


def reverse(num):
    revarray = num[::-1]
    return revarray


def kaprekarsconstant(num):
    array = sort(str(num))
    revarray = reverse(array)
    count = sum = 0
    while sum != 6174:
        if array > revarray:
            sum = int(array) - int(revarray)
            print(sum, "---")
            array = sort(str(sum))
            revarray = reverse(array)
        elif array < revarray:
            sum = int(revarray) - int(array)
            print(sum, "---")
            array = sort(str(sum))
            revarray = reverse(array)
        count += 1
    return count


# keep this function call here
num = input("Value = ")
print(kaprekarsconstant(num))


