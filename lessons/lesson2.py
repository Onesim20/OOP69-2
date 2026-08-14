# from hw.Homework1 import kirito, asuna
#
#
# class Hero:
#     #Конструктор класса
#     def __init__(self, name, lvl, hp):
#         #Атрибуты класса
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def action(self):
#         print(f"{self.name} this me base action !!")
#
# class MageHero(Hero):
#
#    def __init__(self, name, lvl, hp,mp):
#        super() .__init__(name, lvl, hp)
#        self.mp = mp
#
#
#    # def casti_spell(self):
#    #     print(f"{self.name} Cast firboll!")
#
#     def action(self):
#         print(f"My name{self.name} My MP {self.mp}")
#
# kirito = MageHero('Kirito', 100, 10000)
# asuna = Hero('Asuna', 100, 10000)
#
# kirito.action()
# # kirito.casti_spell()
# asuna.action()


class Fly:
    def action(self):
        print("Fly")

class Swin:
    def action(self):
        print("Swin")

class Animal(Swin, Fly):
     def action(self):
         print("Base action")

dunald_duck = Animal()
dunald_duck.action()

class A:
    def action(self):
        print("A")

class B(A):
    def action(self):
        print("B")
        super().action()

class C(A):
    def action(self):
        print("C")
        super().action()

class D(B, C):
    def action(self):
        print("D")
        super().action()

test = D()
test.action()