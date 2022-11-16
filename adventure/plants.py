import items,random

class Plant:
    def __init__(self):
        self.item=None
        self.timer=0
        self.waittime=1000
        self.name="Plant"
        self.active=True
    def grow(self,room,pollinate_chance):
        self.timer+=1
        if self.timer>=self.waittime+random.randint(-1,1) and self.active:
            self.timer=0
            room.collect.append(self.item)
            print(f"The {self.name} grew a {self.item().name}!")
        if random.randint(0,pollinate_chance)==0:
            room.plants.append(type(self)())
            print(f"The {self.name} pollinated and grew another {self.name}!")
    def take(self,player,room):
        self.active=False
    def plant(self,player,room):
        self.active=True
        self.timer=0
        player.plants.remove(self)
        room.plants.append(self)

class TomatoPlant(Plant):
    def __init__(self):
        super().__init__()
        self.item=items.Tomato
        self.waittime=3
        self.name="Tomato Plant"

class WheatStalk(Plant):
    def __init__(self):
        super().__init__()
        self.item=items.Wheat
        self.waittime=4
        self.name="Wheat Stalk"

class BerryBush(Plant):
    def __init__(self):
        super().__init__()
        self.item=items.Berry
        self.waittime=2
        self.name="Berry Bush"

class AppleTree(Plant):
    def __init__(self):
        super().__init__()
        self.item=items.Apple
        self.waittime=5
        self.name="Apple Tree"

class OrangeTree(Plant):
    def __init__(self):
        super().__init__()
        self.item=items.Orange
        self.waittime=4
        self.name="Orange Tree"

class Beehive(Plant):
    def __init__(self):
        super().__init__()
        self.item=items.Honey
        self.waittime=15
        self.name="Beehive"
    def grow(self,room,bees_delay):
        self.timer+=1
        waittime=self.waittime
        waittime-=(20-bees_delay)
        if self.timer>=waittime+random.randint(-1,1) and random.randint(0,1)==0 and self.active:
            self.timer=0
            room.collect.append(self.item)
            print(f"The Beehive dripped more honey!")
