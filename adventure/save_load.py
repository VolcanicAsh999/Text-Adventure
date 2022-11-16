import achievements
import achievements as ach
from rooms import *
import items
from items import *
import plants
from plants import *
import NPCS as npc

def load_items(player,items_to_load):
    #print(items_to_load)
    player.inv.all.clear()
    player.inv.potions.clear()
    player.inv.swords.clear()
    player.inv.books.clear()
    player.inv.food.clear()
    player.inv.other.clear()
    for item in items_to_load:
        #print(item)
        exec("player.inv.all.append(type("+item+"))")
        typ=None
        exec("if issubclass(type("+item+"),items.Book): typ='book'")
        exec("if issubclass(type("+item+"),items.Sword): typ='sword'")
        exec("if issubclass(type("+item+"),items.Potion): typ='potion'")
        exec("if issubclass(type("+item+"),items.Armor): typ='armor'")
        exec("if issubclass(type("+item+"),items.Food): typ='food'")
        exec("if issubclass(type("+item+"),items.Other) or issubclass(type("+item+"),items.Special): typ='other'")
        if typ=='book':
            exec("player.inv.books.append(type("+item+"))")
        elif typ=='sword':
            exec("player.inv.swords.append(type("+item+"))")
        elif typ=='food':
            exec("player.inv.food.append(type("+item+"))")
        elif typ=='potion':
            exec("player.inv.potions.append(type("+item+"))")
        elif typ=='armor':
            exec("player.inv.other.append(type("+item+"))")
        elif typ=='other':
            exec("player.inv.other.append(type("+item+"))")

def load_sack(sack_items):
    for item in sack_items:
        exec("items.items.append(type("+item+"))")

def load_ach(player,achs_names):
    for achieve in ach.all_ach:
        for ach_name in achs_names:
            if ach_name==achieve["name"]:
                a=achieve
                a["active"]=False
                player.ach_got.append(a)
                break

def load_quests(player,quests_names):
    for quest in npc.Teacher().sales+npc.Teacher2().sales:
        for name in quests_names:
            if name==quest["name"]:
                player.quests.append(quest)
                break

def load_plants(player,plants):
    player.plants=[]
    for plant in plants:
        exec("player.plants.append("+plant+")")

def loadworld(player,worldname):
    with open(worldname,mode='r') as file:
        world=file.readlines()
    exec("player.room="+world[0].strip('\n').replace(" ","")+"()")
    exec("player.explored="+world[8].strip('\n'))
    exec("player.trades="+world[7].strip('\n'))
    exec("player.deathtimes="+world[5].strip('\n'))
    exec("load_ach(player,"+world[1].strip('\n')+")")
    exec("player.gold=[items.GoldCoin for j in range("+world[4].strip('\n')+")]")
    exec("player.hp0="+world[6].strip('\n'))
    exec("load_items(player,"+world[2].strip('\n')+")")
    try:
        exec("load_plants(player,"+world[10].strip('\n')+")")
    except IndexError:
        player.plants=[]
    try:
        exec("load_sack("+world[11].strip('\n')+")")
    except IndexError:
        pass
    try:
        exec("load_quests(player,"+world[12].strip('\n')+")")
    except IndexError:
        pass
    exec("""
killed="""+world[3].strip('\n')+"""
if True:
    player.zombies_killed=killed[0]
    player.ogres_killed=killed[1]
    player.dragons_killed=killed[2]
    player.monsters_killed=killed[3]
    player.bears_killed=killed[4]
    player.creepers_killed=killed[5]
    player.cows_killed=killed[6]
    player.sheeps_killed=killed[7]
    player.pigs_killed=killed[8]
    player.chickens_killed=killed[9]
    player.plains=killed[10]
    player.houses=killed[11]
    player.caves=killed[12]
""")
    player.worldname=world[9].strip('\n')
    print("Succesfully loaded the world "+world[9].strip('\n')+"!")

def saveworld(player,worldname):
    with open(worldname,mode='w') as file:
        room=player.room.name+"\n"
        explore=str(player.explored)+"\n"
        tradetimes=str(player.trades)+"\n"
        death=str(player.deathtimes)+"\n"
        ach_gotten=[]
        for a in player.ach_got:
            if a["active"]==False:
                ach_gotten.append(a["name"])
        quests=[]
        for q in player.quests:
            quests.append(q["name"])
        quests=str(quests)+"\n"
        ach_gotten=str(ach_gotten)+"\n"
        gold=str(len(player.gold))+"\n"
        health=str(player.hp0)+"\n"
        inventory=[]
        for item in player.inv.all:
            inventory.append(item().name.replace(" ","")+"()")
        plants=[]
        for plant in player.plants:
            plants.append(plant.name.replace(" ","")+"()")
        inventory=str(inventory)+"\n"
        plants=str(plants)+"\n"
        killed=[player.zombies_killed]
        killed.append(player.ogres_killed)
        killed.append(player.dragons_killed)
        killed.append(player.monsters_killed)
        killed.append(player.bears_killed)
        killed.append(player.creepers_killed)
        killed.append(player.cows_killed)
        killed.append(player.sheeps_killed)
        killed.append(player.pigs_killed)
        killed.append(player.chickens_killed)
        killed.append(player.plains)
        killed.append(player.houses)
        killed.append(player.caves)
        killed=str(killed)+"\n"
        item=[]
        for i in items.items:
            item.append(i().name.replace(" ","")+"()")
        item=str(item)+"\n"
        answer=input("Change World Name? (y/n) > ")
        if answer=='y':
            name=input("Save name > ")+'\n'
        else:
            name=player.worldname+'\n'
        file.writelines([room,ach_gotten,inventory,killed,gold,death,health,tradetimes,explore,name,plants,item,quests])
