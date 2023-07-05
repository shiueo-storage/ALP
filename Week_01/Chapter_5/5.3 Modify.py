# Starter Code

number = 5
print("I have thought of a number between 1 and 10") # the number is 5
guess = int(input("Can you guess what it is?")) # get input from the user


if guess < number: # if the input number is less than 5, print "Too Low!"
  print("Too Low!")
if guess > number: # if the input number is greater than 5, print "Too High!"
  print("Too High!")

# so, If the guessed number is 5, it prints nothing