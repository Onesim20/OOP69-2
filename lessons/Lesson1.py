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
asuna = Hero('Kirito',100,10000)


git init
git add Homework1.py
git commit -m "Add Hero class"
git branch -M main
git remote add origin https://github.com/твой_логин/название_репо.git
git push -u origin main