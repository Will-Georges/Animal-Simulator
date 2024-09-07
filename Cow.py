from Animals import Animals
import random


class Cow(Animals):
    def __init__(self, animal, name, age, food_level, water_level, product, milk, beef_quality):
        super().__init__(animal, name, age, food_level, water_level, product)
        self.milk = milk
        self.beef_quality = beef_quality

    def printAnimalDetails(self):
        self.printDetails()
        print(str(self.milk) + ".")

    def addMilk(self, player):  # Accept 'player' as a parameter
        add_product = random.randint(1, 10)
        player.milk += add_product
        print("Milk storage in Litres: " + str(player.milk))
        quality = (player.food_level + player.water_level) / 2
        if quality >= 80:
            player.beef_quality = 10
        elif quality >= 60:
            player.beef_quality = 8
        elif quality >= 40:
            player.beef_quality = 5
        elif quality >= 20:
            player.beef_quality = 3
        else:
            player.beef_quality = 0

    def sellCow(self, player, money):
        money += 20 * player.beef_quality
        return money  # Return the updated money value
