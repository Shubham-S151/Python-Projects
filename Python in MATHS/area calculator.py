print("Program to calculate the area of rectangle with length 'l' and breadth 'b'")
l=input("enter the value of length (l):-")
b=input("enter the value of breadth (b):-")
a=float(l)*float(b)
if float(l)==float(b):
    print("The given figure is SQUARE")
    print("The area of square =",a,"unit squares")
else:
    print("The given figure is RECTANGLE")
    print("The area of rectangle =",a,"unit square")