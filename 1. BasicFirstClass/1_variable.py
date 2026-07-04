# variable is a named storage location in memory 
# Variable is case sensitive

name = "chandan"
age = 24
Batch = "july26"

print(name)
print(age)
print(Batch)


# Naming rules for variable
# 1. Variable names can only contain letters, numbers, and underscores
# 2. Variable names cannot start with a number
# 3. Variable names cannot contain spaces
# 4. Variable names are case sensitive

# Data types in python
# 1. int - integer : age = 24
# 2. float - decimal number : weight = 65.5
# 3. str - string : name = "chandan"
# 4. bool - boolean (True or False) : is_student = True
# 5. list - ordered collection of items : fruits = ["apple", "banana", "cherry"]
# 6. tuple - ordered collection of items (immutable) : coordinates = (10, 20)
# 7. set - unordered collection of unique items : unique_numbers = {1, 2, 3}
# 8. dict - collection of key-value pairs : person = {"name": "chandan", "age": 24}
# 9. NoneType - represents the absence of a value : result = None

age = 24
weight = 65.5
name = "chandan"
is_student = True
fruits = ["apple", "banana", "cherry"]
coordinates = (10, 20)
unique_numbers = {1, 2, 3}
person = {"name": "chandan", "age": 24}
result = None

print(type(age))          # <class 'int'>
print(type(weight))       # <class 'float'>
print(type(name))         # <class 'str'>
print(type(is_student))   # <class 'bool'>
print(type(fruits))       # <class 'list'>
print(type(coordinates))  # <class 'tuple'>
print(type(unique_numbers)) # <class 'set'>
print(type(person))       # <class 'dict'>
print(type(result))       # <class 'NoneType'>  





# taking input from user and type casting
# converting one data type to another
# 1. int() - converts to integer
# 2. float() - converts to float
# 3. str() - converts to string

# name = input("Enter your name: ")
# print("Hello, " + name + "!")

# # age = int(input("Enter your age: "))
# print("You are " + str(age) + " years old.")

# # weight = float(input("Enter your weight: "))
# print("Your weight is " + str(weight) + " kg.")

# # height = float(input("Enter your height: "))
# print("Your height is " + str(height) + " cm.")


# Invalid type casting
age = int("twenty-four")  # This will raise a ValueError
weight = float("sixty-five point five")  # This will raise a ValueError