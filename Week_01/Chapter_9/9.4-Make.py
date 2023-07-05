def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def divide(a, b):
    return a / b


N1, N2 = map(int, input("Give me a two numbers with a space\n").split())
print("ADDITION: 1\nSUBSTRACTION:2\nMULTIPLICATION:3\nDIVISION:4\n")
choice = input()
if choice == "1":
    print(addition(N1, N2))
elif choice == "2":
    print(substraction(N1, N2))
elif choice == "3":
    print(multiplication(N1, N2))
elif choice == "4":
    print(divide(N1, N2))
else:
    print("You typed something wrong.")
