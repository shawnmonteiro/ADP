'''extra 2: Write a python program to build SIMPLE CALCULATOR using user defined functions'''

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def rem(a, b):
    return a % b

print('''Select your choice:
      1.Addition
      2.Subtraction
      3.Multiplication
      4.Division
      5.Remainder
      6.Exit''')

while True:
    choice = input("Enter your choice: ")
    
    if choice == '6':
        print("Exiting the calculator.")
        break
    
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == '1':
            print(str(num1) + "+" + str(num2) + "=" + str(add(num1, num2)))
        elif choice == '2':
            print(str(num1) + "-" + str(num2) + "=" + str(sub(num1, num2)))
        elif choice == '3':
            print(str(num1) + "*" + str(num2) + "=" + str(mul(num1, num2)))
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(str(num1) + "/" + str(num2) + "=" + str(div(num1, num2)))
        elif choice == '5':
            print(str(num1) + "%" + str(num2) + "=" + str(rem(num1, num2)))
    else:
        print("Invalid option. Please select a valid choice.")

#without  a while loop
'''def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def rem(a, b):
    return a % b

print("Select your choice:
      1.Addition
      2.Subtraction
      3.Multiplication
      4.Division
      5.Remainder
      6.Exit")

choice = input("Enter your choice: ")
    
if choice == '6':
    print("Exiting the calculator.")
    
if choice in ('1', '2', '3', '4', '5'):
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        
    if choice == '1':
        print(str(num1) + "+" + str(num2) + "=" + str(add(num1, num2)))
    elif choice == '2':
        print(str(num1) + "-" + str(num2) + "=" + str(sub(num1, num2)))
    elif choice == '3':
        print(str(num1) + "*" + str(num2) + "=" + str(mul(num1, num2)))
    elif choice == '4':
        if num2 == 0:
             print("Cannot divide by zero.")
        else:
            print(str(num1) + "/" + str(num2) + "=" + str(div(num1, num2)))
    elif choice == '5':
        print(str(num1) + "%" + str(num2) + "=" + str(rem(num1, num2)))
    else:
        print("Invalid option. Please select a valid choice.")
'''