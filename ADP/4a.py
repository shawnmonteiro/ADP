'''a) Write a python program to accept N numbers from the user. Find and display sum of all even numbers and product of all odd numbers in entered list.'''

'''num=int(input("Enter a number:"))
sum=0
product=1
for i in range(1,num+1):
    if(i%2==0):
        sum+=i
    else:
        product*=i

print("the sum of all even numbers is"+str(sum))
print("the product of all odd numbers is"+str(product))'''


n=int(input("Enter a number:"))
l=[]

for i in range(n):
    ele=int(input("enter the number:"))
    l.append(ele)
sum=0
product=1
for i in l:
    if(i%2==0):
        sum+=i
    else:
        product*=i
print(l)
print("the sum of all even numbers is"+str(sum))
print("the product of all odd numbers is"+str(product))