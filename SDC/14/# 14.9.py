# 14.9
import random

class Avatar:
    def __init__(self, name, attack_power, hit_points):
        self.name = name
        self.attack_power = attack_power
        self.hit_points = hit_points
        
    def attack(self, opponent):
        damage = self.attack_power
        opponent.hit_points -= damage
        print(f"{self.name} attacked {opponent.name} for {damage} damage!")
        
    def special_power(self):
        pass

class Fighter(Avatar):
    def special_power(self):
        if random.randint(1, 5) == 1:
            return self.attack_power * 2
        else:
            return 0

class Mage(Avatar):
    def special_power(self):
        if random.randint(1, 5) == 1:
            self.hit_points += 10
        else:
            return 0

# Game
player1 = Fighter("Fighter", 10, 50)
player2 = Mage("Mage", 8, 40)

while player1.hit_points > 0 and player2.hit_points > 0:
    print(f"{player1.name} HP: {player1.hit_points}  |  {player2.name} HP: {player2.hit_points}")
    choice = input(f"{player1.name}, do you want to attack or use your special power? (a/s) ")
    if choice.lower() == "a":
        player1.attack(player2)
    elif choice.lower() == "s":
        damage = player1.special_power()
        player2.hit_points -= damage
        if damage != 0:
            print(f"{player1.name} used special power and dealt {damage} damage to {player2.name}!")
        else:
            print(f"{player1.name} used special power but it failed.")
    if player2.hit_points <= 0:
        print(f"{player2.name} has been defeated!")
        break
    choice = input(f"{player2.name}, do you want to attack or use your special power? (a/s) ")
    if choice.lower() == "a":
        player2.attack(player1)
    elif choice.lower() == "s":
        player2.special_power()
        print(f"{player2.name} used special power and gained 10 HP!")
    if player1.hit_points <= 0:
        print(f"{player1.name} has been defeated!")
        break
