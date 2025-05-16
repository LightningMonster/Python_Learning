secret_number = 7  # The magician's secret number
number = int(input("Enter your guess: "))
while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter your guess: "))
print("Well done, muggle! You are free now.")