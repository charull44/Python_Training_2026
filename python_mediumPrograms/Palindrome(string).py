# Check for Palindrome (string)

name = input("Enter a string: ")
rev = ""

for i in name:
    rev = i + rev

if name == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# Another approach
name = "racecare"
if name == name[::-1]:
    print("Palindrome")
else:
     print("Not Palindrome")