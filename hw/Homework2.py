import random


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Меня зовут {self.name}, я герой {self.level} уровня.")

    def attack(self):
        print(f"{self.name} наносит удар!")

    def rest(self):
        self.health += 20
        print(f"{self.name} отдыхает и восстанавливает здоровье. Текущее здоровье: {self.health}")


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name}: Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}: Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}: Ассасин атакует из-под тишка!")


warrior = Warrior("Онесим", 5, 100, 20, 50)
mage = Mage("Кирито", 4, 80, 15, 70)
assassin = Assassin("Какойто то ассасин", 6, 90, 18, 60)

heroes = {
    "Warrior": warrior,
    "Mage": mage,
    "Assassin": assassin,
}


def demo_methods():
    for hero in heroes.values():
        hero.greet()
        hero.attack()
        hero.rest()
        print()


BEATS = {
    "Warrior": "Assassin",
    "Assassin": "Mage",
    "Mage": "Warrior",
}


def determine_winner(player_choice, enemy_choice):
    if player_choice == enemy_choice:
        return "draw"
    if BEATS[player_choice] == enemy_choice:
        return "player"
    return "enemy"


def play_game():
    valid_choices = list(heroes.keys())
    player_choice = input("Выберите героя (Warrior / Mage / Assassin): ").strip().capitalize()

    while player_choice not in valid_choices:
        player_choice = input("Некорректный ввод. Выберите героя (Warrior / Mage / Assassin): ").strip().capitalize()

    enemy_choice = random.choice(valid_choices)

    print(f"Вы выбрали: {player_choice}")
    print(f"Противник: {enemy_choice}")

    heroes[player_choice].attack()
    heroes[enemy_choice].attack()

    result = determine_winner(player_choice, enemy_choice)

    if result == "draw":
        print("Ничья!")
    elif result == "player":
        print(f"{player_choice} победил!")
    else:
        print(f"{enemy_choice} победил!")


demo_methods()
play_game()