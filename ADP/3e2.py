''' Write a python program to combine two list'''


def fun():
    l1=[]
    l2=[]
    l3=[]

    for i in range(1,9):
        l1.append(i)
    for i in range(10,0,-2):
        l2.append(i)
    for i in range(len(l2)):
        l3.append(l2[i]+l1[i])
    l3.append(len(l1)-len(l2))
    print(l3)

fun()
    


