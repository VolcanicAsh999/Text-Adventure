import items

zombies=[{"active":True,"amount":1,"name":"Zombie Killer","descript":"Kill a Zombie","prizes":[items.GoldCoin,items.GoldCoin]},{"active":True,"amount":5,"name":"Zombie Destroyer","descript":"Kill 5 Zombies","prizes":[items.HealingSword]},{"active":True,"amount":10,"name":"Zombie Hunter","descript":"Kill 10 Zombies","prizes":[items.RottenMeat for i in range(10)]}] 

ogres=[{"active":True,"amount":1,"name":"Ogre Killer","descript":"Kill a Ogre","prizes":[items.HealPotion]},{"active":True,"amount":5,"name":"Ogre Destroyer","descript":"Kill 5 Ogres","prizes":[items.StrongHealPotion]},{"active":True,"amount":10,"name":"Ogre Hunter","descript":"Kill 10 Ogres","prizes":[items.StrongHurtPotion for i in range(5)]+[items.StrongHealPotion for i in range(3)]}]

creepers=[{"active":True,"amount":1,"name":"Creeper Killer","descript":"Kill a Creeper","prizes":[items.HurtPotion]},{"active":True,"amount":5,"name":"Creeper Destroyer","descript":"Kill 5 Creepers","prizes":[items.Gunpowder,items.Gunpowder,items.Bone]},{"active":True,"amount":10,"descript":"Kill 10 Creepers","name":"Creeper Hunter","prizes":[items.Gunpowder for i in range(6)]}]

bears=[{"active":True,"amount":1,"name":"Bear Killer","descript":"Kill a Bear","prizes":[items.GoldCoin]}]

dragons=[{"active":True,"amount":1,"name":"Dragon Killer","descript":"Kill a Dragon","prizes":[items.DragonSlayer]},{"active":True,"amount":5,"name":"Dragon Destroyer","descript":"Kill 5 Dragons","prizes":[items.LavaBucket,items.LavaBucket,items.LavaBucket,items.StrongHealPotion]}]

monsters=[{"active":True,"amount":1,"name":"Monster Killer","descript":"Kill a Monster","prizes":[items.Chicken,items.Bone]},{"active":True,"amount":5,"name":"Monster Destroyer","descript":"Kill 5 Monsters","prizes":[items.Bone,items.Bone,items.StrongHurtPotion]}]

killed=[{"active":True,"amount":5,"name":"Enemy Killer","descript":"Kill 5 Enemies","prizes":[items.DrainingSword]}]

obtainable=[{"active":True,"item":items.TreasureMap,"amount":1,"name":"Treasure Hunter","descript":"Obtain a Treasure Map","prizes":[items.GoldCoin,items.GoldCoin]},{"active":True,"item":items.Gunpowder,"amount":10,"name":"Gunpowder Collector","descript":"Obtain 10 Gunpowder","prizes":[items.Gun]},{"active":True,"amount":30,"item":items.Bone,"name":"Dinosaur Excavator","descript":"Collect 30 Bones","prizes":[items.LavaBucket]}]

trades=[{"active":True,"amount":1,"name":"What a Deal!","descript":"Trade with an NPC","prizes":[items.GoldCoin,items.GoldCoin]},{"active":True,"amount":5,"name":"Miniature Store","descript":"Trade with 5 NPCS","prizes":[items.Beef,items.HealPotion]},{"active":True,"amount":10,"name":"Master Trader","descript":"Trade with 10 NPCS","prizes":[items.DeadlySword,items.GoldCoin]}]

houses=[{"active":True,"amount":5,"name":"Village Explorer","descript":"Enter 5 different village buildings","prizes":[items.GoldCoin,items.GoldCoin,items.Chicken]},{"active":True,"amount":10,"name":"Village Master","descript":"Enter 10 different village buildings","prizes":[items.Bread for i in range(5)]+[items.Grass,items.Grass,items.Carrot]},{"active":True,"amount":25,"name":"Talk About Tired Feet","descript":"Enter 25 different village buildings","prizes":[items.TownMap3,items.StrongHealPotion,items.StrongHealPotion]}]

caves=[{"active":True,"amount":5,"name":"Cave Explorer","descript":"Explore 5 different Caves","prizes":[items.Bone,items.GoldCoin,items.GoldCoin,items.GoldCoin,items.HealPotion]},{"active":True,"amount":10,"name":"Cave Master","descript":"Explore 10 different Caves","prizes":[items.CaveExitsBook]}]

places=[{"active":True,"amount":5,"name":"Explorer","descript":"Explore 5 different places","prizes":[items.GoldCoin for i in range(5)]}]

all_ach=zombies+ogres+creepers+bears+dragons+monsters+killed+obtainable+trades+houses+caves+places
