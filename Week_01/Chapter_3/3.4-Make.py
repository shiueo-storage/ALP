"""
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.
2. Greet the user by name.
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the 5. user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

"""

import sys

print("What's yout name?")
name = sys.stdin.readline().strip()
print(
    f"Welcome! We are thrilled to have you join us, {name}. \nIn order to enhance your user experience, we kindly request some additional details from you. \nWould you mind answering a few questions? Let's go!\n\n"
)

print("How old are you?")
age = sys.stdin.readline().strip()
print(f"Thank you. We've learned that you are {age} years old.")
print("\nWhat is your favorite animal?")
favAnimal = sys.stdin.readline().strip()
print(f"Thank you. We've learned that your favourite animal is {favAnimal}")
print("\nWhat field of study do you enjoy the most?")
favStudy = sys.stdin.readline().strip()
print(f"Thank you. We've learned that your favourite field of study is {favStudy}")
print("\nHow many hours of sleep do you get per day? (just a number)")
sleepHrs = sys.stdin.readline().strip()
print(f"Thank you. We've learned that your average sleep hours is {sleepHrs} hours")
print("\nWhat programming language do you like the most?")
favLang = sys.stdin.readline().strip()
print(f"Thank you. We've learned that your favourite programming language is {favLang}")

print("\n\nThank you for your response\n")

print(
    f"You, {name}, are {age} years old. \nYour favorite animal is the {favAnimal}, and you have a strong passion for the field of study in {favStudy}. \nYou typically get {sleepHrs} hours of sleep, and your preferred programming language is {favLang}!"
)

print("\n\nSummarized\n\n")
print("=======================================")
print(f"Name: {name}\n")
print(f"Age: {age}yrs")
print(f"Favorite Animal: {favAnimal}")
print(f"Favourite field of study: {favStudy}")
print(f"Sleep Hours: {sleepHrs}h")
print(f"Favourite Programming Languages: {favLang}")
print("=======================================")
