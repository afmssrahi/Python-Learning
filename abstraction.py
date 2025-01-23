from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Instantiate objects
dog = Dog()
cat = Cat()

# Call the abstract method
print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow