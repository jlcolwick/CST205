from java.lang.reflect import Array
import java
import string

#commands
north = "north" 
south = "south" 
east = "east" 
west = "west" 
help = "help"

#character
name = "" 
currentRoom = 1 
currentDirection = east
currentState = "init" 
armor = []
armorScore = 0
weaponScore = 0
inventory = [] 
usedInventory = []

#Items
taken = []
wadOHair = "wadOHair"
clothes = "clothes" 
paperClip = "paperclip"

class Item:
  name = ""
  room = 0
  direction = ""
  taken = false

def

class Player:
  #player class
  name = ""
  armor = []
  armorScore = 0
  weapon = []
  weaponScore = 0
  inventory = []
  usedInventory = []
  currentRoom = 1
  currentDirection = 0


def getAction():
  return requestString(Player.name + ", what would you like to do: ") 

def getName():
  Player.name = requestString("You think your name might be..") 
   
def start():
  global currentState
  printNow("You awake from what seemed like an endless dream.  Groggy-eyed, you wonder who you are.") 
  getName() 
  printNow("Still hazy on who you are, and how you got here, you take in your surroundings.") 
  
  printRoomDescription(currentRoom, currentState) 
  doorOpen = false 
  
  action = "rabbits"
  
  while action != "exit":
    action = getAction() 
    if ("get" in action or "take" in action or "pick up" in action) and "clothes" in action and (taken.count(clothes) == 0) and (currentState == init or currentState == east):
      taken.append(clothes);
      inventory.append(clothes) 
      printNow("You've taken the clothes.") 
    elif "equip" in action or "put on" in action and "clothes" in action and inventory.count(clothes) != 0:
      inventory.remove(clothes) 
      printNow("You've gotten dressed and feel a little less vulnerable.") 
      printNow("YOUR ARMOR IS NOW 1!!") 
    elif west in action:
      currentState = west 
      printRoomDescription(currentRoom, currentState) 
    elif east in action:
      currentState = east 
      printRoomDescription(currentRoom, currentState) 
    elif south in action and doorOpen == false:
      currentState = south 
      printRoomDescription(currentRoom, currentState) 
    elif north in action:
      currentState = north 
      printRoomDescription(currentRoom, currentState) 
    elif help in action:
      printRoomDescription(currentRoom, currentState) 
    elif (("take" in action or "get" in action or "pick up" in action) and "hair" in action) and inventory.count(wadOHair) == 0:
      taken.append(wadOHair)
      inventory.append(wadOHair) 
      printNow("You're disgusting.  You've now got a glob of wet, smelly hair in your pocket.") 
    elif currentState == south and "open" in action and "door" in action:
      doorOpen = true 
      printNow("You've opened the door to the south.") 
    elif south in action and doorOpen == true:
      roomTwo() 
    else:
      printNow("I'm sorry, you can't do that.") 
    
def printRoomDescription(room, direction):
  #if(direction == init):
   # printNow("Still hazy on who you are, and how you got here, you take in your surroundings.  You now realize you are lying naked as your name-day in a cold cast iron tub.") 
    #printNow("You climb out and see your clothes neatly folded at the base of the tub.") 
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
    
    

def roomTwo():
  printNow("There is a man standing on the other side in an impeccible suit.")
  printNow("He aims a very large rifle at you, and says something in a harsh language you do not understand.")
  printNow("In your confusion, you do not act fast, and he shoots you dead.. dead .. dead.")
    