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

#create gym room
class Gym(Room):
    def run_story(self, user_items):
        print("Welcome to the new ZDD gym! After 8 hours of sitting, your back tends to ache.\nBut now, that's a thing of the past! At ZDD, you will find the solution.\nOn the first floor, we have now opened a gym for you, where you can work out all around the clock.\nUpon entering the gym, you'll find various equipment with choices for what you want to train:")
        print("These are your training options:\n1. Bulging biceps\n2. Solid chest\n3. Broader than the bouncer (skip leg day)")
        #loop till you do a workout, dont be lazy
        while True:
            user_choice = int(input("Please only enter the number: "))
            if 1 <= user_choice <= 3:
                print("Great job! Here is your reward:")
                #create item instance
                workout_shake = Item("Post-workout shake", "A high protein shake", movable=True)

                #add item to inventory
                user_items.append(workout_shake)
                
                #show the name of the item
                item_names = [item.name for item in user_items]
                return user_items, print(f"Items: {item_names}")
            else:
                print("Pick 1, 2, or 3")
## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "gym_first_floor": gym_first_floor
}
