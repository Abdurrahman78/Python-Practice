# implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z,
#with one space between x and y and one space between y and z, wherein:

#x is an integer
#y is +, -, *, or /
#z is an integer
#For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

#get input string
equation=input("Expression: ")

#since we want to handle each character seperatly seaperate them upon space
newArray=equation.split(" ")

#now that we split them into a array, extract each value and operator into a varaible to be used later, convert string numbers into floats
firstValue=float(newArray[0])
operator=newArray[1]
secondValue=float(newArray[2])

#now since we want to perform calculations we should do it based on what the operator is
match operator:
    case '+':
        print(firstValue + secondValue)
    case '-':
        print(firstValue - secondValue)
    case '/':
        print(firstValue / secondValue)
    case '*':
        print(firstValue * secondValue)
    case _:
        print("Please enter a valid operator")

