
'''a) Write a program using a for loop to print factorial of a given number'''

num=int(input("Enter a number to find it's factorial: "))

factorial=1

for i in range(1,num+1):
    factorial=factorial*i

print("The factorial of "+str(num)+" is "+str(factorial))



'''if(num==0 or num==1):
    factorial=1
else:
    for loop'''