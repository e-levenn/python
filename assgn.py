class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


myobject = people("Peter", 17)
myobject2 = people("John", 18)
myobject3 = people("James", 16)
myobject4 = people("Joseph", 17)
myobject5 = people("Michael", 17)
myobject6 = people("Alex", 17)
myobject.show()
myobject2.show()
myobject3.show()
myobject4.show()
myobject5.show()
myobject6.show()
