"""This is to keep all special rooms of the ZDD."""
from main_classes import Room
from main_classes import Item


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





toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
vr_room = VR_RoomFirstFloor("vr_room", "Purple LED lights lightning up the whole room.. what is this place? You find a little station in the middle of the room..")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "vr_room": vr_room
}
