import rooms,NPCS,items,inv,random
import achievements as ach
import save_load as sl

class Player:
    def __init__(self,world_type):
        self.inv=inv.Inv()
        self.room=rooms.Library()
        self.hp0=10
        self.hpmax=10
        self.gold=[items.GoldCoin for j in range(20)]
        self.deathtimes=0
        self.armor=[]
        for enemy in ["zombies","ogres","creepers","bears","dragons","monsters"]:
            exec("self."+enemy+"_killed=0")
        self.killed=0
        for animal in ["cows","sheeps","chickens","pigs","animals"]:
            exec("self."+animal+"_killed=0")
        self.trades=0
        for place in ["plains","houses","caves","places"]:
            exec("self."+place+"=0")
        self.explored=[self.room.uuid]
        self.quests=[]
        self.ach_got=[]
        self.worldname=""
        self.plants=[]
        if world_type!="new":
            sl.loadworld(self,world_type)
            self.places=self.houses+self.caves+self.plains
            self.killed=self.zombies_killed+self.ogres_killed+self.creepers_killed+self.bears_killed+self.dragons_killed+self.monsters_killed
            self.animals=self.cows_killed+self.sheeps_killed+self.chickens_killed+self.pigs_killed
        elif world_type=="new":
            del self.worldname
        self.room.enter(self)
        self.loop()
    def loop(self):
        for i in ach.zombies:
            if self.zombies_killed>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.ogres:
            if self.ogres_killed>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.creepers:
            if self.creepers_killed>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.dragons:
            if self.dragons_killed>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.monsters:
            if self.monsters_killed>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.bears:
            if self.bears_killed>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.killed:
            if self.killed>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.obtainable:
            found=0
            for j in self.inv.all:
                if j==i["item"]:
                    found+=1
            if found>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.trades:
            if self.trades>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.houses:
            if self.houses>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.caves:
            if self.caves>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for i in ach.places:
            if self.places>=i["amount"] and i["active"] is True and i not in self.ach_got:
                i["active"]=False
                print(f"""You won the achievement {i["name"]}!""")
                self.ach_got.append(i)
                for j in i["prizes"]:
                    self.inv.all.append(j)
        for j in self.inv.all:
            if j().name=="Gold Coin":
                self.inv.all.remove(j)
                self.gold.append(j)
            if j not in self.armor and issubclass(j,items.Armor):
                self.armor.append(j)
        self.inv.loop()
        #print("=====================================")
        if self.hp0<self.hpmax:
            if random.randint(0,2) in [0,1]:
                self.hp0+=0.25
        if self.hp0>self.hpmax:
            self.hp0=self.hpmax
        #print("=====================================")
        if self.hp0<=0:
            print("You died!")
            print("Restarting...")
            self.inv=inv.Inv()
            self.room=rooms.Library()
            self.hp0=10
            self.hpmax=10
            self.room.enter(self)
            self.deathtimes+=1
            if self.deathtimes>=20:
                self.deathtimes=20
                self.inv.potions.remove(items.HealPotion)
                self.inv.all.remove(items.HealPotion)
            self.gold=[items.GoldCoin for j in range(20-self.deathtimes)]
            #print("=====================================")
        print(f"Your health: {self.hp0}")
        print(f"Your gold: {len(self.gold)}")
        #print("=====================================")
        print("Your inventory:")
        if len(self.inv.all)==0: print("Empty")
        inv_dict={}
        inv_list=[]
        for i in self.inv.all:
            if True:#i().stackable:
                if i().name in inv_dict.keys():
                    inv_dict[i().name]+=1
                elif i().name not in inv_dict.keys():
                    inv_dict[i().name]=1
            elif not i().stackable:
                inv_list.append(i().name)
        for item in inv_dict.keys():
            print(f"{item} x{inv_dict[item]}")
        for item in inv_list:
            print(f"{item} x1")
        print("Your plants:")
        if len(self.plants)==0: print("Empty")
        pl_dict={}
        pl_list=[]
        for i in self.plants:
            if True:
                if i.name in pl_dict.keys():
                    pl_dict[i.name]+=1
                elif i.name not in pl_dict.keys():
                    pl_dict[i.name]=1
        for item in pl_dict.keys():
            print(f"{item} x{pl_dict[item]}")
        for item in pl_list:
            print(f"{item} x1")
        #print("=====================================")
        for quest in self.quests:
            amount=0
            for i in self.inv.all:
                if i().name==quest["item"]().name:
                    amount+=1
            if amount>=quest["amount"] and quest["active"] is True:
                quest["active"]=False
                print(f"""You have completed the quest '{quest["name"]}'! Go to the {quest["owner"].name} to collect your reward!""")
        #print("=====================================")
        playing=self.room.loop(self)
        if playing=="stop" or playing=="stop playing":
            def q():
                pass
            self.loop=q
            return False
        else:
            return True
