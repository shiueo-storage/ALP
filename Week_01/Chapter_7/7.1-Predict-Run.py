# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
answer = input()  # ask the question and get the input from the user

while (
    answer != "Paris"
):  # keep saying you are wrong until user type "Paris" and press the enter.
    print("Incorrect! Try again.")
    answer = input("What is the capital of France?")

print("Correct!")  # if the input was "Paris" the loop breaked and print "Correct!"

# Example code 2

counter = 1

while counter < 5:
    print("This code is inside the loop")  # print this sentence for 4 times
    counter += 1
