# Python Calculator

operator = input("Enter an operator: (+  -  *  / )")

num1 = float(input("Enter the 1st No.:"))
num2 = float(input("Enter the 2nd No.:"))

if operator == "+":
    a=num1+num2
    print(f"The addition of two number is {a}")
elif operator == "-":
    a=num1-num2
    print(f"The subtraction of two number is {a}")
elif operator == "*":
    a=num1*num2
    print(f"The multiplication of two number is {a}")
elif operator == "/":
    a=num1/num2
    print(f"The division of two number is {a}")
else:
    print("Choose from above operator only!!!")
