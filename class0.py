class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('hello', self.name)

p = Person('aa')
p.say_hi()

# ok
