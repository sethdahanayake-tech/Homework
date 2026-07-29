number = int(input("Enter the number: "))
n = int(input("Enter the power (n): "))

result = 1

for i in range(n):
    result *= number

print(f"{number}^{n} = {result}")

