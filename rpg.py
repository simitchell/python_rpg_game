# class constructor
class Warrior:
    def __init__(self, health, power):
        self.health = health
        self.power = power

# instantiate a hero
Hero = Warrior("Hero", 10, 5)

# instantiate a goblin
Goblin = Warrior("Goblin", 6, 2)

# greet - an instance method
    def 

# attack - an instance method

# do nothing - an instance method

# flee - an instance method




# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have %d health and %d power." % (hero_health, hero_power))
#         print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ",)
#         user_input = input()
#         if user_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do %d damage to the goblin." % hero_power)
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif user_input == "2":
#             pass
#         elif user_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input %r" % user_input)

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does %d damage to you." % goblin_power)
#             if hero_health <= 0:
#                 print("You are dead.")

# main()