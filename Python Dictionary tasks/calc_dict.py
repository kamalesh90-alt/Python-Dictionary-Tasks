def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    operations = {
        1: add,
        2:  subtract,
        3:  multiply,
        4: divide
    }
    
    print("Enter two numbers:")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    print("\nChoose an operation:")
    print('1.addition')
    print('1.subtraction')
    print('1.multiplication')
    print('1.division')

    
    choice = int(input("Enter your choice: "))
    
    if choice in operations:
        operation_function = operations[choice]
        result = operation_function(num1, num2)
    else:
        result = "Invalid choice!"
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()
