import string

itemList = []
roomList = []
room2DoorNorth = 0
room2DoorSouth = 0
gameover = 0
class Room():
	"""docstring for Room"""
	def __init__(self):
		self.desc = []
		self.items = []

class Player():
	"""docstring for ClassName"""
	def __init__(self):
		self.name = ""
		self.curRoom = ""
		self.curDir = ""
		self.inv = []
		self.usedInv = []
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
		self.taken = "contgrats you've taken " + self.name		

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

	itemList.append(item0)
	itemList.append(item1)
	itemList.append(item2)
	itemList.append(item3)
	itemList.append(item4)
	itemList.append(item5)
	itemList.append(item6)

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
	room1.items.append(itemList[2])
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


def doorHandler():
	global room2DoorNorth
	global room2DoorSouth
	global gameover
	if p.curRoom == roomList[0] and p.curDir == 2:
		p.curRoom = roomList[1]
		return
	if p.curRoom == roomList[1] and p.curDir == 0:
		p.curRoom = roomList[0]
		return
	if p.curRoom == roomList[1] and p.curDir == 3:
		p.curRoom = roomList[2]
		return
	if p.curRoom == roomList[2] and p.curDir == 1:
		p.curRoom = roomList[1]
		return
	if p.curRoom == roomList[2] and p.curDir == 3:
		p.curRoom = roomList[3]
		return
	if p.curRoom == roomList[2] and p.curDir == 0:
		if room2DoorNorth == 0:
			print "The door to the north is locked and impassable."
			return
		else:
			p.curRoom = roomList[5]
			return
	if p.curRoom == roomList[2] and p.curDir == 2:
		if room2DoorSouth == 0:
			print "You must figure out the three digit combination to unlock this door.  There is no way to force it."
			subaction = raw_input("The combination lock is a spinner with 3 numbers.  You can put in 000 to 999.  What do you want to try: ")
			if "680" in subaction:
				room2DoorSouth = 1
				print "The lock openned!"
			else:
				print "The lock doesn't budge."
			return
		else:
			p.curRoom = roomList[7]
			return

	if p.curRoom == roomList[3]:
		if p.curDir == 0:
			p.curRoom = roomList[4]
			return
		if p.curDir == 1:
			p.curRoom = roomlist[2]
			return
		return
	if p.curRoom == roomList[4]:
		if p.curDir == 1:
			p.curRoom = roomList[5]
		if p.curDir == 2:
			p.curRoom = roomList[3]
		return
	if p.curRoom == roomList[5]:
		if p.curDir == 2 and room2DoorNorth == 0:
			print "You see a door with a deadbolt that can be unlocked from this side."
			subaction = raw_input ("Would you like to unlock the door? [y/n]")
			if "y" in subaction:
				room2DoorNorth = 1
				print "You unlock the door."
			return
		if p.curDir == 2 and room2DoorNorth == 1:
			p.curRoom = roomList[2]
			return
		if p.curDir == 3:
			p.curRoom = roomList[4]
			return
		return
	if p.curRoom == roomList[7]:
		if p.curDir == 0:
			p.curRoom = roomList[2]
		if p.curDir == 1:
			p.curRoom = roomList[8]
		if p.curDir == 2:

			if len(p.inv) == 6:
				print "you lay out all the resources you've collected at the base of the door." 
				print "Before you realize what you are doing you've assembled the items into a bomb and placed it in the open doorway"
				print "you retreat to another room."
				print "You hear a loud bang followed by the sound of falling rubble"
				print "you go back into the room to see if worked."
				print "SUCCESS! as the cloud clears you see the man with a mullet from the pictures, he is much older now but you suddenly remeber who you are!"
				print "You are Mcguyvers grandchild"
				print "Mycyver with a tear in his eye comes and give you a hug, happy that his grandchild can fullfil the destiny and become the heir to his knowledge"
				print "you win!"
				gameover = 1
				return 
		return
	if p.curRoom == roomList[8]:
		if p.curDir == 3:
			p.curRoom = roomList[7]
		return

p = Player()

def playGame():
	global gameover
	east = "east"
	west = "west"
	north = "north"
	south = "south"
	help = "help"
	action ="rabbits"
	initItems()
	initRooms()

	print("You awake from what seemed like an endless dream.  Naked and Groggy-eyed, you wonder who you are.") 
	p.name = raw_input("You think your name might be..")
	print("Still hazy on who you are, and how you got here, you climb out of the tub")
	p.curDir = 1
	p.curRoom = roomList[0]
	while gameover == 0:
		print p.curRoom.desc[p.curDir]
		for item in p.curRoom.items:
			if item.dir == p.curDir:
				print item.desc
		action = raw_input("what would you like to do?")
		action = action.lower()
		if help in action:
			print "you can use the commands GO LOOK TAKE"
		elif "look" in action:
			if east in action:
				p.curDir = 1
				
			elif west in action:
				p.curDir = 3
				
			elif north in action:
				p.curDir = 0
				
			elif south in action:
				p.curDir = 2
				
			for item in p.curRoom.items:
				if p.curDir == item.dir:
					print item.desc
		elif "go" in action:
			if east in action:
				p.curDir = 1
			elif west in action:
				p.curDir = 3
			elif north in action:
				p.curDir = 0
			elif south in action:
				p.curDir = 2
			doorHandler()
		elif "take" in action:
			for item in p.curRoom.items:
				print item.name
				if item.name in action:
					p.inv.append(item)
					p.curRoom.items.remove(item)
					print item.taken
		






playGame()