# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)
import sys
print("Perimeter Calc")
print("=============================")
print("Please input two integers which mean width and height with a space")
W, H = map(int, sys.stdin.readline().split())
print(f"The perimeter of your rectangle is {2*(W+H)}")
print("\n\n")
print("Restaurant Tip Calc")
print("=============================")
print("What's your meal's price?")
price = int(sys.stdin.readline())
print(f"TIP: {int(price*0.2)}, TOTAL: {int(price*0.2) + price}")
print("\n\n")
print("Volume and Surface Calc ")
print("=============================")
print("Give us the width, length and heigh, separated by space")
W, L, H = map(int, sys.stdin.readline().split())
print(f"VOLUME: {W*H*L} and the total surface area is {2*(W*H) + 2*(W*L) + 2*(L*H)}")


'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''