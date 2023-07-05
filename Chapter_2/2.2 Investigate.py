### Example Code 1

fName = "Mr"
lName = "Colley"

print(fName)

# Identify a variable in the code
# Answer: fName and lNme

# Identify a string in the code
# Answer: "Mr" and "Colley"

# Line 4 is changed to lName = "Thorpe".  How does this affect the output?
# Answer: this will not change the output because lName didn't used in the code.

# Line 3 is changed to fName = "Mrs". How does this affect the output?
# Answer: output would be change as "Mr" -> "Mrs"


### Example Code 2

num1 = 20
num2 = 5

total1 = num1 + 15
total2 = num2 * 2
total3 = num1 - num2

print(total3)

# What will be output by the program?
# Answer: 15
# because variable total3 only affected by num1 and num2, and they didn't changed


### Example Code 3

name1 = "Ross"
name2 = "Monica"
name3 = "Joey"
name4 = "Rachel"
name5 = "Chandler"

print(name1 + " and " + name4)
print(name3)

name3 = "Phoebe"

# How many variables are used in the program?
# Answer: 5

# What would be the impact of changing  print(name1, " and ", name4) to print(name1, " and ", name5) ?
# Answer: Ross and Chandler

# What is the purpose of the '+' symbol in  print(name1, " and ", name4) 
# Answer: It merges the given strings. in order. Also, with '+' symbol it doesn't add spaces between them.

# The line  print(name3) is added to the end of the code.  Explain what it will do.
# Answer: it will print "Phoebe"