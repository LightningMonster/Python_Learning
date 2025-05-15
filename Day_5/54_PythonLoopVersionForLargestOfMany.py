largest_number = -999999999

while True:
    number = int(input("Enter a number or -1 to stop: "))
    if number == -1:
        break
    if number > largest_number:
        largest_number = number

print("The largest number is:", largest_number)