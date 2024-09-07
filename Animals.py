class Animals:
    def __init__(self, animal, name, age, food_level, water_level, product):
        self.animal = animal
        self.name = name
        self.age = age
        self.food_level = food_level
        self.water_level = water_level
        self.product = product

    def printDetails(self):
        print(self.name + " is a " + str(self.age) + " year old " + self.animal + ". Their water and food levels are 100 and they produce " + self.product + ". " + self.product + " levels are at ", end = "")
