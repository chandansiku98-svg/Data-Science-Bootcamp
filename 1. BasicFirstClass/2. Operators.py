 # 1. Arithmetic Operators
# +, -, *, /, %, **, //- floor division, 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Modulus: ", a % b)
print("Exponentiation: ", a ** b)
print("Floor Division: ", a // b) # floor division returns the largest integer less than or equal to the division result


# 2. Assignment Operators
# =, +=, -=, *=, /=, %=, **=, //=

x = 10
x += 5  # x = x + 5
print("x after += 5: ", x)

x -= 3  # x = x - 3
print("x after -= 3: ", x)

x *= 2  # x = x * 2
print("x after *= 2: ", x)

x /= 4  # x = x / 4
print("x after /= 4: ", x)

x %= 3  # x = x % 3
print("x after %= 3: ", x)

x **= 2  # x = x ** 2
print("x after **= 2: ", x)


# 3. comparison Operators
# ==, !=, >, <, >=, <=


print(16==12) # False
print(16!=12) # True
print(16>12) # True
print(16<12) # False
print(16>=12) # True
print(16<=12) # False

#if-else statement
age = int(input("Enter your age: "))
if age >= 18:      # : is used to indicate the start of a block of code - indentation
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#elif statement - elif is used to check multiple conditions

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("You got A grade.")
elif marks >= 80:
    print("You got B grade.")
else:
    print("You got C grade.")   




# 4. conditional Operators
# and, or, not

print(True and True) # True    # and - returns True if both statements are true
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True     # or - returns True if one of the statements is true
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False        # not - returns True if the statement is false
print(not False) # True