'''a) Write a python program to calculate the total number of an item being brought by all the guests given in the below list.

allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, 
 'Bob': {'ham sandwiches': 3, 'apples': 2}, 
 'Carol': {'cups': 3, 'apple pies': 1}}
'''

allGuests={'Alice':{'apple':5,'pretzels':2},
           'Carol':{'apple pie':3,'apple':2},
           'sam':{'donuts':4,'cake':1}}

def dallguests(guests,item):
    num=0
    for k,v in guests.items():
        num=num+v.get(item,0)
    return num



print("-Apple: "+str(dallguests(allGuests,'apple')))
print("-cake: "+str(dallguests(allGuests,'cake')))
print("-donuts: "+str(dallguests(allGuests,'donuts')))
print("-pretzels: "+str(dallguests(allGuests,'pretzels')))
print("-apple piw: "+str(dallguests(allGuests,'apple pie')))