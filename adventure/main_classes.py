"""
ZDD Text Adventure Game Framework.

This module provides the basic structure for a text-based adventure game,
including classes for handling commands, representing game items, rooms, and floors.
The framework allows for building interactive environments where players can explore rooms,
collect items, and navigate between floors.

Classes:
    - CommandHandler: Manages global commands like 'exit' and 'inventory'.
    - Item: Represents individual game items with properties and interactions.
    - Room: Encapsulates game rooms with descriptions, items, and interactions.
    - Floor: Organizes rooms and their interconnections on a specific level of the game environment.
"""


class CommandHandler:
    """Handles global commands like 'exit' and 'inventory'."""
    def __init__(self, game):
        self.game = game

    def handle_global_commands(self, command):
        if command == "exit":
            print("Thank you for exploring the ZDD!")
            self.game.game_active = False  # End the game
        elif command == "inventory":
            if len(self.game.items) == 0:
                print("Your pockets are empty... as well as your hands... sad.")
            else:
                print("You have the following items:")
                print(", ".join([x.name.upper() for x in self.game.items]))


class Item:
    """Represents a game item with attributes like name, description, and movability."""
    def __init__(self, name, description, movable=False):
        """Construct a new Item
        
        Parameters
        ----------
        name : str
            Name of the item
        description : str
            Description of the item.
        movable : bool
            Determines whether the item is movable, i.e., whether it can be added to the inventory.
            Defaults to False.
        """
        self.name = name
        self.description = description
        self.movable = movable

    def describe(self):
        print(self.description)

    def is_movable(self, user_items, other_item_required=None):
        """Returns True if item can be added to the inventory."""
        if not self.movable:
            return False
        if not other_item_required:
            return True
        if other_item_required and other_item_required in user_items:
            return True
        return False


class Room:
    """Represents a game room with attributes and methods for room interaction."""
    def __init__(self, name, description, items=None):
        """Create a Room

        Parameters
        ----------
        name : str
            Name of the room.
        description : str
            Short description of the room.
        items : Optional
            Additional items to (Item objects) that will be visible to the user upon inspection of the room.
        """
        self.name = name
        self.description = description
        self.visited = 0
        if items is None:
            self.items = []
        elif isinstance(items, list):
            self.items = items
        else:
            self.items = [items]

    def enter_room(self, user_items, command_handler):
        """Main method of Room class."""
        self.visited += 1
        print(40 * "-")

        # Run whatever happens in this room:
        user_items = self.run_story(user_items)

        while True:
            action = input(">> 'leave' to exit the room, 'inspect' to look around: ").lower()

            command_handler.handle_global_commands(action)
            if not command_handler.game.game_active:  # If game is not active anymore, break
                return user_items

            if action == "leave":
                print("You leave the room...")
                return user_items
            elif action == "inspect":
                user_items = self.show_items(user_items)
            else:
                print("Invalid command!")

    def run_story(self, user_items):
        """Customizable method where students can add functionality."""
        print(f"You've entered the {self.name} {self.visited} times.")
        # By default, this method doesn't do much, but students can enhance this method in their custom rooms.

        return user_items

    def show_items(self, user_items):
        """Show all items in the room and ask for addition to the inventory (if item is movable)."""
        if self.items is None or (len(self.items) == 0):
            print("There is nothing of particular interest...")
            return user_items

        print("In here you find...")
        for item in self.items[:]:
            item.describe()
            if item.is_movable(user_items):
                while True:
                    action = input(f"Do you want to take {item.name}? (yes/no): ").lower()
                    if action == "yes":
                        user_items.append(item)
                        self.items.remove(item)
                        print(f"You've taken the {item.name}.")
                        break
                    if action == "no":
                        print(f"You leave the {item.name} where it is.")
                        break
                    print("Please answer with yes or no!")
        return user_items

    def get_detail(self):
        return f"You are in the {self.name}. {self.description}"


class Floor:
    """Represents a game floor containing rooms and connections to other floors."""
    def __init__(self, name, description):
        """Create a new Floor.

        Parameters
        ----------
        name : str
            Name of the floor.
        description : str
            Short description of the floor.
        """
        self.name = name
        self.description = description
        self.rooms = {}
        self.connected_floors = {}

    def add_room(self, direction, room):
        """Add a room to the floor."""
        self.rooms[direction] = room

    def get_room(self, direction):
        """Get room in a specific direction."""
        return self.rooms.get(direction, None)

    def add_connection(self, direction, floor):
        """Define connections between floors."""
        self.connected_floors[direction] = floor

    def get_floor_in_direction(self, direction):
        return self.connected_floors.get(direction, None)

    def get_orientation(self):
        details = ""
        for direction, room in self.rooms.items():
            details += f"\nType 'enter {direction}' to go to {room.name}."
        for direction, floor in self.connected_floors.items():
            details += f"\nType 'go {direction}' to go to {floor.name}."
        return details
