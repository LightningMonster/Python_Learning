# y = 1 / (x + 1/(x + 1/(x + 1/x)))
x = float(input())
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print("y =", y)