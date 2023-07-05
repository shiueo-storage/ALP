'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''


weapons = ["sword", "katana", "pistol", "rifle", "grenade", "flamethrower"]
zombieWeakness = weapons[2]
print("You have encountered a zombie and should prepare to fight.")
print(f"Here's your weapons.\n{', '.join(weapons)}")
while 1:
  tmp = 0
  print("\ntype 1 to use one from the list, or type 2 to pick your own weapon.")
  user_weapon = input()
  if user_weapon == "1":
    input_weapon = input(f"give your weapon name in the list.\n{', '.join(weapons)}\n\n")
    if input_weapon not in weapons:
      tmp = 0
    else:
      tmp=1
  elif user_weapon == "2":
    input_weapon = input("give your own weapon's name\n")
    weapons.append(input_weapon)
    tmp=1
  else:
    tmp=0
  if input_weapon == zombieWeakness:
    print("You won!")
    break
  else:
    if tmp == 1:
      print('You have lost...')
    else:
      print("You typed wrong things.")