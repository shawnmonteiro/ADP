'''a) Write a python program that takes a list of words and returns the length of longest one'''

n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    ele=input("enter the words: ")
    l.append(ele)
print(l)
max=len(l[0])
temp=l[0]
for i in l:
    if len(i)>max:
        max=len(i)
        temp=i

print("The element is "+str(temp) +" with the  length "+str(max))

