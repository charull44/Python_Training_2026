# Program to calculate percentage and check placement eligibility

m1 = int(input("Enter marks of paper 1: "))
m2 = int(input("Enter marks of paper 2: "))
m3 = int(input("Enter marks of paper 3: "))

total = m1 + m2 + m3
percentage = total / 3.0

print("Total marks:", total)
print("Percentage:", percentage)

if percentage >= 60:
    print("Eligible for placements")
else:
    print("Not eligible")