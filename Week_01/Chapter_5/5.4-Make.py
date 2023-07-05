import sys

print("Give me a grade between 1 and 100")  # print questions
grade = int(sys.stdin.readline())  # get input from the user
if grade > 100 or grade < 1:  # define ranges. else, exit the program
    print("The number you entered is too high or too low.")
    sys.exit()
Fail = None  # make a variable as instructed
if grade < 40:  # if grade is lesser than 40, Yes. Failed
    Fail = "Y"
else:  # else PASS
    Fail = "N"

if Fail != "N":  # prints the grade
    print("Retake required. You are 'U' grade")
else:
    if grade < 69:
        print("PASS. You are a 'C' grade")
    elif grade < 80:
        print("PASS. You are a 'B' grade")
    else:
        print("Congratulations. You are an 'A' grade")
