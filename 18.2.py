class person:
    def __init__(self, name , age ,gender , weight):
        self.name = name
        if type(age) != int:
            raise Exception("Age must be a number")
        self.age = age
        self.gender = gender
        self.weight = weight
    def details(self):
        print(f'Name: {self.name}, Age: {self.age}, Gender:{self.gender}, Weight: {self.weight}')
person1 = person("Prerna kapoor",20,"Female",58)
person1.details()