'''
In the modify tasks, you are given some starter code.
Use the instructions below to make changes to the code.
Comment your changes to explain what you have done.

Adapt the code to:
- Rename the function so that it has a sensible name. Don't forget to rename it when it is called.
- Call the function with the argument 'Sweden'.
- Get the user to input a country. Store it in a variable. Call the function again with the variable as the parameter.
'''
def i_am_from(country): # changed my_functiton to "i_am_from"
  print("I am from " + country)


i_am_from("Sweden")

country = input("Where are u from?\n") # ask to the user
i_am_from(country) # print I am from (input)


