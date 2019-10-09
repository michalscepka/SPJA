class Cat:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return '{}: Mnau!'.format(self.name)

class Dog:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return '{}: Haf!'.format(self.name)

animals = [Dog('Lassie'), Cat('Mikes'), Dog('Hafik'), Cat('Garfield')]

for animal in animals:
    print(animal.make_sound())
