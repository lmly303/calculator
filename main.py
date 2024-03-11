print("Welcome to my calculator")
a =int(input("Enter the first number : "))
b =int(input("Enter the second number : "))
status = input("Enter the operatin you want to perform (+,-,*,/) : ")
def operation(status):
    match status:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            if b != 0:
                return a / b
            else:
                 return "Error: Division by zero"
        case _:
            return "Invalid operation"


r = operation(status)
print("Result:", r)
