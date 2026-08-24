#This Program is to learn Abour classes
#Class is a blueprint of an object u can also think of it as a userdefined DataType
#Instead of fixed type of data you can add using defined datatypes

class Character:
    def __init__(self,name,type,health=100,level=0,attackPower=10):
        self.name=name
        self._health=health
        self._level=level
        self.type=type
        self.attackpower=attackPower

    def attack(self,attack,Enemy):
            Enemy.take_damage(self.attackPower)

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
    def __init__(self, name, health=100, level=0,attackPower=50):
        super().__init__(name, "Mage", health, level,attackPower)
    def attack(self,Enemy):
        return super().attack("Arise",Enemy)


class Warrior(Character):
    def __init__(self, name, health=200, level=0,attackPower=70):
        super().__init__(name, "Warrior", health, level,attackPower)
    def attack(self,Enemy):
        return super().attack("Gomu Gomu no Dawn Whip",Enemy)

class Swordsman(Character):
    def __init__(self, name, health=150, level=0,attackPower=65):
        super().__init__(name, "Swordsmen", health, level,attackPower)
    def attack(self,Enemy):
        return super().attack("Getsuga Tenso",Enemy)

class Archer(Character): 
    def __init__(self, name, health=100, level=0,attackPower=55):
        super().__init__(name, "Archer", health, level,attackPower)
    def attack(self,Enemy):
        return super().attack("Piercing Arrow",Enemy)

    

M1=Mage("Sung jin woo")
W1=Warrior("Monkey D. Luffy")
S1=Swordsman("Ichigo Kurosaki")
A1=Archer("Archer")
characters = [M1, W1, S1, A1]
for i in range(0,len(characters)-1):
    characters[i].attack(characters[i+1])
    characters[i].display_status()