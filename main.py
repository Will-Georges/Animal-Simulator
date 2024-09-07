import random
from Cow import Cow
from Sheep import Sheep
from Chicken import Chicken

day = 0
money = 0


animal = input("Do you want your animal to be a cow, sheep, or chicken? ").lower()
while animal not in ["cow", "sheep", "chicken"]:
    print("Invalid input, try again")
    animal = input("Do you want your animal to be a cow, sheep, or chicken? ").lower()

name = input("What would you like to call your " + animal + "? ")
age = int(input("How old do you want your " + animal + " to be? "))

if animal == "cow":
    player = Cow(animal, name, age, 100, 100, "Milk", 0, 1)
elif animal == "sheep":
    player = Sheep(animal, name, age, 100, 100, "Wool", 0)
else:
    player = Chicken(animal, name, age, 100, 100, "Eggs", 0, 3)
player.printAnimalDetails()


def buy_animal():
    global animal
    global name
    global age
    global player
    global money
    if animal == "cow":
        money = player.sellCow(player, money)  # Update money based on return value
    elif animal == "sheep":
        money = player.sellSheep(money)
    else:
        money = player.sellChicken(player, money)
    if money >= 100:
        money -= 100
        animal = input("Do you want your animal to be a cow, sheep, or chicken? ").lower()
        while animal not in ["cow", "sheep", "chicken"]:
            print("Invalid input, try again")
            animal = input("Do you want your animal to be a cow, sheep, or chicken? ").lower()

        name = input("What would you like to call your " + animal + "? ")
        age = int(input("How old do you want your " + animal + " to be? "))

        if animal == "cow":
            player = Cow(animal, name, age, 100, 100, "Milk", 0, 1)
        elif animal == "sheep":
            player = Sheep(animal, name, age, 100, 100, "Wool", 0)
        else:
            player = Chicken(animal, name, age, 100, 100, "Eggs", 0, 3)
        player.printAnimalDetails()
    else:
        print("You do not have enough money. You have bankrupted the farm. Well done, now the game is over because you didn't manage your financials well")
        exit()


def print_day():
    global day
    global money
    day += 1
    player.age += 1
    food_loss = random.randint(2, 10)
    water_loss = random.randint(2, 10)
    player.food_level -= food_loss
    player.water_level -= water_loss
    print("-----------------------------------------------------------------------------------------------------------")
    print("Day: " + str(day))
    if animal == "cow":
        player.addMilk(player)
    elif animal == "sheep":
        player.addWool(player)
    else:
        player.addEggs(player)
    print("Food Level: " + str(player.food_level))
    print("Water Level: " + str(player.water_level))
    print("Money: " + str(money))
    check_food_and_water_levels()
    action()


def action():
    global money
    choice = input("Feed your animal [a], hydrate them [b], sell their product [c], sell your animal [d] or move to the next day [e]")
    if choice == "a":
        if money <= 0:
            print("You do not have enough money to buy food. Sell their product or advance to the next day.")
            action()
        else:
            food_amount = input("How much food would you like to give your animal.")
            if check_money(food_amount):
                money -= int(food_amount)
                player.food_level += int(food_amount)
                check_food_and_water_levels()
            else:
                action()
    elif choice == "b":
        if money <= 0:
            print("You do not have enough money to buy water. Sell their product or advance to the next day.")
            action()
        else:
            water_amount = input("How much water would you like to give your animal.")
            if check_money(water_amount):
                money -= int(water_amount)
                player.water_level += int(water_amount)
                check_food_and_water_levels()
            else:
                action()
    elif choice == "c":
        if player.animal == "cow":
            if player.milk > 0:
                print("Milk sold!")
                money += (player.milk * 3)
                player.milk = 0
                action()
            else:
                print("You do not have any milk.")
                action()
        elif player.animal == "sheep":
            if player.wool > 0:
                print("Wool sold!")
                money += (player.wool * 3)
                player.wool = 0
                action()
            else:
                print("You do not have any wool.")
                action()
        elif player.animal == "chicken":
            if player.eggs > 0:
                print("Eggs sold!")
                money += (player.eggs * player.eggs_per_day)
                player.eggs = 0
                action()
            else:
                print("You do not have any eggs.")
                action()
    elif choice == "d":
        choice = input("Are you sure you want to sell your " + player.animal + ". yes/no ")
        if choice == "yes":
            print("You have sold your animal. You will now be able to start the game again or end the game.")
            end_game = input("Do you want to end the game [a] or buy another animal and continue [b]")
            if end_game == "b":
                buy_animal()
            else:
                exit()
        else:
            return
    elif choice == "e":
        print_day()
        return
    else:
        print("Invalid input. Try again")
        action()


def check_food_and_water_levels():
    global day
    if player.food_level > 100:
        player.food_level = 100
    if player.water_level > 100:
        player.water_level = 100
    if player.food_level <= 0:
        print("Oh no. Due to a lack of food, your animal died. The EPA have now shut down your farm.")
        print("Game over.")
        exit()
    elif player.water_level <= 0:
        print("Oh no. Due to a lack of water, your animal died. The EPA have now shut down your farm.")
        print("Game over.")
        exit()
    elif day >= 100:
        print("Oh no! A true tragedy. " + player.name + " has passed away. Maybe it was all the cocaine you gave them.")
        print("Game over.")
        exit()


def check_money(amount):
    global money
    if money >= int(amount):
        return True
    else:
        return False


def play():
    global day
    if day == 0:
        print("Welcome to animal simulator! Keep " + player.name + " alive, and sell their product for money.")
    while day <= 100:
        print_day()
    else:
        print("Oh no! A true tragedy. " + player.name + " has passed away. Maybe it was all the cocaine you gave them.")
        exit()


play()
