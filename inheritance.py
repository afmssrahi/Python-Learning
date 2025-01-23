class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name} says Tweet!"

    def fly(self):
        return f"{self.name} can fly!" if self.can_fly else f"{self.name} cannot fly."

# Example usage
bird = Bird("Tweety", True)

print(bird.speak())  # Output: Tweety says Tweet!
print(bird.fly())    # Output: Tweety can fly!