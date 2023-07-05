# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer: It prints "Too Low!"

# What happens if you input the guess '6'?
  # Answer: It prints "Too High!"

# What happens if you input the guess '5'?
  # Answer: It prints "Correct!"

# What happens if you input the guess '-5'?
  # Answer: It prints "Too Low!"

# What happens if you input the guess '0'?
  # Answer: It prints "Too Low!"

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer: if a < b and it supposed to be true, then it means a is less than b. and, for a > b, if it's true, then it means a is bigger then b.

# What happens if you change line 5 to if guess = number: ?
  # Answer: it should make an error because, guess is not assigned before. and we are comparing input with guess.

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer: We can make several ways to separate some cases, and can make output for each situations.


