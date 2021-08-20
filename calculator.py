import sys
import os
from calculator_logo import logo

def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2


def main(n1,n2,operation):
    if operation =='+':
        return addition(n1,n2)
    elif operation == '-':
        return subtraction(n1,n2)
    elif operation == '*':
        return multiplication(n1,n2)
    elif operation =='/':
        return division(n1,n2)
    else:
        return "Enter a valid arithmatic operation"

os.system('clear')
print(logo)

while True:
    fresh_calculation = 'n'
    x = int(input("What is the first number?\n"))
    while True:
        if fresh_calculation == 'y':
            break
        while True:
            o = input("+\n-\n*\n/\nPick and dopepration: ")      
            y = int(input("What is the next number?\n"))
            if o == '/' and y == 0:
                print("Denominator cannot be 0, enter again")
                continue
            break
        result = main(x,y,o)
        print('{} {} {} = {}'.format(x,o,y,result))
        while True:
            resume = input("Type y to continue calculating with {}, type 'n' to start a new calculation or type 'q' to quit the calculator\n".format(result))
            if resume == 'y':
                x=result
                break
            elif resume == 'n':
                fresh_calculation = 'y'
                os.system('clear')
                break
            elif resume == 'q':
                sys.exit()
            else:
                print("Please enter either 'y', 'n' or 'q'\n")
                continue

