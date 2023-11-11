"""This is to keep all special rooms of the ZDD."""
from main_classes import Room


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

class PigeonHouse(Room):
    def run_story(self, user_items):
        print("You see a lot of pigeons.")

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
pigeon_house = PigeonHouse("pigeon house", "A pigeon house.")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,

    # Add your room key-value pairs here:
    "pigeon_house": pigeon_house
}
