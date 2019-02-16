import math
a = float(input("Enter a value:   "))
b = float(input("Enter b value:   "))
c = float(input("Enter c value:   "))
z = math.sqrt(b ** 2 - 4 * a * c)
x1 = (-1 * b + z)/(2 * a)
x2 = (-1 * b - z)/(2 * a)
if b ** 2 < 4 * a * c:
    print("Invalid - Negative discriminant")
elif 2 * a == 0:
    print("Invalid - Zero denominator")
else:
    print("Works! Your zeroes are:")
    if x1 == x2:
        print ('single root=')
        print (x1)
    else:
        print('x1=')
        print(x1)
        print('x2=')
        print(x2)
# b has to be largest value to avoid negative discriminant
