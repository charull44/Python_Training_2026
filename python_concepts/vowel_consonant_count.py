# Program to count vowels and consonants in a string

name = "Charul"

v = 0
c = 0

for i in name:
    if i in "aeiouAEIOU":
        v += 1
    else:
        c += 1

print("Vowels:", v)
print("Consonants:", c)