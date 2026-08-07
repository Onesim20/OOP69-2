class Hero:

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):

        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):

        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):

        print(f"{self.name} отдыхает…")
        self.health += 1

kirito = Hero('Kirito', 100, 10000, 500)
asuna = Hero('Asuna', 100, 10000, 450)

heroes = [kirito, asuna]

for hero in heroes:
    print(f"\n=== {hero.name} ===")
    print(f"До:   health={hero.health}, strength={hero.strength}")

    hero.greet()
    hero.attack()
    hero.rest()

    print(f"После: health={hero.health}, strength={hero.strength}")