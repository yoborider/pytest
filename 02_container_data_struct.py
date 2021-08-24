# List
l = [1,2,3]
# len
print(len(l))
# 3
# 1. Append
l = [1, 2, 2]
l.append(4)
print(l)
# [1, 2, 2, 4]
# 2. Insert
l = [1, 2, 4]
l.insert(2, 3)
print(l)
# [1, 2, 3, 4]
# 3. List Concatenation
print([1, 2, 2] + [4])
# [1, 2, 2, 4]
# Removing elements
l = [1, 2, 4]
l.remove(1)
print(l)
# Reverse list
l = [1, 2, 4]
l.reverse()
print(l)
# Sort list
l = [4, 2, 1]
l.sort()
print(l)
# Stack
l = [4, 2, 1]
l.append(5)
print(l)
l.pop()
print(l)
numbers = [0, 1, 2, 'three', 4, 5, 6, 7, 8, 9]
print(numbers[::-1])

# Range
list(range(0,10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list ( range (0, 1000 , 200))
# [0, 200 , 400 , 600 , 800]

#Tranche liste[début:fin:pas].
ani = ["girafe", "tigre", "singe", "souris"]
ani[0:3:2]
# ['girafe', 'singe']

# Sets (collection non ordonnée d'éléments uniques)
hero = "Harry"
guide = "Dumbledore"
enemy = "Lord V."
print(hash(hero))
# 6175908009919104006
print(hash(guide))
# -5197671124693729851
## Can we create a set of strings?
characters = {hero, guide, enemy}
print(characters)
# {'Lord V.', 'Dumbledore', 'Harry'}

# Dictionaries
calories = {'apple':50,'banana':89,'choco':500}
print('apple' in calories.keys())
print(calories['apple'] < calories['choco'])
# True
# Adding cappu,74 in dict
calories['cappu'] = 74
print(calories['banana'] < calories['cappu'])
# False
#Use the keys() and values() functions to access all keys and values of the dictionary
print('apple' in calories.keys())
# True
print(52 in calories.values())
# True
# Access the (key, value) pairs of a dictionary with the items() method:
for k, v in calories.items():
    print(k) if v >= 500 else None
# 'choco

# List and Set comprehension
# Formula is [expression + context]
customers = [("John",24000),
             ("Alice",120000),
             ("Ann",110000),
             ("Zach",44000)]
bigSal = [x for x,y in customers if y>100000]
print(bigSal)