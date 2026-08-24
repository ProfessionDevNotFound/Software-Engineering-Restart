#This Program is to learn Abour classes
#Class is a blueprint of an object u can also think of it as a userdefined DataType
#Instead of fixed type of data you can add using defined datatypes

class Character:
    def __init__(self,name,type,health=100,level=0):
        self.name=name
        self._health=health
        self._level=level
        self.type=type

    def attack(self,attack):
        print(attack," ")

    def take_damage(self,amount):
        self._health-=amount

    def heal(self,amount):
        self._health+=amount

    def display_status(self):
        print(f'''
        Hi there my name is {self.name}
        I am a {self.type}
        My health is {self._health}

              ''')
class Mage(Character):
    def __init__(self, name, health=100, level=0):
        super().__init__(name, "Mage", health, level)
    def attack(self):
        return super().attack("Arise")

class Warrior(Character):
    def __init__(self, name, health=200, level=0):
        super().__init__(name, "Warrior", health, level)
    def attack(self):
        return super().attack("Gomu Gomu no Dawn Whip")

class Swordsman(Character):
    def __init__(self, name, health=150, level=0):
        super().__init__(name, "Swordsmen", health, level)
    def attack(self):
        return super().attack("Getsuga Tenso")

class Archer(Character):
    def __init__(self, name, health=100, level=0):
        super().__init__(name, "Archer", health, level)
    def attack(self):
        return super().attack("Piercing Arrow")

    

M1=Mage("Sung jin woo")
W1=Warrior("Monkey D. Luffy")
S1=Swordsman("Ichigo Kurosaki")
A1=Archer("Archer")

M1.attack()
W1.attack()
S1.attack()
A1.attack()

M1.display_status()
W1.display_status()
S1.display_status()
A1.display_status()