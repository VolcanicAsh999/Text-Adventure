import random

class Potion:
    def __init__(self):
        self.heal=0
        self.attack=False
        self.damage=0
        self.name="Potion"
        self.stackable=False
    def use(self,room,player):
        if self.attack is False:
            player.hp0+=self.heal
        elif self.attack is True:
            enemy=room
            enemy.hp-=self.damage

class HealPotion(Potion):
    def __init__(self):
        super().__init__()
        self.heal=3
        self.name="Heal Potion"

class StrongHealPotion(HealPotion):
    def __init__(self):
        super().__init__()
        self.heal=5
        self.name="Strong Heal Potion"

class HurtPotion(Potion):
    def __init__(self):
        super().__init__()
        self.attack=True
        self.damage=2
        self.name="Hurt Potion"

class StrongHurtPotion(HurtPotion):
    def __init__(self):
        super().__init__()
        self.damage=4
        self.name="Strong Hurt Potion"

class LavaBucket(HurtPotion):
    def __init__(self):
        super().__init__()
        self.damage=7
        self.name="Lava Bucket"

class HitAllPotion(HurtPotion):
    def __init__(self):
        super().__init__()
        self.name="Hit All Potion"
    def use(self,room,player):
        for enemy in player.room.enemies:
            enemy.hp-=self.damage

class StrongHitAllPotion(HitAllPotion):
    def __init__(self):
        super().__init__()
        self.name="Strong Hit All Potion"
        self.damage=4

class Sword:
    def __init__(self):
        self.damage=0
        self.name="Sword"
        self.stackable=False
    def use(self,enemy,player):
        damage=self.damage
        for item in player.inv.books:
            if item().name=="Swords Book":
                damage+=1
                break
        enemy.hp-=damage
        print(f"The {self.name} hit the {enemy.name} for {damage} hp!")
                
            
class DeadlySword(Sword):
    def __init__(self):
        super().__init__()
        self.damage=6
        self.name="Deadly Sword"

class DrainingSword(Sword):
    def __init__(self):
        super().__init__()
        self.damage=3
        self.name="Draining Sword"
    def use(self,enemy,player):
        super().use(enemy,player)
        player.hp0+=self.damage

class HealingSword(Sword):
    def __init__(self):
        super().__init__()
        self.damage=2
        self.name="Healing Sword"
    def use(self,enemy,player):
        super().use(enemy,player)
        player.hp0+=1

class DragonSlayer(Sword):
    def __init__(self):
        super().__init__()
        self.damage=10
        self.name="Dragon Slayer"

class Gun(Sword):
    def __init__(self):
        super().__init__()
        self.damage=11
        self.name="Gun"

class Book:
    def __init__(self):
        self.text1=""
        self.text2=""
        self.text3=""
        self.name="Book"
        self.revealed=False
        self.stackable=False
    def use(self,room,player):
        if self.text3!="" and self.revealed:
            print(self.text3)
        elif self.text3!="" and not self.revealed:
            print(self.text1)
            print(self.text2)
            for e in player.inv.books:
                if e().name=="Book Of Secrets":
                    print("Use the Book Of Secrets to decode?")
                    answer=input("> ")
                    if answer.lower()!="no":
                        print("You decoded it!")
                        print("It says: ")
                        print(self.text3)
                        self.revealed=True
        elif self.text3=="":
            print(self.text1)
            print(self.text2)

class Map(Book):
    def __init__(self):
        super().__init__()
        self.name="Map"
    def use(self,room,player):
        if self.text3!="" and self.revealed:
            print(self.text3)
        elif self.text3!="" and not self.revealed:
            print(self.text1)
            print(self.text2)
            for e in player.inv.books:
                if e().name=="Book Of Secrets":
                    print("Use the Book Of Secrets to reveal?")
                    answer=input("> ")
                    if answer.lower()!="no":
                        print("You revealed it!")
                        print("It says: ")
                        print(self.text3)
                        self.revealed=True
        elif self.text3=="":
            print(self.text1)
            print(self.text2)

class TreasureMap(Map):
    def __init__(self):
        super().__init__()
        self.text3="""_______________________________
| \/  <- Treasure             |   
| /\ _   Cave 5               |
|     \________-----_   Cave 3|
|                    \_____   |
|         Cave 2     __    |  |
|Cave 1  ___________/  \___/  |
|   ____/                     |
| Blacksmith shop             |
-------------------------------"""
        self.text2="Get the Book of Secrets to reveal this."
        self.text1="""_______________________________
|                             |
|                             |
|                             |
|                             |
|                             |
|                             |
|                             |
|                             |
-------------------------------"""
        self.name="Treasure Map"

class BookOfSecrets(Book):
    def __init__(self):
        super().__init__()
        self.text1="This book can help decode secret languages"
        self.text2="and reveal blank maps."
        self.name="Book Of Secrets"

class TownMap(Map):
    def __init__(self):
        super().__init__()
        self.text1="""_________________________________________________
|Blacksmith Shop|    Library    |     Hotel     |
|-----------------------------------------------|
|Normal House 1 |     Store     |   Gold Mine   |
|-----------------------------------------------|
|Normal House 2 |  Butcher Shop |Normal House 3 |
-------------------------------------------------
"""
        self.name="Town Map"

class TownMap2(Map):
    def __init__(self):
        super().__init__()
        self.text1="""_________________________________________________________________
|Normal House 4 |    Library    |Alchemist Shop |Normal House 3 |
|---------------------------------------------------------------|
|  Flower Shop  |Normal House 1 |Jeweller's Shop|Normal House 2 |
|---------------------------------------------------------------|
|    Tannery    |     Store     |   Gold Mine   |    School     |
-----------------------------------------------------------------
"""
        self.name="Town Map 2"

class TownMap3(Map):
    def __init__(self):
        super().__init__()
        self.text1="""_________________________________________________
|     School    |Normal House 1 |  Flower Shop  |
|-----------------------------------------------|
|     Store     |Alchemist Shop |Normal House 2 |
|-----------------------------------------------|
|Normal House 3 |    Tannery    |     Hotel     |
-------------------------------------------------
"""
        self.name="Town Map 3"

class SwordsBook(Book):
    def __init__(self):
        super().__init__()
        self.text1="""Deadly Sword - 5
Draining Sword - 3, heals by 3
Healing Sword - 2, heals by 1
Dragon Slayer - 10, never misses the Dragon.
Gun - 11"""
        self.text2="This book boosts all your sword's damage by 1 when you have it."
        self.name="Swords Book"

class CaveExitsBook(Book):
    def __init__(self):
        super().__init__()
        self.text1=""
        self.text2="Get the Book of Secrets to reveal this."
        self.text3="""
Cave 10 - Cave 9, Gold Mine 2
Cave 9 - Cave 8, Cave 3, Cave 10
Cave 8 - Cave 7, Cave 9, Gold Mine
Cave 7 - Cave 6, Cave 8, Cave 13
Cave 6 - Cave 4, Cave 7, Cave 17
Cave 5 - Cave 3
Cave 4 - Cave 3, Cave 6
Cave 3 - Cave 2, Cave 4, Cave 5
Cave 2 - Cave 1, Cave 3
Cave 1 - Cave 2, Blacksmith Shop"""
        self.name="Cave Exits Book"
        
class GoldCoin:
    def __init__(self):
        self.name="Gold Coin"
    def use(self,room,player):
        pass

class Other:
    def __init__(self):
        self.name="Other"
        self.stackable=True
    def use(self,room,player):
        pass

class Feather(Other):
    def __init__(self):
        super().__init__()
        self.name="Feather"

class Gunpowder(Other):
    def __init__(self):
        super().__init__()
        self.name="Gunpowder"

class Keycard(Other):
    def __init__(self):
        super().__init__()
        self.name="Keycard"
        self.stackable=False

class Bone(Other):
    def __init__(self):
        super().__init__()
        self.name="Bone"

class GoldNugget(Other):
    def __init__(self):
        super().__init__()
        self.name="Gold Nugget"

class Ruby(Other):
    def __init__(self):
        super().__init__()
        self.name="Ruby"

class Leather(Other):
    def __init__(self):
        super().__init__()
        self.name="Leather"

class Grass(Other):
    def __init__(self):
        super().__init__()
        self.name="Grass"

class Wheat(Other):
    def __init__(self):
        super().__init__()
        self.name="Wheat"

class Wool(Other):
    def __init__(self):
        super().__init__()
        self.name="Wool"

class Iron(Other):
    def __init__(self):
        super().__init__()
        self.name="Iron"

class Diamond(Other):
    def __init__(self):
        super().__init__()
        self.name="Diamond"

class Food:
    def __init__(self):
        self.name="Food"
        self.hp=0
        self.stackable=True
    def use(self,room,player):
        player.hp0+=self.hp
        print(f"The {self.name} healed you by {self.hp} hp!")

class Chicken(Food):
    def __init__(self):
        super().__init__()
        self.name="Chicken"
        self.hp=1.5

class Beef(Food):
    def __init__(self):
        super().__init__()
        self.name="Beef"
        self.hp=2

class Mutton(Food):
    def __init__(self):
        super().__init__()
        self.name="Mutton"
        self.hp=1.75

class Pork(Food):
    def __init__(self):
        super().__init__()
        self.name="Pork"
        self.hp=2

class Bread(Food):
    def __init__(self):
        super().__init__()
        self.name="Bread"
        self.hp=1.25

class Tomato(Food):
    def __init__(self):
        super().__init__()
        self.name="Tomato"
        self.hp=1

class Apple(Food):
    def __init__(self):
        super().__init__()
        self.name="Apple"
        self.hp=1.25

class Orange(Food):
    def __init__(self):
        super().__init__()
        self.name="Orange"
        self.hp=1

class Carrot(Food):
    def __init__(self):
        super().__init__()
        self.name="Carrot"
        self.hp=1

class Berry(Food):
    def __init__(self):
        super().__init__()
        self.name="Berry"
        self.hp=0.5

class ApplePie(Food):
    def __init__(self):
        super().__init__()
        self.name="Apple Pie"
        self.hp=2

class Honey(Food):
    def __init__(self):
        super().__init__()
        self.name="Honey"
        self.hp=0

class Honeycomb(Food):
    def __init__(self):
        super().__init__()
        self.name="Honeycomb"
        self.hp=0.75

class RottenMeat(Food):
    def __init__(self):
        super().__init__()
        self.name="Rotten Meat"
        self.hp=random.choice([-0.5,-0.25,0,0.25,0.5])

class PoisonousFlower(Food):
    def __init__(self):
        super().__init__()
        self.name="Poisonous Flower"
        self.hp=random.choice([-1.25,-1,-0.75])

class Armor(Other):
    def __init__(self):
        super().__init__()
        self.name="Armor"
        self.red=0.5
        self.stackable=False
    def apply_damage_reduction(self):
        bonus=random.choice([-0.25,0,0.25])
        #print(f"The {self.name} protected you from {self.red+bonus} damage.")
        return self.red+bonus

class LeatherBoots(Armor):
    def __init__(self):
        super().__init__()
        self.name="Leather Boots"
        self.red=0.5

class LeatherLeggings(Armor):
    def __init__(self):
        super().__init__()
        self.name="Leather Leggings"
        self.red=1

class LeatherChest(Armor):
    def __init__(self):
        super().__init__()
        self.name="Leather Chest"
        self.red=1.5

class LeatherHelmet(Armor):
    def __init__(self):
        super().__init__()
        self.name="Leather Helmet"
        self.red=0.75

class IronBoots(Armor):
    def __init__(self):
        super().__init__()
        self.name="Iron Boots"
        self.red=1.5

class IronLeggings(Armor):
    def __init__(self):
        super().__init__()
        self.name="Iron Leggings"
        self.red=2.5

class IronChest(Armor):
    def __init__(self):
        super().__init__()
        self.name="Iron Chest"
        self.red=3

class IronHelmet(Armor):
    def __init__(self):
        super().__init__()
        self.name="Iron Helmet"
        self.red=2

class DiamondBoots(Armor):
    def __init__(self):
        super().__init__()
        self.name="Diamond Boots"
        self.red=2.5

class DiamondLeggings(Armor):
    def __init__(self):
        super().__init__()
        self.name="Diamond Leggings"
        self.red=3

class DiamondChest(Armor):
    def __init__(self):
        super().__init__()
        self.name="Diamond Chest"
        self.red=3.5

class DiamondHelmet(Armor):
    def __init__(self):
        super().__init__()
        self.name="Diamond Helmet"
        self.red=2.75

class Special:
    def __init__(self):
        self.name="Special"
        self.stackable=False

items=[]
class Sack(Special):
    def __init__(self):
        self.name="Sack"
    def use(self,room,player):
        answer=input("Would you like to add or remove items? > ")
        if answer.lower()=="add":
            answer2=input("Which items? (write like item1, item2, item3, ...) > ").lower().split(', ')
            to_lose=[]
            for i in answer2:
                for j in player.inv.all:
                    if j().name.lower()==i:
                        items.append(j)
                        to_lose.append(j)
            for j in to_lose:
                if True:
                    if j in player.inv.all:
                        player.inv.all.remove(j)
                        if issubclass(j,Book):
                            player.inv.books.remove(j)
                        elif issubclass(j,Potion):
                            player.inv.potions.remove(j)
                        elif issubclass(j,Sword):
                            player.inv.swords.remove(j)
                        elif issubclass(j,Food) or hasattr(j,"hp"):
                            player.inv.food.remove(j)
                        elif issubclass(j,Other) or issubclass(j,Special):
                            player.inv.other.remove(j)
        elif answer.lower()=="remove":
            inv_dict={}
            print("Items in sack: ")
            for i in items:
                if True:
                    if i().name in inv_dict.keys():
                        inv_dict[i().name]+=1
                    elif i().name not in inv_dict.keys():
                        inv_dict[i().name]=1
            for item in inv_dict.keys():
                print(f"{item} x{inv_dict[item]}")
            answer2=input("Which item types to remove? (write like item1, item2, item3, ...) > ").lower().split(', ')
            to_lose=[]
            for i in answer2:
                for j in items:
                    if j().name.lower()==i:
                        player.inv.all.append(j)
                        if issubclass(j,Book):
                            player.inv.books.append(j)
                        elif issubclass(j,Potion):
                            player.inv.potions.append(j)
                        elif issubclass(j,Sword):
                            player.inv.swords.append(j)
                        elif issubclass(j,Food) or hasattr(j,"hp"):
                            player.inv.food.append(j)
                        elif issubclass(j,Other) or issubclass(j,Special) or issubclass(j,Armor):
                            player.inv.other.append(j)
                        to_lose.append(j)
            for i in to_lose:
                items.remove(i)
            player.inv.loop()
