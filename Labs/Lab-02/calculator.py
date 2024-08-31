# CIS 103: Introduction to Programming 
# Lab 01: "Calculator Function" 
# Instructor: Md Ali
# Date: 08/31/2024
# 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y): 
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero!." 

def main():

    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '5':
            print("exiting, thank you!")
            break
        
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} + {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} + {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} + {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input") 
            
if __name__ == "__main__":
    main()
        
