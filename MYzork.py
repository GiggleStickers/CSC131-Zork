######################################################################
# Name: Katherine Guillot
# Date: 12/19/2017
# Description: Strangling superstar Shia Lebeouf
######################################################################
######################################################################

# the blueprint for a room
class Room(object):
    # the constructor
    def __init__(self, name):
        # Contains the room's name.
        self.name = name
        # Contains the room's exits (north, south, etc.).
        self.exits = []
        # Contains the rooms found at each exit (to the south of this \
        # room is room 2).
        self.exitLocations = []
        # Contains the observable items in the room.
        self.items = []
        # Contains the descriptions of the observable items in the room.
        self.itemDescriptions = []
        # Contains the items in the room that can be placed in inventory.
        self.grabbables = []

        # Getters and setters for the instance variables

        @property
        def name(self):
            return self._name
        #
        @name.setter
        def name(self, value):
            self._name = value

        @property
        def exits(self):
            return self._exits
        #
        @exits.setter
        def exits(self, value):
            self._exits = value

        @property
        def exitLocations(self):
            return self._exitLocations
        #
        @exitLocations.setter
        def exitLocations(self, value):
            self._exitLocations = value

        @property
        def items(self):
            return self._items
        #
        @items.setter
        def items(self, value):
            self._items = value

        @property
        def itemDescriptions(self):
            return self._itemDescriptions
        #
        @itemDescription.setter
        def itemDescriptions(self, value):
            self._itemDescription = value

        @property
        def grabbables(self):
            return self._grabbables
        #
        @grabbables.setter
        def grabbables(self, value):
            self._grabbables = value
            
        # Adds an exit to the room.
        # The exit is a string (e.g., north).
        # The room is an instance of a room
        def addExit(self, exit, room):
            # Append the exit and room to the appropriate lists.
            self._exits.append(exit)
            self._exitLocations.append(room)

        # Adds an item to the room.
        # The item is a string (e.g., table).
        # The desc is a string that describes the item (e.g., it is made
        # of wood).
        def addItem(self, item, desc):
            # Append the item and exit to the appropriate lists.
            self._items.append(item)
            self._itemDescriptions.append(desc)

        # Adds a grabbable item to the room.
        # The item is a string (e.g., key).
        def addGrabbable(self, item):
            # Append the item to the list.
            self._grabbables.append(item)

        # Removes a grabbable item from the room.
        # The item is a string (e.g., key).
        def delGrabbable(self, item):
            # Remove the item from the list.
            self._grabbables.remove(item)

        # Returns a string a string description of the room.
        def __str__(self):
            # First, the room name.
            s = "You are in {}. \n" .format(self.name)

            # Next, the items in the room.
            s += "You see: "
            for item in self.items:
                s += item + " "
            s += "\n"

            # Next, the exits from the room.
            s += "Exits: "
            for exit in self.exits:
                s += exit + " "

            return s
# Creates the rooms.
def createRooms():
        # r1 through r4 are the four rooms in the mansion
        # currentRoom is the room the player is currently in (which can
        # be one of r1 through r4).
        # since it needs to be changed in the main part of the program,
        # must be global
        global currentRoom

        # Create the rooms and give them meaningful names.
        r1 = Room("Room 1")
        r2 = Room("Room 2")
        r3 = Room("Room 3")
        r4 = Room("Room 4")

        # Add exits to room 1
        r1.addExit("east", r2)   # To the east of room 1 is room 2.
        r1.addExit("south", r3)
        # Add grabbables to room 1
        r1.addGrabbable("key")
        # Add items to room 1
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
        r1.addItem("table", "It is made of oak. A golden key rests on it.")

        r2.addExit("west", r1)
        r2.addExit("south", r4)
        r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
        r2.addItem("fireplace", "It is full of ashes.")

        r3.addExit("north", r1)
        r3.addExit("east", r4)
        r3.addGrabbable("book")
        r3.addItem("bookshelves", "They are empty. Go figure.")
        r3.addItem("statue", "There is nothing special about it. The nipples are worn away.")
        r3.addItem("desk", "The statue is resting on it. So is a book.")

        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", None)   # DEATH!
        r4.addGrabbable("6-pack")
        r4.addItem("brew_rig", "Cherry is brewing some sort of oatmeal \
                  stout on the brew rig. A 6-pack is resting beside it.")

        currentRoom = r1


###########################################################################
# START THE GAME!!!
inventory = [] # Nothing in inventory... yet.
createRooms() # Add the rooms to the game.
        
# Play forever (well, at least until the player dies or asks to quit)
while (True):
    # Set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}\n" .format(currentRoom, inventory)

    if (currentRoom == None):
        death()
        break

    print ("===========================================================")
    print (status)
    




