'''c) Write a python program to check different function parameters'''


def fun(x=2,y=3):
    x=x+y
    y+=2
    print(x,y)

fun()
fun(10,5)
fun(8)
