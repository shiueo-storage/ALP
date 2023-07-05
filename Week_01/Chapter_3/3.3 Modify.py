
"""Given Code
name = "Billy"
print("We want to know if you like progamming!")
print()
print("Do you like programming " + name + "?")
answer = input()
print("Great! You said " + answer + "!")
print("Let's learn some Python today")
"""

import sys # sys.stdin.readline() is usually faster than input(), cuz input() has more processes internally, and separate each inputs to several buffers, but sys.stdin.readline() do nothing with input and just put everything in one buffer
print("What's your name?")
name = sys.stdin.readline().strip()
print(f"We want to know if you like progamming!\nDo you like programming, {name}?")
answer = sys.stdin.readline().strip()
print(f"Great! You said {answer}!\nLet's learn some Python today!")

