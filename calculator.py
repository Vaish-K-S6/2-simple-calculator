print("🧮 Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("+  Add")
print("-  Subtract")
print("*  Multiply")
print("/  Divide")

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operation")
