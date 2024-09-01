# Triangle Classifier:
# equilateral tiangle - all sides are equal, isoceles triangle - two sides are equal, scalene - no sides are equal
a=float(input("Enter side a: "))
b=float(input("Enter side b: "))
c=float(input("Enter side c: "))

if a == b == c:
    print ("Equilateral")
elif a == b or b == c or a == c:
    print ("Isoceles")
else:
    print("Scalene")