count = 0

for i in range(1, 1000):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
        print(f"{i} is divisible by both 3 and 5")
    elif i % 3 == 0:
        count += 1
        print(f"{i} is divisible by 3")
    elif i % 5 == 0:
        count += 1
        print(f"{i} is divisible by 5") 




# nasted loop