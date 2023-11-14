"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item


class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            return [x for x in user_items if x.name != "old book"]
        return user_items

class EnchantingTable(Room):
    def run_story(self, user_items):
        print("You enter a dimly lit room, filled with an eerie, ominous hum.")
        print("In the center, an Enchanting Table glows faintly, surrounded by rows of ancient bookshelves.")

        sharpness_V = Item("Sharpness V", "sharper than rihanna", movable=True)
        choice = input("You see a book surrounded by a mystical glow lying on one of the bookshelves. Do you want to pick it up? (yes/no)\n").lower()
        if choice == "yes":
            return user_items.append(sharpness_V)
        else:
            print("As you wish")
        return user_items

    
## ----------------------------------------------------------------
## List here all rooms


toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
enchanter = EnchantingTable("enchanting", "Luckily you just hit 30 levels!")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "enchanter": enchanter
    # "my_room_key": my_room
}
