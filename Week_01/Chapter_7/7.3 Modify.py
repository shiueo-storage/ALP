'''
In the modify tasks, you are given some starter code. Use the instructions below to make changes to the code. Comment your changes to explain what you have done.

Run the program to see how it works.
Adapt the code to:

1. Get user input into the number variable.
2. Change the print statement so it outputs 'number' multiplied by 'counter' equals 'product'
3. Make the counter increase by 2 every loop
4. Add a line once the loop has finished to output 'The loop has finished' '''

number = 6
counter = 1
import sys

number = int(sys.stdin.readline()) # get input from the user
while counter < 13:
  print(f"{number} * {counter} = {counter * number}") # changed print sentence
  counter +=2 # changed to increase by 2

print("The loop has finished") # output message

# ===================== extra =======================
num = int(input("give me any number"))
i = 0
until = int(input("to what? (number)"))
while i < until+1:
  print(f"{num} * {i} = {num * i}") 
  i+=1