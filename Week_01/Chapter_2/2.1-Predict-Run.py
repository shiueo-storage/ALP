# Predict and Run Example 1
# Add comments to the code below to explain what it does

firstName = "Andy"

print(firstName)

"""
There is a object that containing the string Andy, and the variable 'firstName' points to the memory where object located. and the statement print, get a string from the variable 'firstName(the loc of memory)' then it printed out.
"""

# Predict and Run Example 2
# Add comments to the code below to explain what it does

lastName = "Colley"

fullName = firstName + " " + lastName

print(fullName)
"""
As the string type on python is an "immutable", the string object stored in lastName variable added with " " string (also located on an another memory) and it added to lastName variable and it create a new object that containing the string which firstName was pointing and " " with the string which was pointed by the lastName. and it printed out.
"""

# Predict and Run Example 3
# Add comments to the code below to explain what it does

print("Hello " + firstName + ". Your full name is " + fullName + ".")

"""
It's same as the above one (Predict and Run Example 2)
"Hello " string object created, the object pointed by variable firstName merged to it, ". Your full name is " does the same things again, fullName, "." does same too. and it printed.
"""
