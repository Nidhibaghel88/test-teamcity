class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

    def details(self):
                print(self.name, self.age)


rest1 = Person(name='abc', age=88)
rest1.details()

rest1.change_name('Micky')
rest1.details()
