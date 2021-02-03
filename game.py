import time
import random
import abc

class Ninja:
    def __init__(self, name, health):
        self.name  = name
        self.health = health
        self.weapon = Hand(self)
        
    def random_weapon(self):
        r = random.random()
        if 0.03 > r:
            self.weapon = Sword(self)
            print("%s hat ein Schwert gefunden" % self.name)
        elif 0.06 > r:
            self.weapon = Magic(self)
            print("%s hat Magiefähigkeiten erhalten" % self.name)
        
    def lose_weapon(self):
        r = random.random()
        if r < 0.1 and self.weapon.__class__ != Hand.__class__:
            print("%s hat seine Waffe %s verloren" % (self.name, self.weapon.__class__))
            self.weapon = Hand(self)
            
    def hit(self, target):
        if self.owner.is_alive
        
class Sword(Weapon):
    def __init__(self, owner):
        
