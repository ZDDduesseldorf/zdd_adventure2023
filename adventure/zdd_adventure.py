class Item:
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

    def is_movable(self, items, other_item_required=None):
        """Returns True if item can be added to the inventory."""
        if not self.movable:
            return False
        if not other_item_required:
            return True
        if other_item_required and other_item_required in items:
            return True
        return False

class Room:
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
        if isinstance(items, list):
            self.items = items
        else:
            self.items = [items]

    def enter_room(self, user_items):
        """Main method of Room class."""
        self.visited += 1
        print(40 * "-")

        # Run whatever happens in this room:
        user_items = self.run_story(user_items)

        while True:
            action = input(">> 'leave' to exit the room, 'inspect' to look around: ").lower()
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
        if len(self.items) > 0:
            print("In here you find...")
        else:
            print("There is nothing of particular interest...")
            return user_items

        for item in self.items:
            item.describe()
            if item.is_movable(self.items):
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
        details = f"You are on the {self.name}. {self.description}\n"
        for direction, room in self.rooms.items():
            details += f"\nType 'enter {direction}' to go to {room.name}."
        for direction, floor in self.connected_floors.items():
            details += f"\nType 'go {direction}' to go to {floor.name}."
        return details


class ZDDAdventure:
    def __init__(self):
        self.items = []
        self.floors = self.create_floors()
        self.current_floor = self.floors['cellar']
        self.current_room = None

    def create_floors(self):
        # Define the floors
        cellar = Floor("cellar", "It's a bit chilly here. Old books are stored in wooden racks.")
        ground_floor = Floor("ground floor", "You see a reception desk and a hallway leading to lecture halls.")
        first_floor = Floor("first floor", "There are study rooms and a library entrance here.")
        second_floor = Floor("second floor", "This floor hosts the professors' offices and some research labs.")
        # roof_floor = Floor("roof", "You really shouldn't be here!!!")

        # Connect floors
        cellar.add_connection("up", ground_floor)
        ground_floor.add_connection("down", cellar)
        ground_floor.add_connection("up", first_floor)
        first_floor.add_connection("down", ground_floor)
        first_floor.add_connection("up", second_floor)
        second_floor.add_connection("down", first_floor)

        # Define rooms in each floor
        analog_book = Item("old book", "a real book made of paper", movable=True)
        archive_room = Room("archive", "Old records and dusty books everywhere.",
                            analog_book)
        cellar.add_room("archive", archive_room)

        reception = Room("reception", "You see a welcoming desk and a receptionist.")
        ground_floor.add_room("reception", reception)

        #... Add other rooms ...

        return {
            "cellar": cellar,
            "ground floor": ground_floor,
            "first floor": first_floor,
            "second floor": second_floor
        }

    def play(self):
        print("Welcome to ZDD Adventure!")
        while True:
            print(self.current_floor.get_orientation())
            print("Type 'inventory' to inspect your inventory.")
            action = input("What do you want to do? ('exit' to end): ").lower()
            # Exit the game
            if action == "exit":
                print("Thank you for exploring the ZDD!")
                break
            # Look up the inventory
            elif action == "inventory":
                if len(self.items) == 0:
                    print("Your pockets are empty... as well as your hands... sad.")
                else:
                    print("You have the following items:")
                    print("\t".join([x.name.upper() for x in self.items]))
            # Change the floor:
            elif action.startswith("go "):
                direction = action.split(" ")[1]
                next_floor = self.current_floor.get_floor_in_direction(direction)
                if next_floor:
                    self.current_floor = next_floor
                    self.current_room = None
                else:
                    print("You can't go in that direction!")
            # Enter a room:
            elif action.startswith("enter "):
                direction = action.split(" ")[1]
                next_room = self.current_floor.get_room(direction)
                if next_room:
                    self.current_room = next_room
                    self.current_room.enter_room(self.items)
                else:
                    print("There is no such room...")
            else:
                print("Unknown command!")


if __name__ == "__main__":
    adventure = ZDDAdventure()
    adventure.play()
