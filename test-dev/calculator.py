num_1 = input("Enter a Number: ")
operation=input("Enter an operation: ")
num_2 = input("Enter another Number: ")



def calculator_main(num1,op,num2):
    if op == "+":
        return float(num1) + float(num2)
    if op == "-":
        return float(num1) - float(num2)
    if op == "*":
        return float(num1) * float(num2)
    if op == "/":
        return float(num1) / float(num2)
    else:
        return "Please enter valid inputs"

print(calculator_main(num_1,operation,num_2))