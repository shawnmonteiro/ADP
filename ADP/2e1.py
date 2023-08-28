''' extra 1: Write a python program to swap two user input numbers using user defined functions'''

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

num1=int(input("Enter the first number, a: "))
num2=int(input("Enter the second number, b: "))

num1,num2=swap(num1,num2)

print("a="+str(num1))
print("b="+str(num2))
