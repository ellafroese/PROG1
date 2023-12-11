# Arithmetic expressions
a = 10
b = 5

# Addition
addition = a + b
print("Addition:", addition)

# Subtraction
subtraction = a - b
print("Subtraction:", subtraction)

# Multiplication
multiplication = a * b
print("Multiplication:", multiplication)

# Division
division = a / b
print("Division:", division)

# Floor Division
floor_division = a // b
print("Floor Division:", floor_division)

# Modulus (Remainder)
modulus = a % b
print("Modulus:", modulus)

# Exponentiation
exponentiation = a ** b
print("Exponentiation:", exponentiation)

# Comparison expressions
print("\nComparison Expressions:")
x = 7
y = 10

# Greater than
print("x > y:", x > y)

# Less than
print("x < y:", x < y)

# Greater than or equal to
print("x >= y:", x >= y)

# Less than or equal to
print("x <= y:", x <= y)

# Equal to
print("x == y:", x == y)

# Not equal to
print("x != y:", x != y)

# Logical expressions
print("\nLogical Expressions:")
p = True
q = False

# Logical AND
print("p and q:", p and q)

# Logical OR
print("p or q:", p or q)

# Logical NOT
print("not p:", not p)

# Membership expressions
print("\nMembership Expressions:")
list_example = [1, 2, 3, 4, 5]

# In
print("3 in list_example:", 3 in list_example)

# Not in
print("6 not in list_example:", 6 not in list_example)

# Identity expressions
print("\nIdentity Expressions:")
m = 10
n = 10
o = [1, 2, 3]
p = [1, 2, 3]

# is
print("m is n:", m is n)

# is not
print("o is not p:", o is not p)

#
#
#
#

# Using range() function
print("Using range() function:")
for i in range(5):
    print(i, end=" ")  # Prints numbers from 0 to 4

# If statement
print("\n\nUsing if statement:")
number = 15
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# While loop
print("\nUsing while loop:")
count = 0
while count < 5:
    print(count, end=" ")  # Prints numbers from 0 to 4
    count += 1

# Dictionaries
print("\n\nUsing dictionaries:")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Car details:", car)

# Using libraries
print("\nUsing libraries (math library):")
import math
print("Square root of 25:", math.sqrt(25))  # Outputs 5.0

# Lists
print("\nUsing lists:")
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)
print("Second fruit in the list:", fruits[1])

# Objects and classes
print("\nUsing objects and classes:")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Creating an object (instance) of the Dog class
my_dog = Dog("Buddy", 3)
print("My dog's name is", my_dog.name, "and it's", my_dog.age, "years old.")
my_dog.bark()
