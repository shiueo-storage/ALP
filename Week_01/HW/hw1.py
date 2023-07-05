"""
Task Instructions
You are going to write a program called "Time Reminder"

The user has to enter a number between 0 and 23
If the number is less than 8 display a message saying "too early to get up"
If the number is less than 12 display a message saying "Good morning"
If the number is less than 14 display a message saying "Lunch time!"
If the number is less than 18 display a message saying "Good afternoon"
If the number is equal to 18 display a message saying "Tea Time"
If the number is less or equal than 19 display a message saying "Good evening"
If the number is less or equal than 22 display a message saying "Nearly bedtime"
If the number is 23 display a message saying "Good night!"
Any other number is met with the response “Sorry, I don’t recognise that”


You are free to use any of the methods that we have learned in class.
"""
# Start coding below this line
n = int(input("give me a number between 0 and 23\n"))
if n < 0:
    print("Sorry, I don’t recognise that")
elif n < 8:
    print("too early to get up")
elif n < 12:
    print("Good morning")
elif n < 14:
    print("Lunch time!")
elif n < 18:
    print("Good afternoon")
elif n == 18:
    print("Tea Time")
elif n < 20:
    print("Good evening")
elif n < 23:
    print("Nearly bedtime")
elif n == 23:
    print("Good night!")
else:
    print("Sorry, I don’t recognise that")
