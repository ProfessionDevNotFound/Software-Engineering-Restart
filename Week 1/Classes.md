# ⚔️ OOP Character Battle — Python

A small Python project created to learn and practice **Object-Oriented Programming (OOP)** and basic **exception handling**.

The program defines different character types, gives each character a set of attacks, and allows a player to choose an attack against an enemy.

## 🎯 Purpose

This project was built as a hands-on way to understand:

- Classes
- Objects
- Constructors
- Inheritance
- Encapsulation
- Method inheritance
- `super()`
- Object interaction
- Dictionaries
- Exception handling
- `try` / `except`
- Loops and input validation

---

## 🧩 Character System

The program has a base `Character` class and four specialized character classes:

```text
                Character
              /    |     |     \
             /     |     |      \
          Mage  Warrior Swordsman Archer
```

### Character

The base class stores common character properties:

- `name`
- `type`
- `_health`
- `_level`
- `attackPower`

It also provides common methods:

- `attack()`
- `take_damage()`
- `heal()`
- `is_alive()`
- `display_status()`

### Mage

Starts with:

- 100 health

Attacks:

- Arise — 50 damage
- Frost Bolt — 40 damage
- Shadow Burst — 70 damage

### Warrior

Starts with:

- 200 health

Attacks:

- Dawn Whip — 70 damage
- Red Hawk — 60 damage
- Gatling — 80 damage

### Swordsman

Starts with:

- 150 health

Attacks:

- Getsuga Tensho — 65 damage
- Moon Fang — 50 damage
- Blade Storm — 75 damage

### Archer

Starts with:

- 100 health

Attacks:

- Piercing Arrow — 55 damage
- Triple Shot — 45 damage
- Rain of Arrows — 75 damage

---

## 🏗️ OOP Concepts

### Class

`Character` acts as the base blueprint for the characters.

```python
class Character:
```

### Objects

Instances of the character classes are created:

```python
M1 = Mage("Sung Jin Woo")
W1 = Warrior("Monkey D. Luffy")
S1 = Swordsman("Ichigo Kurosaki")
A1 = Archer("Archer")
```

### Inheritance

The specialized character classes inherit from `Character`:

```python
class Mage(Character):
```

This allows them to reuse the common functionality defined in the parent class.

### Encapsulation

Health is stored as:

```python
self._health
```

and modified through methods such as:

```python
take_damage()
heal()
```

rather than directly changing the health from outside the class.

### `super()`

The child classes use `super()` to initialize the parent `Character`:

```python
super().__init__(name, "Mage", health, level)
```

### Polymorphism

The program uses a common `attack()` concept while allowing character-specific attack data.

The same general operation can work with different character objects.

---

## ⚔️ Attack System

Each character has an `attacks` dictionary.

For example, the Mage has:

```python
self.attacks = {
    "1": {"name": "Arise", "damage": 50},
    "2": {"name": "Frost Bolt", "damage": 40},
    "3": {"name": "Shadow Burst", "damage": 70}
}
```

Each attack contains:

- Attack name
- Damage value

This makes it possible to add or modify attacks through data rather than creating a separate method for every attack.

---

## 🎮 Current Program Flow

The current version uses:

```python
player = M1
enemy = W1
```

The player is given the available attacks:

```text
Choose your attack:

1. Arise - 50 damage
2. Frost Bolt - 40 damage
3. Shadow Burst - 70 damage
```

The user enters an attack choice.

The selected attack is then applied to the enemy:

```text
Player
   ↓
attack()
   ↓
Attack dictionary
   ↓
Damage
   ↓
Enemy.take_damage()
   ↓
Enemy health decreases
```

The enemy's updated status is then displayed.

---

## 🚨 Exception Handling

The program uses `try` / `except` to handle an invalid attack selection.

If the user enters an attack that doesn't exist in the dictionary, a `KeyError` occurs.

The program catches it:

```python
except KeyError:
    print("Input not valid Try Again")
```

The `while` loop then allows the user to try again.

Example:

```text
Choose your attack:
> 9

Input not valid Try Again

Choose your attack:
> 2

Sung Jin Woo used Frost Bolt!
Damage: 40
```

---

## 📚 What This Project Demonstrates

This project was intentionally kept small so the focus stays on understanding the programming concepts.

The main learning progression was:

```text
Class
  ↓
Object
  ↓
Inheritance
  ↓
Encapsulation
  ↓
Method Reuse
  ↓
Polymorphism
  ↓
Objects interacting with objects
  ↓
Dictionary-based data
  ↓
Exception Handling
```

---

## 🚀 Possible Future Improvements

Some possible extensions:

- [ ] Allow the user to choose their character
- [ ] Allow the user to choose an enemy
- [ ] Allow multiple rounds of combat
- [ ] Add character death using `is_alive()`
- [ ] Prevent dead characters from attacking
- [ ] Add healing during combat
- [ ] Add enemy AI
- [ ] Move attack data into a JSON file
- [ ] Add more characters and attacks
- [ ] Add custom exceptions
- [ ] Add unit tests

---

## 📁 Project Structure

Current project:

```text
oop-character-battle/
│
├── main.py
└── README.md
```

---

## 📌 Status

**Learning Project**

Built to practice Python OOP and exception handling through a small character battle system.

The project is intentionally simple and focuses on understanding **how OOP concepts work together in a practical program**.
