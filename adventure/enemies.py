import items,random

class Enemy:
    def __init__(self):
        self.damage=0
        self.hp=10
        self.name="Enemy"
    def fight(self,room,player):
        a={"1":None,"2":None,"3":None,"4":None}
        if self.hp<=0:
            room.enemies.remove(self)
            print(f"{self.name} died!")
            #print("=====================================")
            return a
        if True:
            if len(player.armor)>0:
                print("Which armor items will you use?")
                for armor_item in player.armor:
                    print(f'Name - {armor_item().name}        Protection (average) - {armor_item().red}')
            for item in player.inv.other:
                if "Boots" in item().name:
                    answer1=input("Boots > ")
                    break
            for item in player.inv.other:
                if "Leggings" in item().name:
                    answer2=input("Leggings > ")
                    break
            for item in player.inv.other:
                if "Chest" in item().name:
                    answer3=input("Chestplate > ")
                    break
            for item in player.inv.other:
                if "Helmet" in item().name:
                    answer4=input("Helmet > ")
                    break
            if True:
                try:
                    q=answer1
                except Exception:
                    answer1=""
                try:
                    q=answer2
                except Exception:
                    answer2=""
                try:
                    q=answer3
                except Exception:
                    answer3=""
                try:
                    q=answer4
                except Exception:
                    answer4=""
            damage=self.damage
            for item in player.inv.other:
                if answer1.lower() in item().name.lower() and "Boots" in item().name:
                    reduct=item().apply_damage_reduction()
                    damage-=reduct
                    print(f"The {item().name} protected you from {reduct} damage!")
                    a["1"]=item
                    break
            for item in player.inv.other:
                if answer2.lower() in item().name.lower() and "Leggings" in item().name:
                    reduct=item().apply_damage_reduction()
                    damage-=reduct
                    print(f"The {item().name} protected you from {reduct} damage!")
                    a["2"]=item
                    break
            for item in player.inv.other:
                if answer3.lower() in item().name.lower() and "Chest" in item().name:
                    reduct=item().apply_damage_reduction()
                    damage-=reduct
                    print(f"The {item().name} protected you from {reduct} damage!")
                    a["3"]=item
                    break
            for item in player.inv.other:
                if answer4.lower() in item().name.lower() and "Helmet" in item().name:
                    reduct=item().apply_damage_reduction()
                    damage-=reduct
                    print(f"The {item().name} protected you from {reduct} damage!")
                    a["4"]=item
                    break
        if damage<=0:
            damage=0
        if random.randint(0,2) in [0,1]:
            player.hp0-=damage
            print(f"{self.name} hit you for {damage} hp!")
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
                return a
            elif issubclass(i,items.Potion) and i().name.lower()==answer.lower() and i().attack is True:
                i().use(self,player)
                #print("=====================================")
                player.inv.potions.remove(i)
                player.inv.all.remove(i)
                return a
        if current==self.hp:
            print("You use your fists...")
            #print("=====================================")
            self.hp-=0.5
        return a

class Bear(Enemy):
    def __init__(self):
        super().__init__()
        self.damage=4
        self.hp=3
        self.name="Bear"

class Ogre(Enemy):
    def __init__(self):
        super().__init__()
        self.damage=4
        self.hp=5
        self.name="Ogre"

class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.damage=2
        self.hp=11
        self.name="Zombie"

class Creeper(Enemy):
    def __init__(self):
        super().__init__()
        self.damage=0
        self.hp=10
        self.name="Creeper"
    def fight(self,room,player):
        armor=super().fight(room,player)
        if armor==None: return armor
        if random.choice(["yes","yes","yes","yes","yes","yes","no"])=="yes":
            print(f"{self.name} exploded!")
            damage=8
            if armor["1"]!=None:
                reduct=round(armor["1"]().apply_damage_reduction()/2)
                print(f"""The {armor["1"]().name} protected you from {reduct} damage.""")
                damage-=reduct
            if armor["2"]!=None:
                reduct=round(armor["2"]().apply_damage_reduction()/2)
                print(f"""The {armor["2"]().name} protected you from {reduct} damage.""")
                damage-=reduct
            if armor["3"]!=None:
                reduct=round(armor["3"]().apply_damage_reduction()/2)
                print(f"""The {armor["3"]().name} protected you from {reduct} damage.""")
                damage-=reduct
            if armor["4"]!=None:
                reduct=round(armor["4"]().apply_damage_reduction()/2)
                print(f"""The {armor["4"]().name} protected you from {reduct} damage.""")
                damage-=reduct
            if damage<=0:
                damage=0
            self.hp=0
            player.hp0-=damage
            print(f"You took {damage} damage!")

class Monster(Enemy):
    def __init__(self):
        super().__init__()
        self.damage=4
        self.name="Monster"
        self.hp=8

class Dragon(Enemy):
    def __init__(self):
        super().__init__()
        self.damage=6
        self.name="Dragon"
        self.hp=17
    def fight(self,room,player):
        if self.hp<=0:
            room.enemies.remove(self)
            print(f"{self.name} died!")
            #print("=====================================")
            return
        if True:
            if len(player.armor)>0:
                print("Which armor items will you use?")
                for armor_item in player.armor:
                    print(f'Name - {armor_item().name}        Protection (average) - {armor_item().red}')
            for item in player.inv.other:
                if "Boots" in item().name:
                    answer1=input("Boots > ")
                    break
            for item in player.inv.other:
                if "Leggings" in item().name:
                    answer2=input("Leggings > ")
                    break
            for item in player.inv.other:
                if "Chest" in item().name:
                    answer3=input("Chestplate > ")
                    break
            for item in player.inv.other:
                if "Helmet" in item().name:
                    answer4=input("Helmet > ")
                    break
            if True:
                try:
                    q=answer1
                except Exception:
                    answer1=""
                try:
                    q=answer2
                except Exception:
                    answer2=""
                try:
                    q=answer3
                except Exception:
                    answer3=""
                try:
                    q=answer4
                except Exception:
                    answer4=""
            damage=self.damage
            for item in player.inv.other:
                if answer1.lower() in item().name.lower() and "Boots" in item().name:
                    reduct=item().apply_damage_reduction()
                    damage-=reduct
                    print(f"The {item().name} protected you from {reduct} damage!")
                    break
            for item in player.inv.other:
                if answer2.lower() in item().name.lower() and "Leggings" in item().name:
                    reduct=item().apply_damage_reduction()
                    damage-=reduct
                    print(f"The {item().name} protected you from {reduct} damage!")
                    break
            for item in player.inv.other:
                if answer3.lower() in item().name.lower() and "Chest" in item().name:
                    reduct=item().apply_damage_reduction()
                    damage-=reduct
                    print(f"The {item().name} protected you from {reduct} damage!")
                    break
            for item in player.inv.other:
                if answer4.lower() in item().name.lower() and "Helmet" in item().name:
                    reduct=item().apply_damage_reduction()
                    damage-=reduct
                    print(f"The {item().name} protected you from {reduct} damage!")
                    break
            if damage<=0:
                damage=0
            if random.randint(0,2) in [0,1]:
                player.hp0-=damage
                print(f"{self.name} hit you for {damage} hp!")
        print("Which weapon would you like to use? ")
        for i in player.inv.all:
            if issubclass(i,items.Sword):
                print(i().name)
            elif issubclass(i,items.Potion):
                if i().attack is True:
                    print(i().name)
        #print("=====================================")
        answer=input("> ")
        if True:
            current=self.hp
            for i in player.inv.all:#range(len(player.inv.all)):
                e=player.inv.all
                if issubclass(i,items.Sword) and i().name.lower()==answer.lower():
                    if random.randint(0,2) in [0,1] or i().name=="Dragon Slayer":
                        i().use(self,player)
                        #print("=====================================")
                    else:
                        print("You missed!")
                        #print("=====================================")
                    return
                elif issubclass(i,items.Potion) and i().name.lower()==answer.lower() and i().attack is True:
                    if random.randint(0,2) in [0,1] or i().name=="Lava Bucket":
                        i().use(self,player)
                        #print("=====================================")
                    else:
                        print("You missed!")
                        #print("=====================================")
                    player.inv.potions.remove(i)
                    player.inv.all.remove(i)
                    return
            if current==self.hp:
                print("You use your fists...")
                #print("=====================================")
                if random.randint(0,2) in [0,1]:
                    self.hp-=0.5
                else:
                    print("You missed!")
                    #print("=====================================")
