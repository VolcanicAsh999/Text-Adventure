import items

class Inv:
    def __init__(self):
        self.books=[]
        self.swords=[]
        self.potions=[items.HealPotion]
        self.all=[items.HealPotion]
        self.other=[]
        self.food=[]
    def loop(self):
        self.potions.clear()
        self.books.clear()
        self.swords.clear()
        self.other.clear()
        self.food.clear()
        for i in self.all:
            if issubclass(i,items.Potion):
                self.potions.append(i)
            if issubclass(i,items.Sword):
                self.swords.append(i)
            if issubclass(i,items.Book):
                self.books.append(i)
            if issubclass(i,items.Other) or issubclass(i,items.Special):
                self.other.append(i)
            if (issubclass(i,items.Food) or hasattr(i,"hp")):
                self.food.append(i)
