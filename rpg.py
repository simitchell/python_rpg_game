# parent class constructor
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    # alive - to check if warrior is alive.  an instance method
    def alive(self):
        return self.health > 0
    
     # greet - an instance method
    def greet(self, other):
        print()
        print(f"You are a mighty {self.name}.\nYou wield the Sword of Destiny and you are here only to win.")
        print(f"You have {self.health} health and {self.power} power.")
        print(f"The {other.name} has {other.health} health and {other.power} power.")

    def print_status(self, other):
        if other.alive():
            print()
            print (f"{self.name} health: {self.health}")
        if self.alive():
            print()
            print (f"{other.name} health: {other.health}")
        else:
            print()
            print(f"The {self.name} has died.  The world is now a much darker place.")
            print()

    # attack - an instance method
    def attack(self, other):
        other.health -= self.power

        if self.alive():
            print()
            print(f"{self.name} does %d damage to the {other.name}." % self.power)
    
        else:
            print()
            print(f"The {self.name} has died.  Peasants and minstrels will sing songs of your victory here for all time.  Long live the {other.name}!")  
            print() 
        

    # do nothing - an instance method
    def nothing(self):
        pass

    # flee - an instance method
    def flee(self):
        print()
        print(f"{self.name} has chosen to flee.  Goodbye, coward.  You're a crappy hero.")
        print()

    
# child class constructor
class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)   

   
# child class constructor
class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


# instantiate a hero
hero = Hero("Hero", 10, 5)

# instantiate a goblin
goblin = Goblin("Goblin", 6, 2)

# call the method greet
hero.greet(goblin)

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
                hero.print_status(goblin)
            # if hero.alive():
            #     print()
            #     print (f"Hero health: {hero.health}")
            # if goblin.alive():
            #     print()
            #     print (f"Goblin health: {goblin.health}")
            

        elif user_input == "2":
            hero.nothing()
            goblin.attack(hero)
            # print()
            if goblin.alive():
                hero.print_status(goblin)
            # if hero.alive():
            #     hero.print_status(goblin)
            # else:
            #     print()
            #     print (f"The {hero.name} is dead.  The world is a darker place now.")

        elif user_input == "3":
            hero.flee()
            break

        else:
            print()
            print("Invalid input %r" % user_input)