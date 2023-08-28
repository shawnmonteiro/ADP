'''b) Collatz Sequence: Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value.If  Number is odd, then collatz() should print and return 3 * number + 1. Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.'''

import sys

def collatz(num):
    if (num%2==0):
        value=num//2
    if (num%2!=0):
        value=(3*num)+1
    
    while value==1:
        print(value)
        sys.exit()

    if value!=1:
        print(value)
        num=value
        collatz(value)
        


print("Enter the number to find the collatz sequence: ")
response=input('>')
if(response==0 or not response.isdecimal()):
    print("Please input in the number greater than 0")
else:
    conum=int(response)
    print(conum)
    if (conum==1):
        print("Please enter a number greater than 1.")
        sys.exit()
    collatz(conum)













'''def collatz(n):
  if n>1:
    steps=0
    while n!=1:
      if n%2==0:
        print(int(n//2))
        n=n//2
        steps+=1
      else:
        print(int(3*n+1))
        n=n*3+1
        steps+=1
    print("collatz sequence finished in {} steps".format(steps))
  else:
    print("please enter a number greater than 1:")

n=int(input("choose any integer greater than 1:"))
collatz(n)'''









'''import sys
def collatz(numb):
    if numb % 2 == 0:  # Remainder = 0, Checks for even number
        value = numb // 2
    elif numb % 2 != 0:  # Remainder = 1, Checks for odd number
        value = (numb*3)+1

    while value == 1:  # If value is 1
        print(value)
        sys.exit()  # Program exits

    while value != 1:  # The loop runs until the value is not 1.
        print(value)
        numb = value  # Value of value is copied to numb
        return collatz(numb)


print('Enter a starting number (greater than 0) or QUIT:')
response = input('> ')  
if response == '0' or not response.isdecimal():
    print('You must enter positive integer greater than 0.')
else:
    numb = int(response)
    print(numb)
    if numb == 1:  # If valuee is 1
        print("Given input should be greater than 1")
        sys.exit()  # Program exits
    collatz(numb)
'''
    