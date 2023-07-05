# Example code 1

number = 7  # set the variable number as 7
print("I have thought of a number between 1 and 10")  # print sentences
guess = int(input("Can you guess what it is?"))  # get input from the user

if guess == number:  # if guess is exactly same as the variable number, print "Correct!"
    print("Correct!")
elif guess < number:  # if guessed number is less than number, print Too Low!
    print("Too Low!")
else:  # if guessed number is greater than number, print Too High!
    print("Too High!")

# Example code 2

number1 = int(
    input("Please enter a number")
)  # get input from the user and put it to number1
number2 = int(
    input("Please enter another number")
)  # get input from the user and put it to number2

if (
    number1 > number2
):  # if number1 is greater than number2, print num1 is bigger than num2
    print("Number 1 is bigger than number 2")
elif number2 > number1:  # if num2 is greater than num1, print num2 is bigger than num1
    print("Number 2 is bigger than number 1")
else:  # if they are same, print Both numbers are the same
    print("Both numbers are the same")
