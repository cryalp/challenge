def FirstFactorial(num):
    for x in range(2, num):
        num = num * x
    # code goes here
    return num


# keep this function call here
innum = input("Num = ")
print(FirstFactorial(int(innum)))
