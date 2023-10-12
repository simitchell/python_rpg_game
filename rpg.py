# class constructor
class Warrior:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    # greet - an instance method
    def greet(self):
        print(f"You are a mighty {self.name}.  You wield the Sword of Destiny and you are here only to win.")
        
    # attack - an instance method
    def attack(self, other):
        other.health -= self.power
        print("You do %d damage to the goblin." % hero.power)
        if goblin.health <= 0:
            print("The goblin is dead.  Peasants will sing songs of your triumph here today for all of time.")

    # do nothing - an instance method
    def nothing(self):
        pass

    # flee - an instance method
    def flee(self):
        print("Goodbye, coward.  You're a crappy hero.")


# instantiate a hero
hero = Warrior("Hero", 10, 5)

# instantiate a goblin
goblin = Warrior("Goblin", 6, 2)

# call the method greet
hero.greet()

while goblin.health > 0 and hero.health > 0:
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack(goblin)

        elif user_input == "2":
            hero.nothing()

        elif user_input == "3":
            hero.flee()
            break

        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.  The world is a darker place now.")