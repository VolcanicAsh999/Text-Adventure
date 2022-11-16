import player as p
import plants
import os
import time

def clrscr():
    print('\n' * 10)

class SadnessError(Exception):
    pass

def load_world():
    with open("worldd.txt") as f:
        name1=f.readlines()[9].strip('\n')
    with open("worlddd.txt") as f:
        name2=f.readlines()[9].strip('\n')
    with open("worldddd.txt") as f:
        name3=f.readlines()[9].strip('\n')
    answer=input(f"Which world? ({name1}, {name2}, {name3}) > ").lower()
    if answer==name1.lower():
        world="worldd.txt"
    elif answer==name2.lower():
        world="worlddd.txt"
    elif answer==name3.lower():
        world="worldddd.txt"
    else:
        world="worldd.txt"
    return world

def rename_world(world):
    clrscr()
    answer3=input("What would you like to rename it? > ")
    with open(world,mode='r') as file:
        lines=file.readlines()
    with open(world,mode='w') as file2:
        file2.writelines([lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7],lines[8],answer3,lines[10],lines[11],lines[12]])
    return

def revert_world(world):
    clrscr()
    if world=="worldd.txt":
        world_name="New World 1\n"
    elif world=="worlddd.txt":
        world_name="New World 2\n"
    elif world=="worldddd.txt":
        world_name="New World 3\n"
    with open(world,mode='w') as file:
        file.writelines(['Library\n','[]\n',"['HealPotion()']\n",'[0,0,0,0,0,0,0,0,0,0,0,0,0]\n','20\n','0\n','10\n','0\n',"['Library']\n",world_name,'[]\n','[]\n','[]\n'])
        
def edit_world():
    clrscr()
    with open("worldd.txt") as f:
        name1=f.readlines()[9].strip('\n')
    with open("worlddd.txt") as f:
        name2=f.readlines()[9].strip('\n')
    with open("worldddd.txt") as f:
        name3=f.readlines()[9].strip('\n')
    answer=input(f"Which world? ({name1}, {name2}, {name3}) > ").lower()
    if answer==name1.lower():
        world="worldd.txt"
    elif answer==name2.lower():
        world="worlddd.txt"
    elif answer==name3.lower():
        world="worldddd.txt"
    else:
        return
    while True:
        answer2=input("What would you like to do? (Rename, Revert, Cancel) > ").lower()
        if answer2=="rename":
            rename_world(world)
            continue
        elif answer2=="revert":
            revert_world(world)
            continue
        elif answer2=="cancel":
            break
    return

def main_menu():
    clrscr()
    b=False
    while not b:
        print("============== Main Menu ==============")
        answer=input("New World, Load World, Edit World, Quit > ").lower()
        if answer=="new world" or answer=="new":
            clrscr()
            player=p.Player("new")
            b=True
        elif answer=="load world" or answer=="load":
            clrscr()
            world_type=load_world()
            player=p.Player(world_type)
            b=True
        elif answer=="edit world" or answer=="edit":
            edit_world()
        elif answer=="quit":
            clrscr()
            answer2=input("Are you sure you want to quit? > ")
            if answer2.lower()=="yes":
                print("Goodbye :(")
                raise SadnessError("Python died from sadness.")
            else:
                continue
        else:
            continue
    return player

def play_game():
    player=main_menu()
    playing=True
    while playing:
        try:
            clrscr()
            playing=player.loop()
            if playing==False:
                return
            time.sleep(1)
        except Exception as e:
            clrscr()
            print('Error')
            print(e)
            print('Auto-saving world')
            import save_load
            with open('worldd.txt') as f:
                name1=f.readlines()[9].strip('\n')
            with open('worlddd.txt') as f:
                name2=f.readlines()[9].strip('\n')
            with open('worldddd.txt') as f:
                name3=f.readlines()[9].strip('\n')
            world=player.worldname
            if world==name1:
                name='worldd.txt'
            elif world==name2:
                name='worlddd.txt'
            elif world==name3:
                name='worldddd.txt'
            save_load.saveworld(player,name)
            return
    return

while True:
    clrscr()
    play_game()
