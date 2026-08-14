# def test(name, lvl):
#      print(nam
#      print(lvl)

class Hero:
    #Конструктор класса
    def __init__(self, name, lvl, hp):
        #Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp




# print(Kirito)

    def action(self):
        print(f"{self.name} this me base action !!")


#Обьект/Экземпляр на основе класса
kirito = Hero('Kirito',100,10000)
asuna = Hero('Asuna',100,10000)


