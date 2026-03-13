name = "Charul"
newname = ""

for i in name:
    if i not in newname:
        newname += i
print(name)
print(newname)

#--------------
#Reverse String
#---------------
name = "Charul"
rev = ""

for i in name:
    rev = i + rev

print(rev)