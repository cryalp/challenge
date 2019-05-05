def SimpleAdding(num):
    summ = 0
    for sayac in range(int(num)+1):
        summ = sayac + summ
    return summ
# keep this function call here
num = input("Value = ")
print(SimpleAdding(num))
