import items,random

class Animal:
    def __init__(self):
        self.name="Animal"
        self.hp=1
        self.drops=[]
    def hunt(self,player):
        print("Which weapon would you like to use? ")
        for i in player.inv.all:
            if issubclass(i,items.Sword):
                print(i().name)
            elif issubclass(i,items.Potion):
                if i().attack is True:
                    print(i().name)
        #print("=====================================")
        answer=input("> ")
        current=self.hp
        for i in player.inv.all:#range(len(player.inv.all)):
            e=player.inv.all
            if issubclass(i,items.Sword) and i().name.lower()==answer.lower():
                i().use(self,player)
                #print("=====================================")
                return
            elif issubclass(i,items.Potion) and i().name.lower()==answer.lower() and i().attack is True:
                i().use(self,player)
                #print("=====================================")
                player.inv.potions.remove(i)
                player.inv.all.remove(i)
                return
        if current==self.hp:
            print("You use your fists...")
            #print("=====================================")
            self.hp-=0.5

class Cow(Animal):
    def __init__(self):
        super().__init__()
        self.name="Cow"
        self.hp=4
        self.drops=[items.Beef for i in range(random.randint(1,3))]+[items.Leather for i in range(random.randint(0,2))]

class Sheep(Animal):
    def __init__(self):
        super().__init__()
        self.name="Sheep"
        self.hp=4
        self.drops=[items.Wool]+[items.Mutton for i in range(random.randint(0,1))]

class Chicken(Animal):
    def __init__(self):
        super().__init__()
        self.name="Chicken"
        self.hp=1
        self.drops=[items.Chicken,items.Feather]

class Pig(Animal):
    def __init__(self):
        super().__init__()
        self.name="Pig"
        self.hp=3
        self.drops=[items.Pork for i in range(random.randint(2,4))]

class Bumblebee(Animal):
    def __init__(self):
        super().__init__()
        self.name="Bumblebee"
        self.hp=1
        self.drops=[]
        self.decrease=1

class Honeybee(Animal):
    def __init__(self):
        super().__init__()
        self.name="Honeybee"
        self.hp=1
        self.drops=[]
        self.decrease=2
