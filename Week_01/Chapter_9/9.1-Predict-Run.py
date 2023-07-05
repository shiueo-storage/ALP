# Example Code 1


def say_hi():
    print("Why hello there!")


def offer_drink():
    print("Would you care for a spot of tea?")


def offer_food():
    print("Biscuit?")


def say_bye():
    print("Cheerio then.")


offer_drink()  # run the subroutine offer_drink() -> print("Would you care ---")
say_hi()  # run the subroutine say_hi() -> print("Why hello there?")
offer_food()  # run the subroutinee offer_food() -> print("Bisquit.")

# Example code 2
def maths1():
    num1 = 50
    num2 = 5
    return num1 + num2


def maths2():
    num1 = 50
    num2 = 5
    return num1 - num2


def maths3():
    num1 = 50
    num2 = 5
    return num1 * num2


outputNum = maths2()  # set variable outputNum as the subroutine maths2()
print(outputNum)  # run the subroutine outputNum (actually maths2)

# Example Code 3
def location(country):
    print("I am from " + country)


location(
    "Brazil"
)  # it passes the string "Brazil" as the argument. so it will print : I am from Brazil
