#Modular Calculator Version 1
def add_numbers(num1, num2):
    return num1 + num2
def subtract_numbers(num1, num2):
    return num1 - num2
def multiply_numbers(num1, num2):
    return num1 * num2
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

#Main Program
print ("Modular Calculator")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
print("\nChoose operation: ")
print("1-Addition | 2-Subtraction | 3-Multiplication | 4-Division")
opt = int(input("Enter choice: "))
if opt == 1:
    res = add_numbers(first, second)
elif opt == 2:
    res = subtract_numbers(first, second)
elif opt == 3:
    res = multiply_numbers(first, second)
elif opt == 4: 
    res = divide_numbers(first, second)
else:
    res = "Invalid Choice"
print(f"Result: {res}")
