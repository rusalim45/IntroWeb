class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name, "and I am", self.age)

p1 = Person("Alice", 22)
p1.introduce()

# Modifying
p1.age = 23
print("Updated age:", p1.age)

# Class Variable vs Instance Variable
class Student:
    school = "AUCA"

    def __init__(self, name):
        self.name = name

s1 = Student("Bob")
print("Student:", s1.name)
print("School:", Student.school)

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
print("Balance:", acc.get_balance())

# Inheritance
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog says Bark")

d = Dog()
d.speak()

# Polymorphism
class Bird:
    def move(self):
        print("Flying")

class Fish:
    def move(self):
        print("Swimming")

animals = [Bird(), Fish()]

for a in animals:
    a.move()

# Deleting
del p1.age
print("Attribute age deleted from p1")
