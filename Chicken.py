from Animals import Animals
import random


class Chicken(Animals):
    def __init__(self, animal, name, age, food_level, water_level, product, eggs, eggs_per_day):
        super().__init__(animal, name, age, food_level, water_level, product)
        self.eggs = eggs
        self.eggs_per_day = eggs_per_day

    def printAnimalDetails(self):
        self.printDetails()
        print(str(self.eggs) + ".")

    def addEggs(self, player):
        quality = (player.food_level + player.water_level) / 2
        if quality >= 80:
            player.eggs_per_day = 6
        elif quality >= 60:
            player.eggs_per_day = 4
        elif quality >= 40:
            player.eggs_per_day = 3
        elif quality >= 20:
            player.eggs_per_day = 2
        else:
            player.eggs_per_day = 1
        add_product = random.randint(1, 6)
        player.eggs += add_product * player.eggs_per_day
        print("Number of eggs: " + str(player.eggs))

    def sellChicken(self, player, money):
        money += 25 * player.eggs_per_day
        return money
