# Starter Code

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
number3 = int(input("Please enter a third number"))

if number1 > number2:
    print("Number 1 is bigger than number 2")
elif number2 > number1:
    print("Number 2 is bigger than number 1")
else:
    print("Both numbers are the same")

if number3 > number1:
    print("Number 3 is bigger than number 1")
elif number1 > number3:
    print("Number 1 is bigger than number 3")
else:
    print("Both numbers are the same (Number1 and Number 3)")

if number3 > number2:
    print("Number 3 is bigger than number 2")
elif number2 > number3:
    print("Number 2 is bigger than number 3")
else:
    print("Both numbers are the same (Number2 and Number3)")
