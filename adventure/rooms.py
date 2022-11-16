import items, random, time
import NPCS as npcs
import enemies as en
import achievements as ach
import animals as an
import recipes as r
import plants as p
from items import Special

class Room:
    def __init__(self):
        self.items=[]
        self.NPCS=[]
        self.name="Room"
        self.uuid=self.name
        self.exits=[]
        self.hidden=False
        self.needed=None
        self.hidden2=None
        self.storedaction=""
    def enter(self,player):
        #print("=====================================")
        print(f"You enter the {self.name}.")
        #print("=====================================")
        print("Available NPCS:")
        if len(self.NPCS)==0: print("None")
        for i in self.NPCS:
            print(i.name)
        #print("=====================================")
    def exit(self,player,room_to_enter):
        if self.uuid in player.explored:
            pass
        elif self.uuid not in player.explored:
            player.houses+=1
            player.places+=1
            player.explored.append(self.uuid)
        #print("=====================================")
        print(f"You exit the {self.name}.")
        room=room_to_enter()
        player.room=room
        room.storedaction=self.storedaction
        room.enter(player)
    def loop(self,player):
        answer=input("What would you like to do? > ")
        #print("=====================================")
        if answer.lower()=="":
            answer=self.storedaction
        self.storedaction=answer
        if answer.lower()=="exit":
            self.on_exit(player)
        elif answer.lower()=="trade":
            self.on_trade(player)
        elif answer.lower()=="explore":
            self.on_explore(player)
        elif answer.lower().startswith("use item "):
            self.on_use_item(player,answer)
        elif answer.lower()=="ach":
            self.on_ach(player)
        elif answer.lower()=="help":
            self.on_help(player)
        elif answer.lower()=="quests":
            self.on_quests(player)
        elif answer.lower()=="combine":
            self.on_combine(player)
        elif answer.lower()=="stop playing" or answer.lower()=="stop":
            self.stop(player)
        elif answer=="qwertyuiop":
            self.cheat_code(player)
        elif answer=="asdfghjkl":
            self.cheat_code2(player)
        elif answer=="zxcvbnm":
            self.cheat_code3(player)
        elif answer=="qazmklp":
            self.cheat_code4(player)
        return answer
    def on_exit(self,player):
        if True:
            print("Available exits:")
            for i in self.exits:
                if self.hidden2 is not None:
                    if i().name==self.hidden2().name:
                        if self.needed in player.inv.all:
                            print(i().name)
                        else:
                            continue
                    else:
                        print(i().name)
                else:
                    print(i().name)
            #print("=====================================")
            answer=input("> ")
            for i in self.exits:
                if i().name.lower()==answer.lower():
                    if i==self.hidden2 and self.needed in player.inv.all:
                        self.exit(player,i)
                    elif i==self.hidden2 and self.needed not in player.inv.all:
                        print(f"You don't have the {self.needed().name}!")
                        #print("=====================================")
                    elif i!=self.hidden2:
                        self.exit(player,i)
    def on_trade(self,player):
        if True:
            print("Who would you like to trade with?")
            for i in self.NPCS:
                print(i.name)
            #print("=====================================")
            answer2=input("> ")
            found=False
            for i in self.NPCS:
                if answer2.lower()==i.name.lower() and not found:
                    i.sell(player)
                    found=True
    def on_explore(self,player):
        if True:
            if len(self.items)==0:
                print("There is nothing else to find!")
                #print("=====================================")
                return
            try:
                answer=int(input('How many times?'))
            except ValueError:
                return
            print("You decide to explore.")
            for i in range(answer):
                if random.randint(0,100)!=0:
                    if len(self.items)==0:
                        print("There is nothing else to find!")
                        #print("=====================================")
                        return
                    choice=random.choice(self.items)
                    #print("=====================================")
                    print(f"You found a {choice().name}!")
                    if "Book" in choice().name or "Map" in choice().name:
                        player.inv.books.append(choice)
                    elif "Sword" in choice().name:
                        player.inv.swords.append(choice)
                    elif "Potion" in choice().name:
                        player.inv.potions.append(choice)
                    elif issubclass(choice,items.Food):
                        player.inv.food.append(choice)
                    elif issubclass(choice,items.Other):
                        player.inv.other.append(choice)
                    elif issubclass(choice,items.Armor) or issubclass(choice,Special):
                        player.inv.other.append(choice)
                    player.inv.all.append(choice)
                    self.items.remove(choice)
                else:
                    #print("=====================================")
                    print("You didn't find anything. Maybe try again?...")
    def on_use_item(self,player,answer):
        if True:
            answer2=answer[9:].lower()
            for i in player.inv.all:
                if i().name.lower()==answer2:
                    i().use(self,player)
                    if issubclass(i,items.Potion):
                        player.inv.potions.remove(i)
                        player.inv.all.remove(i)
                    elif issubclass(i,items.Food):
                        player.inv.food.remove(i)
                        player.inv.all.remove(i)
                    print(f"You use the {i().name}.")
                    #print("=====================================")
                    self.storedaction=answer
                    return
    def on_ach(self,player):
        if True:
            answer2=input("What type of achievements? (Killing, Trading, Obtainable, Exploring) > ")
            #print("=====================================")
            if answer2.lower()=="killing":
                answer3=input("What monster? (Zombie, Ogre, Creeper, Bear, Monster, Dragon, All) > ")
                #print("=====================================")
                if answer3.lower()=="zombie":
                    for i in ach.zombies:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.zombies_killed}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                elif answer3.lower()=="ogre":
                    for i in ach.ogres:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.ogres_killed}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                elif answer3.lower()=="creeper":
                    for i in ach.creepers:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.creepers_killed}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                elif answer3.lower()=="bear":
                    for i in ach.bears:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.bears_killed}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                elif answer3.lower()=="monster":
                    for i in ach.monsters:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.monsters_killed}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                elif answer3.lower()=="dragon":
                    for i in ach.dragons:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.dragons_killed}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                elif answer3.lower()=="all":
                    for i in ach.killed:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.killed}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                time.sleep(1)
            elif answer2.lower()=="obtainable":
                for i in ach.obtainable:
                    print(f"""Achievement Name - {i["name"]}""")
                    time.sleep(1)
                    print(f"""Achievement Description - {i["descript"]}""")
                    time.sleep(1)
                    print("Prizes:")
                    prize_dict={}
                    for j in i["prizes"]:
                        if j().name in prize_dict.keys():
                            prize_dict[j().name]+=1
                        elif j().name not in prize_dict.keys():
                            prize_dict[j().name]=1
                    for prize in prize_dict.keys():
                        print(f"{prize} x{prize_dict[prize]}")
                        time.sleep(1)
                    if i["active"]:
                        progress=0
                        for item in player.inv.all:
                            if item().name==i["item"]().name:
                                progress+=1
                        print(f"""Progress: {progress}/{i["amount"]}""")
                    elif not i["active"]:
                        print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                    time.sleep(1)
                    #print("=====================================")
                time.sleep(1)
            elif answer2.lower()=="trading":
                for i in ach.trades:
                    print(f"""Achievement Name - {i["name"]}""")
                    time.sleep(1)
                    print(f"""Achievement Description - {i["descript"]}""")
                    time.sleep(1)
                    print("Prizes:")
                    prize_dict={}
                    for j in i["prizes"]:
                        if j().name in prize_dict.keys():
                            prize_dict[j().name]+=1
                        elif j().name not in prize_dict.keys():
                            prize_dict[j().name]=1
                    for prize in prize_dict.keys():
                        print(f"{prize} x{prize_dict[prize]}")
                        time.sleep(1)
                    if i["active"]:
                        print(f"""Progress: {player.trades}/{i["amount"]}""")
                    elif not i["active"]:
                        print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                    time.sleep(1)
                    #print("=====================================")
                time.sleep(1)
            elif answer2.lower()=="exploring":
                answer3=input("What places? (Houses, Caves, Places) > ")
                #print("=====================================")
                if answer3.lower()=="houses":
                    for i in ach.houses:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.houses}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                    time.sleep(1)
                elif answer3.lower()=="caves":
                    for i in ach.caves:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.caves}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                    time.sleep(1)
                elif answer3.lower()=="places":
                    for i in ach.places:
                        print(f"""Achievement Name - {i["name"]}""")
                        time.sleep(1)
                        print(f"""Achievement Description - {i["descript"]}""")
                        time.sleep(1)
                        print("Prizes:")
                        prize_dict={}
                        for j in i["prizes"]:
                            if j().name in prize_dict.keys():
                                prize_dict[j().name]+=1
                            elif j().name not in prize_dict.keys():
                                prize_dict[j().name]=1
                        for prize in prize_dict.keys():
                            print(f"{prize} x{prize_dict[prize]}")
                            time.sleep(1)
                        if i["active"]:
                            print(f"""Progress: {player.places}/{i["amount"]}""")
                        elif not i["active"]:
                            print(f"""Progress: {i["amount"]}/{i["amount"]}""")
                        time.sleep(1)
                        #print("=====================================")
                    time.sleep(1)
    def on_help(self,player):
        if True:
            print("Available actions:")
            print("exit - exit the current room and choose what room to enter next.")
            #print("=====================================")
            time.sleep(3)
            print("use item [item] - use the [item], if it is in your inventory.")
            #print("=====================================")
            time.sleep(3)
            print("trade - trade with an NPC (you choose which one, Civilians don't trade anything).")
            #print("=====================================")
            time.sleep(3)
            print("explore - explore the room, with a chance of finding an item.")
            #print("=====================================")
            time.sleep(3)
            print("help - read this text.")
            #print("=====================================")
            time.sleep(2)
            print("ach - view achievements, with more optional specifiers.")
            #print("=====================================")
            time.sleep(3)
            print("quests - view your quests.")
            time.sleep(2)
            print("combine - combine materials to make to things.")
            time.sleep(3)
            print("stop playing/stop - stop playing the game, with an option to save your world.")
            time.sleep(3)
            print("Actions are case-insensitive.")
            #print("=====================================")
            time.sleep(2)
    def on_quests(self,player):
        for quest in player.quests:
            print(f"""Quest name - {quest["name"]}""")
            time.sleep(1)
            print(f"""Item needed - {quest["item"]().name} x{quest["amount"]}""")
            time.sleep(1)
            print(f"""Owner - {quest["owner"].name}""")
            time.sleep(1)
    def on_combine(self,player):
        available=[]
        for recipe in r.recipes:
            amount=0
            for i in player.inv.all:
                if i().name==recipe["item"]().name:
                    amount+=1
            if amount>=recipe["amount"]:
                available.append(recipe)
        print("Available recipes:")
        for rec in available:
            print(f'Item - {rec["item"]().name}        Amount needed - {rec["amount"]}        Item gained - {rec["item2"]().name}        Amount gained - {rec["amount2"]}')
        answer2=input("Which one would you like to make? > ")
        answer3=input("How many times would you like to make it? > ")
        for rec in available:
            if rec["item2"]().name.lower()==answer2.lower():
                amount=0
                for item in player.inv.all:
                    if item().name==rec["item"]().name:
                        amount+=1
                amountn=rec["amount"]
                amountcm=0
                while True:
                    amount-=amountn
                    if amount>=0:
                        amountcm+=1
                        if amountcm==int(answer3):
                            break
                    elif amount<0:
                        break
                break
        for rec in available:
            if rec["item2"]().name.lower()==answer2.lower():
                chosen=rec
                break
        try:
            q=chosen
            w=amountcm
        except Exception:
            return
        print(f'You make the {rec["item2"]().name} {amountcm} times.')
        for i in range(amountcm):
            for k in range(chosen["amount"]):
                try:
                    player.inv.all.remove(chosen["item"])
                    i=chosen
                    if issubclass(i["item"],items.Book):
                        player.inv.books.remove(i["item"])
                    elif issubclass(i["item"],items.Potion):
                        player.inv.potions.remove(i["item"])
                    elif issubclass(i["item"],items.Sword):
                        player.inv.swords.remove(i["item"])
                    elif issubclass(i["item"],items.Food) or hasattr(i["item"],"hp"):
                        player.inv.food.remove(i["item"])
                    elif issubclass(i["item"],items.Other) or issubclass(j,Special):
                        player.inv.other.remove(i["item"])
                except Exception:
                    player.inv.all.append(chosen["item2"])
                    j=chosen["item2"]
                    if issubclass(j,items.Book):
                        player.inv.books.append(j)
                    elif issubclass(j,items.Potion):
                        player.inv.potions.append(j)
                    elif issubclass(j,items.Sword):
                        player.inv.swords.append(j)
                    elif issubclass(j,items.Food) or hasattr(j,"hp"):
                        player.inv.food.append(j)
                    elif issubclass(j,items.Other) or issubclass(j,Special):
                        player.inv.other.append(j)
                    return
            for l in range(chosen["amount2"]):
                player.inv.all.append(chosen["item2"])
                j=chosen["item2"]
                if issubclass(j,items.Book):
                    player.inv.books.append(j)
                elif issubclass(j,items.Potion):
                    player.inv.potions.append(j)
                elif issubclass(j,items.Sword):
                    player.inv.swords.append(j)
                elif issubclass(j,items.Food) or hasattr(j,"hp"):
                    player.inv.food.append(j)
                elif issubclass(j,items.Other) or issubclass(j,Special):
                    player.inv.other.append(j)
    def stop(self,player):
        if hasattr(player,"worldname"):
            answer2=input("Save world? (yes/no)")
            if answer2.lower()=="yes":
                import save_load
                with open("worldd.txt") as f:
                    name1=f.readlines()[9].strip('\n')
                with open("worlddd.txt") as f:
                    name2=f.readlines()[9].strip('\n')
                with open("worldddd.txt") as f:
                    name3=f.readlines()[9].strip('\n')
                world=player.worldname
                if world==name1:
                    name="worldd.txt"
                elif world==name2:
                    name="worlddd.txt"
                elif world==name3:
                    name="worldddd.txt"
                else:
                    name="worldd.txt"
                save_load.saveworld(player,name)
        #print("Goodbye :(")
        #raise Exception("Python died from sadness.")
        return "stop"
    def cheat_code(self,player):
        if True:
            player.inv.all.append(items.DeadlySword)
            player.inv.all.append(items.DrainingSword)
            player.inv.all.append(items.DragonSlayer)
            player.inv.all.append(items.Gun)
            player.inv.swords.append(items.DeadlySword)
            player.inv.swords.append(items.DrainingSword)
            player.inv.swords.append(items.DragonSlayer)
            player.inv.swords.append(items.Gun)
            for i in range(5):
                player.inv.all.append(items.StrongHealPotion)
                player.inv.potions.append(items.StrongHealPotion)
                player.inv.all.append(items.StrongHitAllPotion)
                player.inv.potions.append(items.StrongHitAllPotion)
                player.inv.all.append(items.StrongHurtPotion)
                player.inv.potions.append(items.StrongHurtPotion)
            player.inv.all.append(items.LeatherChest)
            player.inv.other.append(items.LeatherChest)
            player.inv.all.append(items.SwordsBook)
            player.inv.books.append(items.SwordsBook)
            player.inv.all.append(items.ApplePie)
            player.inv.food.append(items.ApplePie)
            self.exit(player,Cave10)
    def cheat_code2(self,player):
        #for item in self.items:
            #print(item().name,end=', ')
        #print()
        self.exit(player,Plains7)
        #print("=====================================")
    def cheat_code3(self,player):
        for i in range(10):
            player.inv.all.append(items.Bone)#items.GoldNugget)
            player.inv.all.append(items.HealPotion)#items.Ruby)
            player.inv.other.append(items.Bone)#items.GoldNugget)
            player.inv.potions.append(items.HealPotion)#items.Ruby)
            player.inv.other.append(items.Leather)
            player.inv.all.append(items.Leather)
        self.exit(player,Plains8)#WiseManHut)#JewellerShop)
    def cheat_code4(self,player):
        for i in range(20):
            player.inv.all.append(items.Diamond)
            player.inv.other.append(items.Diamond)
        self.exit(player,Cave13)

class Library(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.BookOfSecrets,items.GoldCoin]
        self.NPCS=[npcs.Librarian(),npcs.Civilian(),npcs.Civilian()]
        self.name="Library"
        self.uuid=self.name
        self.exits=[BlacksmithShop,Hotel,Store]

class BlacksmithShop(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.GoldCoin,items.GoldCoin,items.HurtPotion]
        self.NPCS=[npcs.Blacksmith(),npcs.Civilian()]
        self.exits=[Library,NormalHouse1,Cave1]
        self.name="Blacksmith Shop"
        self.uuid=self.name

class Hotel(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.GoldCoin,items.GoldCoin,items.GoldCoin]
        self.NPCS=[npcs.HotelOwner()]
        self.exits=[Library,HotelRoom,GoldMine,Cave20]
        self.name="Hotel"
        self.uuid=self.name
        self.hidden=True
        self.needed=items.Keycard
        self.hidden2=HotelRoom

class HotelRoom(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.GoldCoin]
        self.NPCS=[npcs.Civilian()]
        self.exits=[Hotel]
        self.name="Hotel Room"
        self.uuid=self.name
        
class NormalHouse1(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.GoldCoin]
        self.NPCS=[npcs.Civilian() for i in range(random.randint(1,3))]
        self.exits=[BlacksmithShop,NormalHouse2,Store]
        self.name="Normal House 1"
        self.uuid=self.name

class NormalHouse2(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.GoldCoin]
        self.NPCS=[npcs.Civilian() for i in range(random.randint(1,3))]
        self.exits=[NormalHouse1,ButcherShop]
        self.name="Normal House 2"
        self.uuid=self.name

class NormalHouse3(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.GoldCoin]
        self.NPCS=[npcs.Civilian() for i in range(random.randint(1,3))]
        self.exits=[GoldMine,ButcherShop]
        self.name="Normal House 3"
        self.uuid=self.name

class GoldMine(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.GoldCoin for i in range(random.randint(6,9))]
        self.NPCS=[npcs.Miner(i+1) for i in range(3)]
        self.exits=[NormalHouse3,Hotel,Store,Cave8]
        self.name="Gold Mine"
        self.uuid=self.name

class ButcherShop(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.GoldCoin]
        self.NPCS=[npcs.Butcher(),npcs.Civilian()]
        self.exits=[NormalHouse2,NormalHouse3,Store]
        self.name="Butcher Shop"
        self.uuid=self.name

class Store(Room):
    def __init__(self):
        super().__init__()
        self.items=[items.GoldCoin,items.Bread]
        self.exits=[GoldMine,Library,ButcherShop,NormalHouse1]
        self.name="Store"
        self.uuid=self.name
        self.NPCS=[npcs.ShopKeeper()]

class Cave(Room):
    def __init__(self):
        super().__init__()
        self.name="Cave"
        self.uuid=self.name
        self.enemies=[]
    def enter(self,player):
        super().enter(player)
        print("Enemies:")
        if len(self.enemies)==0: print("None")
        en_dict={}
        for i in self.enemies:
            if i.name in en_dict.keys():
                en_dict[i.name]+=1
            elif i.name not in en_dict.keys():
                en_dict[i.name]=1
        for enemy in en_dict.keys():
            print(f"{enemy} x{en_dict[enemy]}")
        #print("=====================================")
    def exit(self,player,room_to_enter):
        if self.uuid in player.explored:
            pass
        elif self.uuid not in player.explored:
            player.caves+=1
            player.places+=1
            player.explored.append(self.uuid)
        print(f"You exit the {self.name}.")
        #print("=====================================")
        player.room=room_to_enter()
        player.room.enter(player)
    def loop(self,player):
        self.check_dead(player)
        answer=super().loop(player)
        if answer is None: return ""
        elif answer=="fight":
            self.on_fight(player)
        return answer
    def check_dead(self,player):
        for i in self.enemies:
            if i.hp<=0:
                print(i.name+" died!")
                self.enemies.remove(i)
                exec("player."+i.name.lower()+"s_killed+=1")
                player.killed+=1
    def on_help(self,player):
        super().on_help(player)
        if True:
            print("fight - fight an enemy (you choose which one).")
            time.sleep(2)
            print("fight can only be used in Caves.")
            #print("=====================================")
            time.sleep(1)
    def on_fight(self,player):
        if True:
            #print("=====================================")
            print("Enemies you can fight:")
            for i in self.enemies:
                print("Name - "+i.name+"    HP - "+str(i.hp))
            #print("=====================================")
            answer2=input("> ")
            for i in self.enemies:
                if i.name.lower()==answer2.lower():
                    i.fight(self,player)
                    return
            #print("=====================================")

class Cave1(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 1"
        self.uuid=self.name
        self.enemies=[en.Bear()]
        self.exits=[BlacksmithShop,Cave2]
        self.items=[items.GoldCoin]

class Cave2(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 2"
        self.uuid=self.name
        self.enemies=[en.Ogre()]
        self.exits=[Cave1,Cave3]
        self.items=[items.GoldCoin,items.Bone]

class Cave3(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 3"
        self.uuid=self.name
        self.enemies=[en.Zombie()]
        self.exits=[Cave2,Cave4,Cave5]
        self.items=[items.Bone,items.Bone]

class Cave4(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 4"
        self.uuid=self.name
        self.enemies=[en.Zombie(),en.Ogre()]
        self.exits=[Cave3,Cave6]
        self.items=[items.Bone,items.Bone,items.Bone,items.DrainingSword]

class Cave5(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 5"
        self.uuid=self.name
        self.enemies=[en.Zombie() for i in range(2)]
        self.exits=[Cave3,TreasureRoom]
        self.hidden=True
        self.needed=items.TreasureMap
        self.hidden2=TreasureRoom
        self.items=[items.GoldCoin,items.Bone,items.Bone,items.Bone]

class TreasureRoom(Cave):
    def __init__(self):
        super().__init__()
        self.name="Treasure Room"
        self.uuid=self.name
        self.exits=[Cave5]
        self.items=[items.GoldCoin for i in range(random.randint(2,4))]+[items.Bone,items.Bone]
    def enter(self,player):
        super().enter(player)
        j=random.randint(16,23)
        for i in range(j):
            player.gold.append(items.GoldCoin)
        print(f"The treasure room had {str(j)} Gold!")
        #print("=====================================")

class Cave6(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 6"
        self.uuid=self.name
        self.enemies=[en.Creeper(),en.Zombie(),en.Ogre()]
        self.exits=[Cave4,Cave7,Cave17]
        self.items=[items.Bone for i in range(5)]

class Cave7(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 7"
        self.uuid=self.name
        self.enemies=[en.Zombie(),en.Zombie(),en.Ogre(),en.Ogre()]
        self.exits=[Cave6,Cave8,Cave13]
        self.items=[items.RottenMeat,items.Bone,items.Bone]

class Cave8(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 8"
        self.uuid=self.name
        self.enemies=[en.Zombie(),en.Zombie(),en.Zombie(),en.Monster()]
        self.exits=[Cave7,Cave9,GoldMine]
        self.items=[items.GoldCoin for i in range(3)]+[items.Bone for i in range(4)]+[items.Gunpowder]

class Cave9(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 9"
        self.uuid=self.name
        self.enemies=[en.Monster(),en.Monster(),en.Creeper(),en.Creeper(),en.Dragon()]
        self.exits=[Cave8,Cave3,Cave10,Plains10]
        self.items=[items.DeadlySword,items.Bone,items.Bone,items.Gunpowder,items.Gunpowder]

class Cave10(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 10"
        self.uuid=self.name
        self.enemies=[en.Dragon(),en.Dragon(),en.Creeper(),en.Creeper(),en.Creeper(),en.Monster()]+[en.Zombie() for i in range(6)]
        self.exits=[Cave9,GoldMine2]
        self.items=[items.Bone for i in range(random.randint(7,23))]+[items.Gunpowder for i in range(3)]

class GoldMine2(Room):
    def __init__(self):
        super().__init__()
        self.name="Gold Mine 2"
        self.uuid=self.name
        self.exits=[Cave10,JewellerShop,Store2,School]
        self.items=[items.GoldCoin for i in range(random.randint(5,10))]
        self.NPCS=[npcs.Miner2(1),npcs.Miner2(2)]

class JewellerShop(Room):
    def __init__(self):
        super().__init__()
        self.name="Jeweller Shop"
        self.uuid=self.name
        self.exits=[GoldMine2,NormalHouse12,NormalHouse22,AlchemistShop]
        self.items=[items.GoldCoin,items.Ruby]
        self.NPCS=[npcs.Jeweller(),npcs.Civilian(),npcs.Civilian()]

class NormalHouse12(Room):
    def __init__(self):
        super().__init__()
        self.name="Normal House 1 2"
        self.uuid=self.name
        self.exits=[JewellerShop,Store2,Library2,FlowerShop]
        self.items=[items.GoldCoin,items.GoldCoin]
        self.NPCS=[npcs.Civilian() for i in range(random.randint(2,4))]

class NormalHouse22(Room):
    def __init__(self):
        super().__init__()
        self.name="Normal House 2 2"
        self.uuid=self.name
        self.exits=[JewellerShop,NormalHouse32,School]
        self.items=[items.GoldCoin,items.GoldCoin]
        self.NPCS=[npcs.Civilian() for i in range(random.randint(2,4))]

class Store2(Room):
    def __init__(self):
        super().__init__()
        self.name="Store 2"
        self.uuid=self.name
        self.exits=[NormalHouse12,GoldMine2,Tannery]
        self.items=[items.Tomato,items.Beef]
        self.NPCS=[npcs.StoreKeeper(),npcs.Civilian(),npcs.Civilian()]

class Tannery(Room):
    def __init__(self):
        super().__init__()
        self.name="Tannery"
        self.uuid=self.name
        self.exits=[Store2,FlowerShop]
        self.items=[items.Leather for i in range(2)]
        self.NPCS=[npcs.LeatherWorker(),npcs.Civilian()]

class Library2(Room):
    def __init__(self):
        super().__init__()
        self.name="Library 2"
        self.uuid=self.name
        self.exits=[NormalHouse12,AlchemistShop,Plains1,NormalHouse4]
        self.items=[items.GoldCoin,items.SwordsBook]
        self.NPCS=[npcs.Librarian2(),npcs.Civilian()]

class NormalHouse32(Room):
    def __init__(self):
        super().__init__()
        self.name="Normal House 3 2"
        self.uuid=self.name
        self.exits=[NormalHouse22,AlchemistShop]
        self.items=[items.GoldCoin for i in range(2)]
        self.NPCS=[npcs.Civilian() for i in range(random.randint(2,5))]

class School(Room):
    def __init__(self):
        super().__init__()
        self.name="School"
        self.uuid=self.name
        self.exits=[GoldMine2,NormalHouse22,Cave11]
        self.items=[items.GoldCoin]
        self.NPCS=[npcs.Teacher()]

class AlchemistShop(Room):
    def __init__(self):
        super().__init__()
        self.name="Alchemist Shop"
        self.uuid=self.name
        self.exits=[Library2,JewellerShop,NormalHouse32]
        self.items=[items.HealPotion,items.HurtPotion]
        self.NPCS=[npcs.Alchemist(),npcs.Civilian()]

class FlowerShop(Room):
    def __init__(self):
        super().__init__()
        self.name="Flower Shop"
        self.uuid=self.name
        self.exits=[Tannery,NormalHouse12,NormalHouse4]
        self.items=[items.GoldCoin]
        self.NPCS=[npcs.Florist(),npcs.Civilian()]

class NormalHouse4(Room):
    def __init__(self):
        super().__init__()
        self.name="Normal House 4"
        self.uuid=self.name
        self.exits=[Library2,FlowerShop]
        self.items=[items.GoldCoin for i in range(3)]
        self.NPCS=[npcs.Civilian() for i in range(random.randint(3,7))]

class School2(Room):
    def __init__(self):
        super().__init__()
        self.name="School 2"
        self.uuid=self.name
        self.exits=[Plains10,NormalHouse13,Store3]
        self.items=[items.Bread,items.Carrot]
        self.NPCS=[npcs.Teacher2()]

class NormalHouse13(Room):
    def __init__(self):
        super().__init__()
        self.name="Normal House 1 3"
        self.uuid=self.name
        self.exits=[School2,AlchemistShop2,FlowerShop2]
        self.items=[items.GoldCoin for i in range(5)]
        self.NPCS=[npcs.Civilian() for i in range(6)]

class Store3(Room):
    def __init__(self):
        super().__init__()
        self.name="Store 3"
        self.uuid=self.name
        self.exits=[School2,AlchemistShop2,NormalHouse33]
        self.items=[items.ApplePie,items.Honeycomb]
        self.NPCS=[npcs.Civilian(),npcs.Storekeeper()]

class AlchemistShop2(Room):
    def __init__(self):
        super().__init__()
        self.name="Alchemist Shop 2"
        self.uuid=self.name
        self.exits=[NormalHouse13,Store3]
        self.items=[items.HitAllPotion,items.StrongHealPotion]
        self.NPCS=[npcs.Alchemist2()]

class FlowerShop2(Room):
    def __init__(self):
        super().__init__()
        self.name="Flower Shop 2"
        self.uuid=self.name
        self.exits=[NormalHouse13,NormalHouse23]
        self.items=[items.GoldCoin for i in range(5)]
        self.NPCS=[npcs.Civilian(),npcs.Florist2()]

class NormalHouse23(Room):
    def __init__(self):
        super().__init__()
        self.name="Normal House 2 3"
        self.uuid=self.name
        self.exits=[FlowerShop2,Hotel2]
        self.items=[items.GoldCoin for i in range(random.randint(3,10))]
        self.NPCS=[npcs.Civilian() for i in range(4)]

class NormalHouse33(Room):
    def __init__(self):
        super().__init__()
        self.name="Normal House 3 3"
        self.uuid=self.name
        self.exits=[Store3,Tannery2,Cave18]
        self.items=NormalHouse23().items
        self.NPCS=NormalHouse23().NPCS+[npcs.Civilian()]

class Tannery2(Room):
    def __init__(self):
        super().__init__()
        self.name="Tannery 2"
        self.uuid=self.name
        self.exits=[NormalHouse33,Hotel2]
        self.items=[items.Leather,items.Leather]
        self.NPCS=[npcs.Tanner()]

class Hotel2(Room):
    def __init__(self):
        super().__init__()
        self.name="Hotel 2"
        self.uuid=self.name
        self.exits=[Tannery2,NormalHouse23]
        self.items=[items.GoldCoin,items.GoldCoin]
        self.NPCS=[npcs.HotelOwner(),npcs.Civilian()]
        self.hidden=True
        self.needed=items.Keycard
        self.hidden2=HotelRoom

class Plains(Room):
    def __init__(self):
        super().__init__()
        self.name="Plains"
        self.uuid=self.name
        self.animals=[]
        self.plants=[]
        self.collect=[]
    def on_help(self,player):
        super().on_help(player)
        print("hunt - hunt an animal")
        time.sleep(2)
        print("harvest - harvest food from plants")
        time.sleep(2)
        print("take [plant] - take the plant")
        time.sleep(2)
        print("plant [plant] - plant the plant,if it is in your inventory")
        time.sleep(3)
        print("hunt, harvest, take, and plant can only be used in Plains.")
        time.sleep(1)
    def loop(self,player):
        self.check_dead(player)
        self.grow_plants()
        answer=super().loop(player)
        if answer is None: return ""
        elif answer=="hunt":
            self.on_hunt(player)
        elif answer=="harvest":
            self.on_harvest(player)
        elif answer.startswith("take"):
            self.on_take(player,answer[5:].lower())
        elif answer.startswith("plant"):
            self.on_plant(player,answer[6:].lower())
        return answer
    def enter(self,player):
        super().enter(player)
        print("Animals:")
        if len(self.animals)==0: print("None")
        an_dict={}
        for i in self.animals:
            if i.name in an_dict.keys():
                an_dict[i.name]+=1
            elif i.name not in an_dict.keys():
                an_dict[i.name]=1
        for animal in an_dict.keys():
            print(f"{animal} x{an_dict[animal]}")
        #print("=====================================")
        print("Plants:")
        if len(self.plants)==0: print("None")
        pl_dict={}
        for i in self.plants:
            if i.name in pl_dict.keys():
                pl_dict[i.name]+=1
            elif i.name not in pl_dict.keys():
                pl_dict[i.name]=1
        for plant in pl_dict.keys():
            print(f"{plant} x{pl_dict[plant]}")
    def exit(self,player,room_to_enter):
        if self.uuid in player.explored:
            pass
        elif self.uuid not in player.explored:
            player.plains+=1
            player.places+=1
            player.explored.append(self.uuid)
        print(f"You exit the {self.name}.")
        #print("=====================================")
        player.room=room_to_enter()
        player.room.enter(player)
    def on_take(self,player,pl_name):
        answer=input('How many would you like to take? > ')
        if answer=='*':
            took=0
            to_remove=[]
            for plant in self.plants:
                if plant.name.lower()==pl_name:
                    plant.take(player,self)
                    player.plants.append(plant)
                    to_remove.append(plant)
                    took+=1
            for i in to_remove:
                self.plants.remove(i)
            print(f'You took {took} {pl_name}s!')
        else:
            try:
                answer=int(answer)
            except Exception:
                return
            took=0
            to_remove=[]
            for plant in self.plants:
                if plant.name.lower()==pl_name:
                    plant.take(player,self)
                    player.plants.append(plant)
                    took+=1
                    to_remove.append(plant)
                    if took>=answer:
                        break
            for i in to_remove:
                self.plants.remove(i)
            print(f'You took {took} {pl_name}s!')
    def on_plant(self,player,pl_name):
        for plant in player.plants:
            if plant.name.lower()==pl_name:
                plant.plant(player,self)
                print(f"You planted the {plant.name}!")
                return
    def check_dead(self,player):
        for i in self.animals:
            if i.hp<=0:
                print(i.name+" died!")
                self.animals.remove(i)
                for j in i.drops:
                    player.inv.all.append(j)
                    if issubclass(j,items.Book):
                        player.inv.books.append(j)
                    elif issubclass(j,items.Potion):
                        player.inv.potions.append(j)
                    elif issubclass(j,items.Sword):
                        player.inv.swords.append(j)
                    elif issubclass(j,items.Food) or hasattr(j,"hp"):
                        player.inv.food.append(j)
                    elif issubclass(j,items.Other):
                        player.inv.other.append(j)
                exec("player."+i.name.lower()+"s_killed+=1")
                player.animals_killed+=1
    def grow_plants(self):
        pollinate_chance=20
        for animal in self.animals:
            if "bee" in animal.name:
                pollinate_chance-=animal.decrease
        if pollinate_chance<=0:
            pollinate_chance=0
        for plant in self.plants:
            plant.grow(self,pollinate_chance+random.randint(0,4))
    def on_hunt(self,player):
        if True:
            #print("=====================================")
            print("Animals you can hunt:")
            for i in self.animals:
                print("Name - "+i.name+"    HP - "+str(i.hp))
            #print("=====================================")
            answer2=input("> ")
            for i in self.animals:
                if i.name.lower()==answer2.lower():
                    i.hunt(player)
                    return
            #print("=====================================")
    def on_harvest(self,player):
        if len(self.collect)>0:
            for item in self.collect:
                player.inv.all.append(item)
                if issubclass(item,items.Food) or hasattr(item,"hp"):
                    player.inv.food.append(item)
                elif issubclass(item,items.Other):
                    player.inv.other.append(item)
            print("You harvested:")
            pl_dict={}
            for i in self.collect:
                if i().name in pl_dict.keys():
                    pl_dict[i().name]+=1
                elif i().name not in pl_dict.keys():
                    pl_dict[i().name]=1
            for plant in pl_dict.keys():
                print(f"{plant} x{pl_dict[plant]}")
            self.collect=[]
        else:
            print("There is nothing to harvest!")

class Plains1(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 1"
        self.uuid=self.name
        self.items=[items.Beef]+[items.Grass for i in range(random.randint(3,5))]
        self.exits=[Library2,Plains2]
        self.animals=[an.Cow()]

class Plains2(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 2"
        self.uuid=self.name
        self.items=[items.Grass for i in range(6)]+[items.Wool,items.Beef]
        self.exits=[Plains1,Plains3,Plains7]
        self.animals=[an.Cow(),an.Cow(),an.Sheep()]

class Plains3(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 3"
        self.uuid=self.name
        self.items=[items.Grass for i in range(random.randint(7,13))]+[items.Mutton,items.Beef,items.Beef,items.Chicken]
        self.exits=[Plains2,Plains4]
        self.animals=[an.Cow(),an.Cow(),an.Cow(),an.Sheep(),an.Sheep(),an.Chicken()]

class Plains4(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 4"
        self.uuid=self.name
        self.items=[items.Grass for i in range(random.randint(17,21))]+[items.Pork,items.Pork,items.Wool,items.Leather,items.Beef,items.Feather]
        self.exits=[Plains3,Plains5]
        self.animals=[an.Cow() for i in range(5)]+[an.Sheep() for i in range(3)]+[an.Chicken(),an.Chicken(),an.Pig(),an.Pig(),an.Pig()]
        self.plants=[p.TomatoPlant()]

class Plains5(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 5"
        self.uuid=self.name
        self.items=[items.Grass for i in range(random.randint(8,29))]+[items.Pork,items.Pork,items.Leather,items.Leather,items.Leather,items.Feather,items.Feather,items.Beef]
        self.exits=[Plains4,Cave12,Plains6]
        self.animals=[an.Cow() for i in range(5)]+[an.Sheep() for i in range(4)]+[an.Chicken() for i in range(4)]+[an.Pig() for i in range(4)]
        self.plants=[p.TomatoPlant(),p.TomatoPlant(),p.WheatStalk()]

class Plains6(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 6"
        self.uuid=self.name
        self.items=[items.Berry,items.Tomato,items.Tomato,items.Wheat,items.Pork,items.Pork,items.Feather,items.Mutton,items.Leather,items.Leather,items.Beef,items.Chicken]+[items.Grass for i in range(random.randint(17,32))]
        self.exits=[Plains5,Plains7]
        self.animals=[an.Cow() for i in range(6)]+[an.Sheep() for i in range(5)]+[an.Chicken() for i in range(5)]+[an.Pig() for i in range(6)]
        self.plants=[p.TomatoPlant() for i in range(3)]+[p.WheatStalk(),p.WheatStalk(),p.BerryBush()]

class Plains7(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 7"
        self.uuid=self.name
        self.items=Plains6().items+[items.Berry,items.Wheat,items.Tomato,items.Beef,items.Leather]
        self.animals=Plains6().animals+[an.Cow(),an.Sheep(),an.Pig(),an.Chicken()]
        self.plants=[p.TomatoPlant() for i in range(4)]+[p.WheatStalk() for i in range(3)]+[p.BerryBush() for i in range(3)]
        self.exits=[Plains6,Plains2,Plains8]

class Plains8(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 8"
        self.uuid=self.name
        self.items=Plains7().items+[items.Apple,items.Apple]
        self.animals=Plains7().animals+[an.Bumblebee(),an.Bumblebee()]
        self.plants=Plains7().plants+[p.TomatoPlant(),p.AppleTree(),p.Beehive()]
        self.exits=[Plains7,Plains9]

class Plains9(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 9"
        self.uuid=self.name
        self.items=Plains8().items
        self.animals=Plains8().animals+[an.Bumblebee(),an.Honeybee(),an.Honeybee()]
        self.plants=Plains8().plants+[p.Beehive(),p.OrangeTree()]
        self.exits=[Plains8,Plains10]

class Plains10(Plains):
    def __init__(self):
        super().__init__()
        self.name="Plains 10"
        self.uuid=self.name
        self.items=Plains9().items+[items.Apple,items.Beef]
        self.animals=Plains9().animals+[an.Bumblebee(),an.Honeybee(),an.Pig()]
        self.plants=Plains9().plants+[p.AppleTree(),p.TomatoPlant(),p.Beehive(),p.OrangeTree()]
        self.exits=[Plains9,Cave9,School2]

class Cave11(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 11"
        self.uuid=self.name
        self.items=[items.Bone for i in range(random.randint(3,5))]+[items.GoldCoin,items.Iron]
        self.exits=[School,Cave12]
        self.enemies=[en.Zombie() for i in range(3)]

class Cave12(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 12"
        self.uuid=self.name
        self.items=[items.Bone for i in range(random.randint(7,12))]+[items.Iron,items.Iron,items.Iron,items.Diamond,items.RottenMeat,items.RottenMeat]
        self.exits=[Cave11,Cave13,Plains5]
        self.enemies=[en.Zombie(),en.Zombie(),en.Zombie(),en.Zombie(),en.Ogre(),en.Ogre(),en.Creeper()]

class Cave13(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 13"
        self.uuid=self.name
        self.items=[items.Bone for i in range(4)]+[items.RottenMeat for i in range(5)]+[items.Iron for i in range(random.randint(3,6))]+[items.Diamond,items.Diamond]
        self.exits=[Cave12,Cave14,Cave7]
        self.enemies=[en.Zombie() for i in range(7)]+[en.Creeper(),en.Creeper(),en.Dragon()]

class DeepCave(Cave):
    def __init__(self):
        super().__init__()
        self.name="Deep Cave"
        self.uuid=self.name
        self.st_chance=1
    def loop(self,player):
        answer=super().loop(player)
        if random.randint(0,self.st_chance)==0:
            print('You were hit by a stalactite!')
            player.hp0-=random.choice([1,1.25,1.5,1.75,2])
        return answer

class Cave14(DeepCave):
    def __init__(self):
        super().__init__()
        self.name="Cave 14"
        self.uuid=self.name
        self.items=Cave13().items+[items.Iron,items.Iron,items.Diamond,items.Diamond]
        self.exits=[Cave13,Cave15]
        self.enemies=Cave13().enemies+[en.Dragon(),en.Creeper(),en.Monster()]
        self.st_chance=4

class Cave15(DeepCave):
    def __init__(self):
        super().__init__()
        self.name="Cave 15"
        self.uuid=self.name
        self.items=Cave14().items+[items.Diamond]
        self.exits=[Cave14,Cave16]
        self.enemies=[en.Zombie(),en.Zombie(),en.Creeper(),en.Dragon()]
        self.st_chance=2

class Cave16(DeepCave):
    def __init__(self):
        super().__init__()
        self.name="Cave 16"
        self.uuid=self.name
        self.items=[items.Diamond,items.Diamond,items.Diamond,items.Iron,items.Iron,items.LavaBucket,items.Sack]
        self.exits=[Cave15,Cave17]
        self.enemies=[en.Zombie(),en.Creeper()]
        self.st_chance=2

class Cave17(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 17"
        self.uuid=self.name
        self.items=[items.Diamond,items.Diamond,items.Diamond,items.Iron,items.Iron,items.LavaBucket]
        self.exits=[Cave16,Cave6,Cave18]
        self.enemies=Cave16().enemies

class Cave18(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 18"
        self.uuid=self.name
        self.items=[items.Iron,items.Iron]
        self.exits=[Cave17,NormalHouse33,Cave19]
        self.enemies=[en.Bear()]

class Cave19(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 19"
        self.uuid=self.name
        self.items=[items.GoldCoin]
        self.exits=[Cave18,Cave20]
        self.enemies=[en.Zombie()]

class Cave20(Cave):
    def __init__(self):
        super().__init__()
        self.name="Cave 20"
        self.uuid=self.name
        self.items=[items.GoldCoin]
        self.exits=[Cave19,Hotel]
        self.enemies=[en.Bear()]
