# parent class constructor
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    # alive - to check if warrior is alive.  an instance method
    def alive(self):
        return self.health >= 0

    # attack - an instance method
    def attack(self, other):
        other.health -= self.power
        print(f"{self.name} do %d damage to the {other.name}." % other.power)
        if goblin.health <= 0:
            print(f"The {other.name} is dead.")

    # do nothing - an instance method
    def nothing(self):
        pass

    # flee - an instance method
        def flee(self):
            print(f"You have chosen to {flee}.  Goodbye, coward.  You're a crappy hero.")

    
# child class constructor
class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)   

    # greet - an instance method
    def greet(self, other):
        print(f"You are a mighty {self.name}.\nYou wield the Sword of Destiny and you are here only to win.")
        print(f"You have {self.health} health and {self.power} power.")
        print(f"The {other.name} has {other.health} health and {other.power} power.")


# child class constructor
class Goblin(Character):
    def __init__(self, name, health,power):
        super().__init__(name, health, power)


# instantiate a hero
hero = Hero("Hero", 10, 5)

# instantiate a goblin
goblin = Goblin("Goblin", 6, 2)

# call the method greet
hero.greet()

while hero.alive() and goblin.alive():
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1" and hero.alive() and goblin.alive():
            hero.attack(goblin)
            goblin.attack(hero)
            if goblin.alive():
                print (f"Goblin health: {goblin.health}")
            if hero.alive():
                print (f"Hero health: {hero.health}")

        elif user_input == "2":
            hero.nothing()
            goblin.attack(hero)
            if goblin.alive():
                print (f"Goblin health: {goblin.health}")
            if hero.alive():
                print (f"Hero health: {hero.health}")

        elif user_input == "3":
            hero.flee()
            break

        else:
            print("Invalid input %r" % user_input)

        # if goblin.alive():
            # Goblin attacks hero
        
        # hero.health -= goblin.power
        # print("The goblin does %d damage to you." % goblin.power)
        # if hero.health <= 0:
        #     print("You are dead.  The world is a darker place now.")