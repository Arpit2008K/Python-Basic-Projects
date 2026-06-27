import math
from datetime import datetime
import random

history={}
last_result=None

def add():
    a=float(input("Enter First Number:"))
    b=float(input("Enter Second Number:"))
    result=a+b
    print("Additon is:",result)
    global last_result
    last_result=result

def subtract():
    a=float(input("Enter First Number:"))
    b=float(input("Enter Second Number:"))
    result=a-b
    print("Subtraction is:",result)
    global last_result
    last_result=result

def multiply():
    a=float(input("Enter First Number:"))
    b=float(input("Enter Second Number:"))
    result=a*b
    print("Multiplication is:",result)
    global last_result
    last_result=result

def divide():
    try:
        a=float(input("Enter First Number:"))
        b=float(input("Enter Second Number:"))
        result=a/b
        print("Divison is:",result)
        global last_result
        last_result=result
    except ZeroDivisionError:
        print("Cannot divide by zero")


while True:
    try:
        print()
        print("Enter 1 for Basic Arithmetic")
        print("Enter 2 for Scientific Calculations")
        print("Enter 3 for Generate Random Numbers")
        print("Enter 4 for Store Results in Dictionary")
        print("Enter 5 to view history")
        print("Enter 6 to Exit")
        ch=int(input("Enter your choice:"))
        print()

        if ch==1:
            print("Enter 1 to Add")
            print("Enter 2 Subtract")
            print("Enter 3 to Multiply")
            print("Enter 4 to Divide")
            print("Enter 5 to return Main-Menu")
            z=int(input("Enter your choice:"))
            if z==1:
                add()
            elif z==2:
                subtract()
            elif z==3:
                multiply()
            elif z==4:
                divide()
            elif z==5:
                print("Returning to Main-Menu")
            else:
                print("Enter a valid choice!")

        elif ch==2:
            print("Enter 1 for Square Root")
            print("Enter 2 for Power")
            print("Enter 3 for Factorial")
            print("Enter 4 to return Main-Menu")
            z=int(input("Enter your choice:"))
            if z==1:
                a=float(input("enter a number:"))
                if a<0:
                    print("Enter a positive number!")
                else:
                    sqrt=math.sqrt(a)
                    print("Square root is:",sqrt)
                    last_result=sqrt

            elif z==2:
                a=float(input("Enter base:"))
                b=float(input("Enter power:"))
                result=math.pow(a,b)
                print("Result:",result)
                last_result=result

            elif z==3:
                a=int(input("Enter a number:"))
                fact=math.factorial(a)
                print("Factorial is:",fact)
                last_result=fact
            elif z==4:

                print("Returning to Main-Menu")

            else:
                print("Enter a valid choice!")

        elif ch==3:
            a=int(input("Enter starting number:"))
            b=int(input("Enter last number:"))
            r=random.randint(a,b)
            print("Random numbers between the given range:",r)
            last_result=r
        
        elif ch==4:
            if last_result is None:
                print("No result available to store")
            else:
                timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                history[timestamp]=last_result
                print("Result stored successfully.")
        elif ch==5:
            if history=={}:
                print("No result stored")
            else:
                for i in history:
                    print("Time:",i,"Result:",history[i])
        elif ch==6:
            print("Exiting.....")
            break
        else:
            print("Enter a valid choice!")
    except ValueError:
        print("Give Proper Inputs")