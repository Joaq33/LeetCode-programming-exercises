# Python Program to find Factors of a Number

number = int(input("Please Enter any Number: "))

value = 2
print("Factors of a Given Number {0} are:".format(number))

while (value <= number):
    if (number % value == 0):
        print("{0}".format(value))
    value = value + 1