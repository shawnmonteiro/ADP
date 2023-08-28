stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayinv(inventory):
    total_items=0
    for item,qty in inventory.items():
        print(str(qty)+ item)
        total_items+=qty
    print("Total items"+str(total_items))

def addtoinv(inv,addlist):

    for item in addlist:
        inv.setdefault(item,0)
        inv[item]+=1
    return inv
    



dragonloot=['gold','silver','ruby','crystal','dagger','gold']

addtoinv(stuff,dragonloot)
displayinv(stuff)

