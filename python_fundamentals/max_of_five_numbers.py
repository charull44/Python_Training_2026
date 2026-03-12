# Program to accept five numbers and find the maximum

a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))
c = int(input("Enter value 3: "))
d = int(input("Enter value 4: "))
e = int(input("Enter value 5: "))

if a > b and a > c and a > d and a > e:
    print("a is maximum")

elif b > a and b > c and b > d and b > e:
    print("b is maximum")

elif c > a and c > b and c > d and c > e:
    print("c is maximum")

elif d > a and d > b and d > c and d > e:
    print("d is maximum")

else:
    print("e is maximum")