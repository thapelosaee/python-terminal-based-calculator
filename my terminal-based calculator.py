#python calculator

operator = input("enter an operator(+ - * /) ")# user enters an operator
num1 = float(input("enter the 1st number:"))
num2 = float(input("enter the 2nd number:"))

if operator == "+":# if they chose addition then add the first input and second
    result = num1 + num2
    print(result)
elif  operator == "-": # if they chose subtraction then minus the first input with the second
    result = num1 - num2
    print(result)
elif  operator == "*":# if they chose amultiplication then multiply the first input and second
    result = num1 * num2
    print(result)
elif  operator == "/":# if they chose division then divide the first input and second
    result = num1 /  num2
    print(result)
else:# if the user enters an operator that is not available, print the following
    print(f" {operator} is not a valid operator")