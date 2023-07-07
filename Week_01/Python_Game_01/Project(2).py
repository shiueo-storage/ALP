# Players have to guess the correct number within 7 attempts
import random
random_num = random.randint(0, 129)
name = input("What's your name?\n")
i = 0
while 1:
  n = int(input("Guess the number between 0-128\n"))
  if n < random_num:
    print("It's too low!")
  elif n > random_num:
    print("It's too high!")
  else:
    print(f"Congratulations! {name} You guessed the number in {i+1} times!")
    break
  print(f"try: {i+1}\n")
  i+=1