# Demonstration of dictionary operations

mydict = {
    101: "Charul",
    102: "Chhaya",
    103: "Chahat",
    104: "Charvi"
}

print(mydict)

a = mydict[102]
print(a)

for x in mydict:
    print(x)

for x in mydict.values():
    print(x)

for x, y in mydict.items():
    print(x, y)

mydict["mobile_no"] = 9921778950
print(mydict)