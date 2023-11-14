"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import random as random
#import random for a random soda

class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            return [x for x in user_items if x.name != "old book"]
        return user_items

## ----------------------------------------------------------------
## List here all rooms

class SodaMachine(Room):
    def run_story(self, user_items):
        print("Welcome in the first room with the mysterious soda machine")
        action = input("Kick the machine for some soda's\n" )
        #type kick to start if function
        while True:
            if action == "kick":
                            cola = Item("Cola","Makes you run super fast", movable=True)
                            sprite = Item("Sprite","Your head turns into a lemon", movable=True)
                            fanta = Item("Fanta", "All the colors get super intense and bright",movable=True)
                            sodas = [cola,sprite,fanta]
                            user_items.append(random.choice(sodas))
                            item_name = [item.name for item in user_items]
                           
                            
                            return user_items, print("Nice! you got ", item_name)
            else:
                print("Type kick")
#check function for three random sodas
#a random soda get append in items and inventory
#return with a print statement
             


toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
soda_machine = SodaMachine("soda","mysterious soda machine.")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "soda_machine": soda_machine
}
