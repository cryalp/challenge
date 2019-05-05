def TimeConvert(num):
    minute = num % 60
    hour = num/60
    return str(int(hour)) + ":" + str(int(minute))


# keep this function call here
num = input("Value = ")
print(TimeConvert(float(num)))


