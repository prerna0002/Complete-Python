class Device:
    def __init__(self, brand:str , name:str, wireless:bool, type: str, rec: bool , warranty: float = None, price:float = None):
        self.brand = brand
        self.name = name
        self.category = type
        self.wirless = wireless
        self.rechargable = rec
        self.warranty = warranty
    def __str__(self:
                return f"{self.brand} {self.name}")
