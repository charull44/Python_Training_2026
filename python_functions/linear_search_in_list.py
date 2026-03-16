mylist = [5, 2, 9, 7, 5, 6]

def searchElement(target):
    for i in range(len(mylist)):
        if target == mylist[i]:
            return i
    return -1

result = searchElement(10)

if result != -1:
    print("Element found at index number =", result)
else:
    print("Element not found")