# Importing libraries
import toml

# Defining functions


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


def squared(x):
    return x**2


def exppower(x, y):
    return x**y

# Creating a looping statement that breaks when you don't want to perform another calculation
while True:

    # Printing possible selections for calculator input types
    print("Select operation.\n"
          "1.Add\n"
          "2.Subtract\n"
          "3.Multiply\n"
          "4.Divide\n"
          "5.Second Power\n"
          "6.Exponential Power\n")

    # Taking input from user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # Checking if choice is one of the options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number:\n"))
        num2 = float(input("Enter second number:\n"))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    # Checking if choice wants product to the second power, or exponential power
    elif choice in ('5', '6'):
        num1 = float(input("Enter number:\n"))
        if choice == '5':
            print(num1, "**", '2', "=", squared(num1))
        elif choice == '6':
            num2 = int(input("Enter power:\n"))
            print(num1, "**", num2, "=", exppower(num1, num2))

    # Checking if user wants another calculation
    next_calculation = input(
        "Let's do next calculation? (y/n):\n").capitalize()

    # Breaking the while loop if answer is no, returning the choices if answer is yes, and breaking the while loop if answer is invalid
    if next_calculation == "N":
        break
    elif next_calculation == "Y":
        print("You decide to calculate again.")
    else:
        print("Invalid choice!\n")
        break
