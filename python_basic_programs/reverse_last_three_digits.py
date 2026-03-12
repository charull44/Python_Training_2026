# Program to reverse the last three digits of a number

num = 1234567
print("Original number:", num)

a = num % 10
num = num // 10

b = num % 10
c = num // 10

rev = a * 100 + b * 10 + c * 1

print("Reversed digits:", rev)