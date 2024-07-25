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
        1: ("Addition", add),
        2: ("Subtraction", subtract),
        3: ("Multiplication", multiply),
        4: ("Division", divide)
    }
    
    print("Enter two numbers:")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    print("\nChoose an operation:")
    for key, (name, _) in operations.items():
        print(f"{key}) {name}")
    
    choice = int(input("Enter your choice: "))
    
    if choice in operations:
        operation_name, operation_function = operations[choice]
        result = operation_function(num1, num2)
    else:
        result = "Invalid choice!"
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()
    