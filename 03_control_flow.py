# if, else and elif
x = int(input("your value: "))
if x > 3:
    print("Big")
elif x == 3:
    print("Medium")
else:
    print("Small")

# Loops
for i in [0,1,2]:
    print(i)

# Functions
def solde(x, percentage):
    return x - x * percentage / 100
print(solde(100, 5))
# 95

# Lambda
solde = lambda x, percentage: x - x * percentage / 100
print(solde(100,5))
# 95