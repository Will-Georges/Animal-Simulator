from Animals import Animals
import random


class Sheep(Animals):
    def __init__(self, animal, name, age, food_level, water_level, product, wool):
        super().__init__(animal, name, age, food_level, water_level, product)
        self.wool = wool

    def printAnimalDetails(self):
        self.printDetails()
        print(str(self.wool) + ".")

    def addWool(self, player):
        add_product = random.randint(1, 10)
        player.wool += add_product
        print("Wool storage: " + str(player.wool))

    def sellSheep(self, money):
        money += 100
        return money
