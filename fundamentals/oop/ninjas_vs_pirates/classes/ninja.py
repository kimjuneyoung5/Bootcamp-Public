class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self
    
    def heal( self ):
        self.health += 5
        return self

class VampireNinja(Ninja):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 15
        self.speed = 7
        self.health = 120

    def berserker_mode(self):
        self.strength += 10 
    
    def attack(self, pirate):
        super().attack(pirate)
        self.health += 3
        return self
