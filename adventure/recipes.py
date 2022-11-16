import items

def boots(item1,item2):
    return {"item":item1,"amount":4,"item2":item2,"amount2":1}

def leggings(item1,item2):
    return {"item":item1,"amount":7,"item2":item2,"amount2":1}

def chest(item1,item2):
    return {"item":item1,"amount":8,"item2":item2,"amount2":1}

def helmet(item1,item2):
    return {"item":item1,"amount":5,"item2":item2,"amount2":1}

la_b=boots(items.Leather,items.LeatherBoots)
la_l=leggings(items.Leather,items.LeatherLeggings)
la_c=chest(items.Leather,items.LeatherChest)
la_h=helmet(items.Leather,items.LeatherHelmet)

ia_b=boots(items.Iron,items.IronBoots)
ia_l=leggings(items.Iron,items.IronLeggings)
ia_c=chest(items.Iron,items.IronChest)
ia_h=helmet(items.Iron,items.IronHelmet)

da_b=boots(items.Diamond,items.DiamondBoots)
da_l=leggings(items.Diamond,items.DiamondLeggings)
da_c=chest(items.Diamond,items.DiamondChest)
da_h=helmet(items.Diamond,items.DiamondHelmet)

wheat={"item":items.Grass,"amount":11,"item2":items.Wheat,"amount2":1}
bread={"item":items.Wheat,"amount":3,"item2":items.Bread,"amount2":1}
apple_pie={"item":items.Apple,"amount":5,"item2":items.ApplePie,"amount2":1}
honeycomb={"item":items.Honey,"amount":4,"item2":items.Honeycomb,"amount2":1}
sack={"item":items.Leather,"amount":7,"item2":items.Sack,"amount2":1}

recipes=[la_b,la_l,la_c,la_h,ia_b,ia_l,ia_c,ia_h,da_b,da_l,da_c,da_h,wheat,bread,apple_pie,honeycomb,sack]
