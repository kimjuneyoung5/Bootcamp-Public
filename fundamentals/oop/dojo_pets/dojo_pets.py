#from _typeshed import Self


class Ninja:
    #implement __init__
    def __init__(self, first_name, last_name, treats, pet_food, pet_name, pet_type):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(pet_name, pet_type, "sit")       	
    def walk(self):
        self.pet.play()
    
    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()


class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 75
    
    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print("Bark! Bark!")




