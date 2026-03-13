# Add key value pairs to a Dictionary
student = {"name": "Rashi", "age": 20}
student["course"] = "CSE"
print(student)

#To check if key exits in a dictionary
student = {"name": "Rashi", "age": 20, "course": "CSE"}
key = input("Enter key to check: ")

if key in student:
    print("Key exists")
else:
    print("Key does not exist")