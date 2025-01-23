class Person() :
    def __init__(self) :
        self.name = 'Bob'
        self.age = 25

    def show(self) :
        print(f'Name: {self.name}, Age: {self.age}')

p1 = Person()
p2 = Person()

p1.show()
p2.show()