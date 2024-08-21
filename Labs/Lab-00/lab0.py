# CIS 103: Introduction to Programming 
# Lab 00: "Hello, World!" 
# Instructor: Md Ali
# Date: 08/21/2024
# 
# This script is a simple Python program that prints "Hello, World!" to the
# console. It is designed to introduce students to basic Python syntax, 
# including how to write comments, define a main function, and print 
# output to the console. 
#
# This single-line comment. Comments are ignored by the Python interpreter.
# These are typically used to add explanation or notes within your code. 
# Make sure to always have the first four lines I've commented in your code, 
# so other developers can know who made this code as well as the date, 
# descriptions, etc. 
#
# The print() function is used to display output to the console. 
# The following line of code will print the string "Hello, World!" when 
# executed. 

def main():
    # The print() function outputs text to the console. 
    # In this case, it outputs the string "Hello World!".
    print("Hello, World!") # This is an inline comment, explaining this line

    # This if __name__ == "__main__": block is used to ensure that the main() 
    # function is called only when this script is executed directly, and not 
    # when it is imported as a module. 

if __name__ == "__main__":
    main() # This line calls the main() function to execute the code within
        
