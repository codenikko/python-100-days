def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



num1 = float(input("enter number : "))
a = num1

go_again = True
while go_again:
    
    op = input("Enter operand :")
    num2 = float(input("Enter number: "))
    
    # dictionary values working as functions, so we can use parameters to call 
    # the function here
    num1 = operations[op](num1, num2)

    print(f"{a} {op} {num2} = {num1}")
    a = num1
    repeat=input("continue calculation? [y/n]").lower()

    if repeat == "y":
        go_again= True
    elif repeat == "n":
        print("The final answer is: ", num1)
        go_again= False
    
    
