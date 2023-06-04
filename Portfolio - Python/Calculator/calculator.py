#!/usr/bin/env python3

#this function adds two numbers
def add(x,y):
    return x+y

#this function subtracts two numbers
def subtract(x,y):
    return x-y

#this function multiplies two numbers
def multiply(x,y):
    return x*y

#this function divides two numbers
def divide(x,y):
    return x/y

#this function squares a number  
def squared(x):
    return x**2

#this function gets the exponential power
def exppower(x,y):
    return x**y



#creates a looping statement that breaks when you don't want to perform another calculation
while True:

    #print possible selections for calculator input types
    print("Select operation.\n"
      "1.Add\n"
      "2.Subtract\n"
      "3.Multiply\n"
      "4.Divide\n"
      "5.Second Power\n"
      "6.Exponential Power\n")

    #take input from user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    #check if choice is one of the options
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number:\n"))
        num2 = float(input("Enter second number:\n"))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1,num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))
            
    #check if choice wants a product to the second power
    elif choice in ('5'):
        num1 = float(input("Enter number:\n"))
        if choice == '5':
            print(num1, "**", '2', "=", squared(num1))

    #check if choice wants exponential power.
    elif choice in ('6'):
        num1 = int(input("Enter base number:\n"))
        num2 = int(input("Enter power:\n"))
        if choice == '6':
            print(num1, "**", num2, "=", exppower(num1,num2))

#check if user wants another calculation
    next_calculation = input("Let's do next calculation? (y/n):\n").capitalize()
    #break the while loop if answer is no
    if next_calculation == ("N").capitalize():
        break
    #return the the choices
    elif next_calculation == ("Y").capitalize():
         print("You decide to calculate again.")
    #break the while loop if answer is invalid
    else:
        print("Invalid choice!\n")
        break
        
        