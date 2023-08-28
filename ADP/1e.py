'''a) Write a program to check if the given number is PRIME or Not'''

num=int(input("Enter the number to check if it is a prime number or not: "))

if (num==1 or num==0):
    print("The given number "+str(num)+" is not a prime number.")

count=0

for i in range(2,num+1):
    if num%i==0:
        count+=1

if count==1:
    print("The given number "+str(num)+" is a prime number.")

else:
    print("The given number "+str(num)+" is not a prime number.")


'''if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,'is not a PRIME number')
            break
    else:
        print(num,'is a prime number')    
else:
    print(num, "is not a prime number")
'''