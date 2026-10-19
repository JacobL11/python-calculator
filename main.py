number1 = float(input("enter the first number.. "))
number2 = float(input("enter the second number.. "))

print("operations: add, sub, mult, div, mod, pow")
operation = input("select what operation to do")
if operation in ("add", "addition", "+"):
    total = number1 + number2
    print(f"{number1} + {number2} = {total}")
elif operation in ("sub", "subtract", "subtraction", "-"):
    total = number1 - number2
    print(f"{number1} - {number2} = {total}")
elif operation in ("mult", "multiply", "multiplication", "*"):
    total = number1 * number2
    print(f"{number1} * {number2} = {total}")
elif operation in ("div", "divide", "division", "/"):
    total = number1 / number2
    print(f"{number1} / {number2} = {total}")
elif operation in ("mod", "modulus", "remainder", "%"):
    total = number1 % number2
    print(f"the remainder of {number1} / {number2} is {total}")
elif operation in ("pow", "power", "exponent", "^", "**"):
    total = number1 ** number2
    print(f"{number1} to the power of {number2} is {total}")

print("\nbye")