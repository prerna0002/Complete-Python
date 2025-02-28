class Person:
    characterstics_option = ["height, weight, eye_color, hair_color, age"]
    def __init__(self, height=None, weight=None, eye_color=None, hair_color=None, age=None):
        # Height attribute
        if height is not None:
            if type(height) != int:
                raise Exception("Height must be an integer")
            if height <= 0:
                raise Exception("Height must be a positive integer")
            self.height = height
        else:
            self.height = None

        # Weight attribute
        if weight is not None:
            if type(weight) != int:
                raise Exception("Weight must be an integer")
            if weight <= 0:
                raise Exception("weight must be a positive integer")
            self.weight = weight
        else:
            self.weight = None

        # Eye color attribute
        if eye_color is not None:
            if type(eye_color) != str:
                raise Exception("Eye color must be a string")
            if not eye_color:
                raise Exception("Eye color must not be empty")
            self.eye_color = eye_color
        else:
            self.eye_color = None

        # Hair color attribute
        if hair_color is not None:
            if type(hair_color) != str:
                raise Exception("Hair color must be a string")
            if not hair_color:
                raise Exception("Hair color must not be empty")
            self.hair_color = hair_color
        else:
            self.hair_color = None

        # Age attribute
        if age is not None:
            if type(age) != int:
                raise Exception("Age must be an integer")
            if age < 0:
                raise Exception("Age must be a positive integer")
            self.age