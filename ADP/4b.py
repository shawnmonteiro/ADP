'''b)For a given list num=[45,22,14,65,97,72], write a python program to replace all the integers divisible by 3 with “ppp” and all integers divisible by 5 with “qqq” and replace all the integers divisible by both 3 and 5 with “pppqqq” and display the output.
'''

num=[45,22,14,65,97,72]

for i in range(len(num)):
    if(num[i]%3==0) and (num[i]%5==0):
        num[i]="pppqqq"
    elif(num[i]%3==0):
        num[i]="ppp"
    elif(num[i]%5==0):
        num[i]="qqq"
print(num)

