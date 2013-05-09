import string


class Room():
	"""docstring for Room"""
	def __init__(self):
		self.desc = []
		self.items = []
itemList = []
roomList = []
class Player():
	"""docstring for ClassName"""
	def __init__(self):
		self.name = ""
		self.curRoom = ""
		self.curDir = ""
		self.inv = []
		self.takenInv = []
		self.armorScore = 0
		self.weaponScore = 0
		self.Score = 0

class Item():
	def __init__(self):
		self.name = ""
		self.desc = ""
		self.scoreVal = 0
		self.armorVal = 0
		self.dir = ""
		self.weaponVal = 0		


if(direction == north):
    printNow("Looking North, you see nothing interesting.") 
  if(direction == south):
    printNow("Looking South, you see a door.") 
  if(direction == east):
    printNow("Looking East, you see the cast-iron tub sitting along a diagonal wall.") 
    if (taken.count(wadOHair) == 0):
      printNow("In the tub you see a disgusting wad of hair.")
    if (taken.count(clothes) == 0):
      printNow("You see your clothes folded neatly at the base of the tub.")    
  if(direction == west):
    printNow("Looking west, you see a sink on a pedestal with a slowly dripping faucet.  You hear the faint sound of music coming from the other side of the wall. ") 
def initItems():
	item0 = Item()
	item1 = Item()
	item2 = Item()
	item3 = Item()
	item4 = Item()
	item5 = Item()
	item6 = Item()

	item0.desc="You see a pile of neatly folded CLOTHES"
	item0.name ="clothes"
	item0.dir = 1

	item1.desc="In the tub you see a disgusting wad of HAIR."
	item1.name ="hair"
	item1.dir = 1

	item2.desc="On top of the desk you see a PAPERCLIP"
	item2.name ="paperclip"
	item2.dir = 2

	item3.desc="in the corner you see see a couple D BATTERYies"
	item3.name ="battery"
	item3.dir = 0

	item4.desc="you see a FUSE in the radio"
	item4.name ="fuse"
	item4.dir = 1

	item5.desc="you see a RUBBER BAND is wrapped around a naked barbies throat"
	item5.name ="rubber band"
	item5.dir = 2

	item6.desc="You took all your items and somehow made a BOMB"
	item6.name ="bomb"
	item6.dir = -1


def initRooms():
	room0 = Room()
	room0.desc.append("Looking North, you see nothing interesting.")
	room0.desc.append("Looking East, you see the cast-iron tub sitting along a diagonal wall.") 
	room0.desc.append("Looking South, you see a door.") 
	room0.desc.append("Looking west, you see a sink on a pedestal with a slowly dripping faucet. You hear the faint sound of music coming from the other side of the wall. ")
	room0.items.append(itemList[0])
	room0.items.append(itemList[1])
	roomList.append(room0)

	room1 = Room()
	room1.desc.append("Looking North, You see a Door")
	room1.desc.append("Looking East, you notice a boreded up window that allows just a small amount of light in the room.") 
	room1.desc.append("Looking South, you see a desk") 
	room1.desc.append("Looking west, you see a slightly opened door which is red")
	room1.items.append(itemList[0])
	roomList.append(room1)

	room2 = Room()
	room2.desc.append("Looking North, you see see a green door, and hear what sounds like a baseball game comeing from the room on the other side")
	room2.desc.append("Looking East, you see a red door")
	room2.desc.append("Looking South, you see a door with a combination lock.") 
	room2.desc.append("Looking west, you see a door with no knob and a hole has been kicked in")
	roomList.append(room2)

	room3 = Room()
	room3.desc.append("Looking North, you see an empty doorway")
	room3.desc.append("Looking East, you see a door with no knob and a hole has been kicked in") 
	room3.desc.append("Looking South, you a wall with peeling paint and a few holes that may have been cause by mice") 
	room3.desc.append("Looking west, you see a painting of a person with a wicked mullet")
	roomList.append(room3)

	room4 = Room()
	room4.desc.append("Looking North, you see a slanted wall")
	room4.desc.append("Looking East, you see the plainest looking door you've ever seen if it were a women you would call it Jane") 
	room4.desc.append("Looking South, you see a vacuous space under a portal of wood") 
	room4.desc.append("Looking west, you see a slanted wall, with some curse words written on it in spay paint, and a number offering a good time")
	room4.items.append(itemList[3])
	roomList.append(room4)

	room5 = Room()
	room5.desc.append("Looking North, you see a window painted all black")
	room5.desc.append("Looking East, you see a raido tuned to AM SIX EIGHT ZERO bolted to the wall playing a baseball game, it sounds like the SF giants are beating the brewers by 15") 
	room5.desc.append("Looking South, you see a door with deadbolt that can be unlocked from this side") 
	room5.desc.append("Looking west, you see your good friend 'Jane'")
	room5.items.append(itemList[4])
	roomList.append(room5)

	room6 = Room()
	room6.desc.append("")
	room6.desc.append("") 
	room6.desc.append("") 
	room6.desc.append("")
	roomList.append(room6)

	room7 = Room()
	room7.desc.append("Looking North, you see a bronze spitoon next to the door you open with the combination")
	room7.desc.append("Looking East, you see a door, and you start wondering why the fuck there are so many doors in this place") 
	room7.desc.append("Looking South, you see a doorway that has been covered with bricks, the middle most brick is missing and you can see daylight through it.") 
	room7.desc.append("Looking west, You see a painter of a Mulleted man with a child on his knee this picture stirs up emotion in you for some reason")
	roomList.append(room7)

	room8 = Room()
	room8.desc.append("Looking North, you see a RUBBER BAND hanging from a nail in the wall")
	room8.desc.append("Looking East, you see a slanted wall with lots of what looks like human claw marks and see a few finger nails at the base of the wall") 
	room8.desc.append("Looking South, you see a slanted wall with lots of what looks like human claw marks and see a few finger nails at the base of the wall") 
	room8.desc.append("Looking west, you see a door and begin signing the song People are Strange")
	room8.items.append(itemList[5])
	roomList.append(room8)






def playGame():
	p = Player()
	p.name = raw_input("You think your name might be..")

	initItems()
	initRooms()




playGame()