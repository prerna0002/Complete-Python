class Device:
    def __init__(self, brand:str , name:str, wireless:bool, type: str, rec: bool , warranty: float = None, price:float = None):
        self.brand = brand
        self.name = name
        self.category = type
        self.wirless = wireless
        self.rechargable = rec
        self.warranty = warranty
    def __str__(self):
        return f"{self.brand} {self.name}"
    def __float__(self):
        return self.price

class Mobile(Device):
    def __init__(self, brand , name, warrenty,price , ram , network):
        self.supper().__init__(brand, name , True, "Handheld Mobile", True , price)
        self.ram = ram
        self.network = network

myphone = Mobile("Motorola", "G82", 1, 18_000,8, "5G")
print(myphone)