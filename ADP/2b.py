'''2b) Write a python program to find area of square, rectangle and circle using user defined functions. Take input from the user and print the results'''

def square(a):
    area=a*a
    print("The area of square is "+str(area) )
def rectangle(a,b):
    area=a*b
    print("The area of rectangle is "+str(area) )
def circle(r):
    area=3.14*r**2 
    print("The area of circle is "+str(area) )

print("choice available to find the area of the given shape:\n 1.Square\n2.Rectangle\n3.Circle")
choice=int(input("Enter the choice: "))

match choice:
    case 1:
        a=float(input("Enter the edge: "))
        square(a)

    case 2:
        a=float(input("Enter the length of the edge: "))
        b=float(input("Enter the breadth of the edge: "))
        rectangle(a,b)

    case 3:
        r=float(input("Enter the radius of the circle: "))
        circle(r)

    case _:
        print("Invalid option")

