# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# if a > b:
#     print(f"{a} is greater than {b}")
# else:
#     print(f"{b} is greater than {a}")


#take intput intger and check even and positive number


# a = int(input("Enter a number: "))

# if a > 0:
#     if a % 2 ==0:
#         print(f"{a} is a positive and even number") 
#     else:
#         print(f"{a} is a positive and odd number")
# else:
#     print(f"{a} is not a positive number")  



# password Authenticator

import re

print("=== Account Registration ===")
username = input("Enter your username: ")
password = input("Enter your password: ")

# 1. Validate Username Format
if not username.isalnum():
    print("❌ Registration Failed: Username must contain only letters and numbers.") 

# 2. Validate Password Format
      # Criteria: 
    # - At least 1 lowercase letter (?=.*[a-z])
    # - At least 1 uppercase letter (?=.*[A-Z])
    # - At least 1 digit/number (?=.*\d)
    # - At least 1 special character (?=.*[@$!%*?&])
    # - Minimum 8 characters long {8,}
     
else:
   
    password_criteria = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#_\-+])[A-Za-z\d@$!%*?&#_\-+]{8,}$"
    
    if re.match(password_criteria, password):
        print("✅ Success: Account created successfully!")
    else:
        print("❌ Registration Failed: Password does not meet security requirements.")
        print("\nYour password must include:")
        print("  • At least 8 characters")
        print("  • At least one uppercase letter (A-Z)")
        print("  • At least one lowercase letter (a-z)")
        print("  • At least one number (0-9)")
        print("  • At least one special character (e.g., @, $, !, %, *, ?, &)")



        # ===================================================


# Logical Opreater
# and or not
# and - returns True if both statements are true
# or  - returns True if one of the statements is true
# not - returns True if the statement is false


