n = int(input("Enter the number of tickets: "))

sum = 0
for i in range(n):
    age = int(input("Enter your age: "))
    if age < 18: price = 0
    elif 18 <= age <= 25: price = 990
    elif age > 25: price = 1390
    sum = sum + price

if n > 3: sum = sum*0.9

print(sum)

