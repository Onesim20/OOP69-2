# ЗАДАЧА 1: Базовый класс Hero
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")

# Проверка задачи 1 (раскомментируйте, чтобы увидеть вывод)
# hero1 = Hero("Onesim", 10, 100)
# hero1.action()


# ЗАДАЧА 2: Дочерние классы MageHero и WariorHero
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")


class WarriorHero(MageHero):
    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")

# Проверка задачи 2
# merlin = MageHero("Merlin", 50, 100, 150)
# merlin.action()
# conan = WarriorHero("Conan", 50, 120, 0)
# conan.action()


# ЗАДАЧА 3: Класс BankAccoynt
class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password):
        return password == self.__password

    @property
    def full_info(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

 # ЗАДАЧА 4: Магиические методы
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) != type(other.hero):
            raise TypeError("Нельзя сложить счета героев разных классов!")
        return self._balance + other._balance

    def __eq__(self, other):
        return type(self.hero) == type(other.hero) and self.hero.lvl == other.hero.lvl

# Проверка задачи 3

# merlin = MageHero("Merlin", 50, 100, 150)
# acc1 = BankAccount(merlin, 5000, "1234", "Simba")
# print(acc1.login("1234"))
# print(acc1.full_info)
# print(acc1.get_bank_name())
# print(acc1.bonus_for_level())

#  Проверка задачи 4
# merlin = MageHero("Merlin", 50, 100, 150)
# merlin2 = MageHero("Merlin", 50, 100, 150)
# conan = WarriorHero("Conan", 50, 120, 0)
# acc1 = BankAccount(merlin, 5000, "1234", "Simba")
# acc2 = BankAccount(merlin2, 3000, "1234", "Simba")
# acc3 = BankAccount(conan, 2000, "1234", "Simba")
# print(acc1)
# print(acc2)
# print("Сумма счетов двух магов:", acc1 + acc2)
# try:
#     acc1 + acc3
# except TypeError as e:
#     print("Ошибка:", e)
# print("Mage1 == Mage2 ?", acc1 == acc2)
# print("Mage1 == Warrior ?", acc1 == acc3)