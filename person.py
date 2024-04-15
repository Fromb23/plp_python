#!/usr/bin/python3

class Person:
    """ A class person"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce_person(self):
        """Introduce the person"""
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# creating the instance of the person
person1 = Person("John", 30, "male")

#calling the person to introduce themselves
person1.introduce_person()
