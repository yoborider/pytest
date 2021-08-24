# Numerical Data Types and Structures
x, y = 3, 2
print(x + y) # = 5
print(x - y) # = 1
print(x * y) # = 6
print(x / y) # = 1.5
print(x // y) # = 1
print(x % y) # = 1
print(-x) # = -3
print(abs(-x)) # = 3
print(int(3.9)) # = 3
print(float(x)) # = 3.0
print(x ** y) # = 9

# Booleans
x = 1 > 2
print(x)
x = 2 > 1
print(x)

# Keywords: and, or, not
x,y = True, False
print((x or y) == True)
print((x and y) == False)
print ((not y) == True)

# Strings
y = "   This is lazy\t\n    "
print(y.strip())
y = """
multiple
line 
string
"""
print(y)
print ("DrDre".lower())
print ("attention".upper())
print("smartphone".startswith("smart"))
# Matches the string's prefix against the argument: True
print("smartphone".endswith("phone"))
# Matches the string's suffix against the argument: True
print("another".find("other"))
# Match index: 2
print("cheat".replace("ch", "m"))
# Replaces all occurrences of the first by the second argument: meat
print(','.join(["F", "B", "I"]))
# Glues together all elements in the list using the separator string: F,B,I
print(len("Rumpelstiltskin"))
# String length: 15
print("ear" in "earth")
# Contains: True