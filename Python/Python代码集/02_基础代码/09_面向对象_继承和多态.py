class Animal(object):
    def run(self):
        print('Animal is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

if __name__ == '__main__':
    animal = Animal()
    cat = Cat()
    dog = Dog()
    animal.run()
    cat.run()
    dog.run()