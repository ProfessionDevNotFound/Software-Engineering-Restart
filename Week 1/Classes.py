#This Program is to learn Abour classes
#Class is a blueprint of an object u can also think of it as a userdefined DataType
#Instead of fixed type of data you can add using defined datatypes

class Character:
    def __init__(self,name,type,health=100,level=0,attackPower=10):
        self.name=name
        self._health=health
        self._level=level
        self.type=type
        self.attackPower=attackPower
    def isAlive(self):
        if (self._health>0):
            return True    
        return False
    def attack(self,attack,Enemy):
            Enemy.take_damage(self.attackPower)
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
    def __init__(self, name, health=100, level=0,attackPower=50):
        super().__init__(name, "Mage", health, level,attackPower)
    def attack(self,Enemy):
        if(super().isAlive):
            return super().attack("Arise",Enemy)
        else:
            print("You are dead")


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



class Character:
    def __init__(self, name, type, health=100, level=0, attackPower=10):
        self.name = name
        self._health = health
        self._level = level
        self.type = type
        self.attackPower = attackPower

    def attack(self, attack, Enemy):
        attack_data = self.attacks[attack]

        print(f"{self.name} used {attack_data['name']}!")
        print(f"Damage: {attack_data['damage']}")

        Enemy.take_damage(attack_data["damage"])

    def take_damage(self, amount):
        self._health -= amount

    def heal(self, amount):
        self._health += amount

    def is_alive(self):
        return self._health > 0

    def display_status(self):
        print(f"""
Name   : {self.name}
Type   : {self.type}
Health : {self._health}
Level  : {self._level}
""")


class Mage(Character):
    def __init__(self, name, health=100, level=0):
        super().__init__(name, "Mage", health, level)

        self.attacks = {
            "1": {"name": "Arise", "damage": 50},
            "2": {"name": "Frost Bolt", "damage": 40},
            "3": {"name": "Shadow Burst", "damage": 70}
        }


class Warrior(Character):
    def __init__(self, name, health=200, level=0):
        super().__init__(name, "Warrior", health, level)

        self.attacks = {
            "1": {"name": "Dawn Whip", "damage": 70},
            "2": {"name": "Red Hawk", "damage": 60},
            "3": {"name": "Gatling", "damage": 80}
        }


class Swordsman(Character):
    def __init__(self, name, health=150, level=0):
        super().__init__(name, "Swordsman", health, level)

        self.attacks = {
            "1": {"name": "Getsuga Tensho", "damage": 65},
            "2": {"name": "Moon Fang", "damage": 50},
            "3": {"name": "Blade Storm", "damage": 75}
        }


class Archer(Character):
    def __init__(self, name, health=100, level=0):
        super().__init__(name, "Archer", health, level)

        self.attacks = {
            "1": {"name": "Piercing Arrow", "damage": 55},
            "2": {"name": "Triple Shot", "damage": 45},
            "3": {"name": "Rain of Arrows", "damage": 75}
        }


M1 = Mage("Sung Jin Woo")
W1 = Warrior("Monkey D. Luffy")
S1 = Swordsman("Ichigo Kurosaki")
A1 = Archer("Archer")

characters = [M1, W1, S1, A1]

player = M1
enemy = W1

print("Choose your attack:")

for key, attack in player.attacks.items():
    print(f"{key}. {attack['name']} - {attack['damage']} damage")

try:
    choice = input("Choose attack: ")
    player.attack(choice, enemy)
    enemy.display_status()
except KeyError:
    print("Input not valid Try Again")

