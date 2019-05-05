def CheckNums(num1, num2):
    if num2 > num1:
        return True
    elif num1 > num2:
        return False
    elif num1 == num2:
        return -1


# keep this function call here
num1 = input("Value1 = ")
num2 = input("Value2 = ")
print(CheckNums(num1, num2))
