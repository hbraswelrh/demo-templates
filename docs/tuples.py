# Tuples: immutable sequences used for storing collections of heterogeneous data
# Tuples are used for cases where an immutable sequence of homogenous data is needed
# Ex: allowing storage in a set or dict instance

birth_certificate = ("Hannah", 21, "Kalamazoo Michigan")

# Tuple printing given value and requesting index
print((birth_certificate).index("Hannah"))
print(birth_certificate.index(21))
print(birth_certificate.index("Kalamazoo Michigan"))

# Printing original tuple
print(birth_certificate)

# Tuple printing given index
print(birth_certificate[0])
print(birth_certificate[1])
print(birth_certificate[2])

for value in birth_certificate:
    print(value)

work_to_do = ("Learn Python", ["Go", "Python", "YAML"], 40)

for work in work_to_do:
    print("Today I need to", work_to_do[0])
    print("Some programming languages I use daily", work_to_do[1])
    print("Hours I work per week", work_to_do[2])
