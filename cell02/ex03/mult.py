#!/usr/bin/env python3
a = int(input("Enter the first number: ").strip())
b = int(input("Enter the second number: ").strip())
result = a * b
print(str(a) + " x " + str(b) + " = " + str(result))

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")