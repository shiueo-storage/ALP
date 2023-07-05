# Example code 1

age = 18  # the variable age assigned as 18 (integer)

if age > 18:
    print(
        "You are old enough to drive"
    )  # if age is bigger than 18, it print "You are old enough to drive"

# Example code 2

num1 = 1337  # num1 assigned as 1337

if num1 == 10:
    print(
        "This text is output because the condition was true"
    )  # if num1 is 'same' as 10, it print those messages
else:
    print("This text is output because the condition was false")  # else.

# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
    print("Correct!")
if guess < number:
    print("Too Low!")
if guess > number:
    print("Too High!")

# if user give a 5 as a input, it will print Correct! message, else, if bigger than 5, it will print too high, if less, then it will print too low.
