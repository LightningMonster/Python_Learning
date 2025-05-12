# Operator Precedence Example: * has higher priority than +
print("2 + 3 * 5 =", 2 + 3 * 5)  # Expected: 2 + (3 * 5) = 17

# Left-sided Binding of Modulus (%)
print("9 % 6 % 2 =", 9 % 6 % 2)  # Expected: (9 % 6) % 2 = 3 % 2 = 1

# Right-sided Binding of Exponentiation (**)
print("2 ** 2 ** 3 =", 2 ** 2 ** 3)  # Expected: 2 ** (2 ** 3) = 2 ** 8 = 256

# Negation and Exponentiation (Important precedence case)
print("-3 ** 2 =", -3 ** 2)         # Expected: -(3 ** 2) = -9
print("-2 ** 3 =", -2 ** 3)         # Expected: -(2 ** 3) = -8
print("-(3 ** 2) =", -(3 ** 2))     # Expected: -9 (same as above, made explicit)
