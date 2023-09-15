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

## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar
}
