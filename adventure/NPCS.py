import items,random,plants
from items import Special

class NPC:
    
    def __init__(self):
        self.sales=[]
        self.hp0=10
        self.name="NPC"

    def sell(self,player):
        for i in self.sales:
            if i["type"]=="gold":
                #print("=====================================")
                print(f"""{self.name} > 'I will take {i["cost"]} gold for 1 {i["item"]().name}.'""")
                answer=input("Would you like to buy it? > ")
                if answer.lower()=="no":
                    continue
                elif answer.lower()=="yes":
                    if len(player.gold)>=i["cost"]:
                        for j in range(i["cost"]):
                            player.gold.remove(player.gold[0])
                        if issubclass(i["item"],items.Book):
                            player.inv.books.append(i["item"])
                        elif issubclass(i["item"],items.Potion):
                            player.inv.potions.append(i["item"])
                        elif issubclass(i["item"],items.Sword):
                            player.inv.swords.append(i["item"])
                        elif issubclass(i["item"],items.Food) or hasattr(i["item"],"hp"):
                            player.inv.food.append(i["item"])
                        elif issubclass(i["item"],items.Other) or issubclass(i["item"],Special):
                            player.inv.other.append(i["item"])
                        player.inv.all.append(i["item"])
                        player.trades+=1
                    else:
                        print("Not enough gold!")
                        continue
            elif i["type"]=="item":
                #print("=====================================")
                print(f"""{self.name} > 'I will take 1 {i["item"]().name} for {i["amount"]} gold.'""")
                answer=input("Would you like to buy the gold? > ")
                if answer.lower()=="no":
                    continue
                elif answer.lower()=="yes":
                    if i["item"] in player.inv.all:
                        if issubclass(i["item"],items.Book):
                            player.inv.books.remove(i["item"])
                        elif issubclass(i["item"],items.Potion):
                            player.inv.potions.remove(i["item"])
                        elif issubclass(i["item"],items.Sword):
                            player.inv.swords.remove(i["item"])
                        elif issubclass(i["item"],items.Food):
                            player.inv.food.remove(i["item"])
                        elif issubclass(i["item"],items.Other) or issubclass(i["item"],Special):
                            player.inv.other.remove(i["item"])
                        for j in range(i["amount"]):
                            player.gold.append(items.GoldCoin)
                        player.inv.all.remove(i["item"])
                        player.trades+=1
                    else:
                        print("You don't have the item!")
                        continue
            elif i["type"]=="plant_sell":
                print(f"""{self.name} > 'I will take {i["cost"]} gold for 1 {i["plant"].name}.'""")
                answer=input("Would you like to buy it? > ")
                if answer.lower()=="no":
                    continue
                elif answer.lower()=="yes":
                    if len(player.gold)>=i["cost"]:
                        for j in range(i["cost"]):
                            player.gold.remove(player.gold[0])
                        player.plants.append(i["plant"])
                    else:
                        print("Not enough gold!")
                        continue
            elif i["type"]=="plant_buy":
                print(f"""{self.name} > 'I will take 1 {i["plant"].name} for {i["amount"]} gold.'""")
                answer=input("Would you like to buy the gold? > ")
                if answer.lower()=="no":
                    continue
                elif answer.lower()=="yes":
                    for plant in player.plants:
                        if plant.name==i["plant"].name:
                            plant_to_sell=plant
                            break
                    try:
                        p=plant_to_sell
                    except NameError:
                        print("You don't have the plant!")
                        continue
                    player.plants.remove(plant_to_sell)
                    for j in range(i["amount"]):
                        player.gold.append(items.GoldCoin)
            elif i["type"]=="quest":
                active=i["active"]
                for q in player.quests:
                    if q["name"]==i["name"] and type(q["owner"])==type(self):
                        active=q["active"]
                        break
                for quest in player.quests:
                    if quest==i:
                        amount=0
                        for j in player.inv.all:
                            if j().name==quest["item"]().name:
                                amount+=1
                        if amount<i["amount"]:
                            q["active"]=True
                            i["active"]=True
                            active=True
                            print(f'Not enought {quest["item"]().name}s')
                if active is True:
                    found=False
                    for q in player.quests:
                        if q["name"]==i["name"]:
                            found=True
                            break
                    if found: continue
                    answer=input(f"""{self.name} > 'Would you like to go on the quest '{i["name"]}' for {i["amount"]} {i["item"]().name}s? > """)
                    if answer.lower()=="yes":
                        found=False
                        for q in player.quests:
                            if q["name"]==i["name"]:
                                found=True
                                break
                        if not found:
                            player.quests.append(i)
                            print("You accepted the quest.")
                        else:
                            print("You already have this quest.")
                elif active is False:
                    i["active"]=True
                    print(f"""You have completed the quest '{i["name"]}'! Here is your reward!""")
                    for j in i["prize"]:
                        player.inv.all.append(j)
                        if issubclass(j,items.Book):
                            player.inv.books.append(j)
                        elif issubclass(j,items.Potion):
                            player.inv.potions.append(j)
                        elif issubclass(j,items.Sword):
                            player.inv.swords.append(j)
                        elif issubclass(j,items.Food) or hasattr(j,"hp"):
                            player.inv.food.append(j)
                        elif issubclass(j,items.Other) or issubclass(i["item"],Special):
                            player.inv.other.append(j)
                        print(f"{j().name}",end=', ')
                    print()
                    for j in range(i["amount"]):
                        player.inv.all.remove(i["item"])
                        if True:
                            if issubclass(i["item"],items.Book):
                                player.inv.books.remove(i["item"])
                            elif issubclass(i["item"],items.Potion):
                                player.inv.potions.remove(i["item"])
                            elif issubclass(i["item"],items.Sword):
                                player.inv.swords.remove(i["item"])
                            elif issubclass(i["item"],items.Food) or hasattr(i["item"],"hp"):
                                player.inv.food.remove(i["item"])
                            elif issubclass(i["item"],items.Other) or issubclass(i["item"],Special):
                                player.inv.other.remove(i["item"])
                    for k in player.quests:
                        if k["name"]==i["name"]:
                            player.quests.remove(k)
                            break
                del active
        #print("=====================================")
        return

class Librarian(NPC):
    def __init__(self):
        super().__init__()
        self.sales=[{"type":"gold","cost":20,"item":items.TreasureMap},{"type":"item","item":items.HealPotion,"amount":7},{"type":"gold","cost":17,"item":items.TownMap}]
        self.name="Librarian"

class Blacksmith(NPC):
    def __init__(self):
        super().__init__()
        self.name="Blacksmith"
        self.sales=[{"type":"item","item":items.DrainingSword,"amount":27},{"type":"gold","cost":4,"item":items.HurtPotion},{"type":"gold","cost":19,"item":items.StrongHurtPotion}]

class HotelOwner(NPC):
    def __init__(self):
        super().__init__()
        self.name="Hotel Owner"
        self.sales=[{"type":"gold","cost":9,"item":items.Keycard}]

class Civilian(NPC):
    def __init__(self):
        super().__init__()
        self.name="Civilian"

class Miner(NPC):
    def __init__(self,num):
        super().__init__()
        self.name=f"Miner {num}"
        self.sales=[{"type":"item","item":items.Chicken,"amount":7},{"type":"item","item":items.Beef,"amount":11}]

class Butcher(NPC):
    def __init__(self):
        super().__init__()
        self.name="Butcher"
        self.sales=[{"type":"gold","cost":6,"item":items.Chicken},{"type":"gold","cost":9,"item":items.Beef}]

class ShopKeeper(NPC):
    def __init__(self):
        super().__init__()
        self.name="Shopkeeper"
        self.sales=[{"type":"gold","cost":4,"item":items.Tomato},{"type":"gold","cost":5,"item":items.Bread},{"type":"gold","cost":7,"item":items.Apple}]

class Miner2(NPC):
    def __init__(self,num):
        super().__init__()
        self.name=f"Miner {num}"
        self.sales=[{"type":"item","item":items.CaveExitsBook,"amount":23},{"type":"gold","cost":7,"item":items.GoldNugget},{"type":"gold","cost":6,"item":items.Ruby}]

class Jeweller(NPC):
    def __init__(self):
        super().__init__()
        self.name="Jeweller"
    def sell(self,player):
        for item in player.inv.all:
            if item().name=="Gold Nugget":
                a=input("Jeweller > 'Would you like me to inspect your Gold Nugget?' > ")
                if a.lower()!="no":
                    worth=random.randint(5,11)
                    self.sales.append({"item":items.GoldNugget,"amount":worth,"active":True})
                    print(f"Jeweller > 'That would be worth {worth} Gold.'")
        for s in range(len(self.sales)):
            sale=self.sales[s]
            if sale["item"]().name=="Gold Nugget" and sale["active"] is True:
                print(f"""Jeweller > 'I will give you {sale["amount"]} Gold for a Gold Nugget.""")
                an=input("Would you like to buy the gold? > ")
                if an.lower()=="yes":
                    player.inv.all.remove(sale["item"])
                    player.inv.other.remove(sale["item"])
                    for j in range(sale["amount"]):
                        player.gold.append(items.GoldCoin)
                sale["active"]=False
        for item in player.inv.all:
            if item().name=="Ruby":
                a=input("Jeweller > 'Would you like me to inspect your Ruby?' > ")
                if a.lower()!="no":
                    worth=random.randint(4,12)
                    self.sales.append({"item":items.Ruby,"amount":worth,"active":True})
                    print(f"Jeweller > 'That would be worth {worth} Gold.'")
        for s in range(len(self.sales)):
            sale=self.sales[s]
            if sale["item"]().name=="Ruby" and sale["active"] is True:
                print(f"""Jeweller > 'I will give you {sale["amount"]} Gold for a Ruby.""")
                an=input("Would you like to buy the gold? > ")
                if an.lower()=="yes":
                    player.inv.all.remove(sale["item"])
                    player.inv.other.remove(sale["item"])
                    for j in range(sale["amount"]):
                        player.gold.append(items.GoldCoin)
                sale["active"]=False
                    
class StoreKeeper(NPC):
    def __init__(self):
        super().__init__()
        self.name="Shopkeeper"
        self.sales=[{"type":"item","item":items.Beef,"amount":13},{"type":"gold","cost":3,"item":items.Carrot},{"type":"gold","cost":7,"item":items.Chicken}]

class Librarian2(NPC):
    def __init__(self):
        super().__init__()
        self.name="Librarian"
        self.sales=[{"type":"item","item":items.TreasureMap,"amount":23},{"type":"gold","cost":11,"item":items.TownMap2}]

class Teacher(NPC):
    def __init__(self):
        super().__init__()
        self.name="Teacher"
        self.sales=[{"name":"Gimme some Bones","owner":self,"active":True,"type":"quest","item":items.Bone,"amount":10,"prize":[items.LavaBucket]},{"name":"I'm hurt!","owner":self,"active":True,"type":"quest","item":items.HealPotion,"amount":2,"prize":[items.Beef for i in range(3)]}]

class Alchemist(NPC):
    def __init__(self):
        super().__init__()
        self.name="Alchemist"
        self.sales=[{"type":"gold","item":items.HitAllPotion,"cost":15},{"type":"gold","item":items.StrongHealPotion,"cost":13},{"type":"item","item":items.HurtPotion,"amount":7}]

class LeatherWorker(NPC):
    def __init__(self):
        super().__init__()
        self.name="Leatherworker"
        self.sales=[{"type":"item","item":items.Leather,"amount":1},{"type":"gold","item":items.LeatherChest,"cost":6},{"type":"gold","item":items.LeatherHelmet,"cost":4}]

class Florist(NPC):
    def __init__(self):
        super().__init__()
        self.name="Florist"
        self.sales=[{"type":"plant_sell","plant":plants.TomatoPlant(),"cost":6},{"type":"plant_buy","plant":plants.BerryBush(),"amount":3}]

class Teacher2(NPC):
    def __init__(self):
        super().__init__()
        self.name="Teacher"
        self.sales=[{"name":"I need some space","owner":self,"active":True,"type":"quest","item":items.Sack,"amount":1,"prize":[items.IronChest,items.IronLeggings]},{"name":"I need to translate","owner":self,"active":True,"type":"quest","item":items.BookOfSecrets,"amount":1,"prize":[items.Keycard,items.SwordsBook,items.ApplePie]},{"name":"May I have some lava?","owner":self,"active":True,"type":"quest","item":items.LavaBucket,"amount":2,"prize":[items.StrongHitAllPotion,items.StrongHitAllPotion,items.DragonSlayer]}]

class Alchemist2(NPC):
    def __init__(self):
        super().__init__()
        self.name="Alchemist"
        self.sales=[{"type":"gold","item":items.StrongHurtPotion,"cost":10},{"type":"item","item":items.StrongHitAllPotion,"amount":15},{"type":"gold","item":items.HitAllPotion,"cost":7}]

class Storekeeper(NPC):
    def __init__(self):
        super().__init__()
        self.name="Shopkeeper"
        self.sales=[{"type":"gold","item":items.ApplePie,"cost":5},{"type":"item","item":items.Honeycomb,"amount":7}]

class Florist2(NPC):
    def __init__(self):
        super().__init__()
        self.name="Florist"
        self.sales=[{"type":"plant_sell","plant":plants.OrangeTree(),"cost":11},{"type":"plant_buy","plant":plants.Beehive(),"amount":7},{"type":"plant_sell","plant":plants.AppleTree(),"cost":8}]

class Tanner(NPC):
    def __init__(self):
        super().__init__()
        self.name="Leatherworker"
        self.sales=[{"type":"item","item":items.Leather,"amount":2},{"type":"gold","item":items.Sack,"cost":15},{"type":"gold","item":items.LeatherLeggings,"cost":9}]
