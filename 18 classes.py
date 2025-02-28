class Towel:
    def __init__(self,color,cloth_type,size):
       self.color = color
       self.cloth_type = cloth_type
       self.size = size
    def overview(self):
        print(f"{self.size} {self.cloth_type} Towel\ncolor: {self.color}")

mytowel1 = Towel("Lime","Green","Small")
mytowel1.color = "White"

mytowel2 = Towel("Red","Khaki","Large")
print(mytowel1.color)
mytowel1.overview()
mytowel2.overview()

class Kitchen:
    def __init__(self,fruits,fruits_type,weight):
        self.fruits = fruits
        self.fruits_type = fruits_type
        self.weight = weight
    def overview(self):
        print(f"{self.fruits} {self.fruits_type} kitchen\nfruits: {self.fruits}")

mykitchen1 = Kitchen("Apple","yellow.in.color","1kg")
mykitchen1.fruits = "banana"

mykitchen2 = Kitchen("Mango","Yellow.in.color","2kg")
print(mykitchen1.fruits)
mykitchen1.overview()
mykitchen2.overview() 