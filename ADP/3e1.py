'''a) Write a python program to check if a number is palindrome or not  using user defined functions'''


num=int(input("Enter a number: "))
temp=num
rev=0
next=10
while(num!=0):
    r=num%10
    rev=rev*next+r
    num=num//10

if(rev==temp):
    print("The given number "+str(temp)+" is a palindrome.")
else:
    print("The given number "+str(temp)+" is not a palindrome.")