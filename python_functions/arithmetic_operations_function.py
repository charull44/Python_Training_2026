def add():
    n1 = int(input("Enter the value of n1: "))
    n2 = int(input("Enter the value of n2: "))
    
    sum = n1 + n2
    mul = n1 * n2
    sub = n1 - n2
    div = n1 / n2
    
    return sum, mul, div, sub

result = add()
print(result)