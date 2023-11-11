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
        print("You walk through an old, slightly broken door.\n"
              "Inside, there are no pigeons.\n"
              "You see an old window, do you want to open it?")
        
        while True:
            choice = input("Type 'open window' or 'do not open window'\n"
                           "What do you want to do?: ")
            if choice == "open window":
                print("The window opens, and you hear something fall to the floor behind you. You go there and see a broken egg and a baby pigeon on the floor.\n"
                      "You ask the baby pigeon if it would like to be your companion, and it answers with 'gurrrrr!' \n"
                      "Of course, that means 'yes,' so you put the baby pigeon in your bag.\n")
                break
            elif choice == "do not open window":
                print("You decide not to open the window and look around the room. You see an abandoned pigeon's nest in a corner.\n")
                
                while True:
                    inspect_choice = input("Type 'inspect nest' or 'do not inspect nest'\n"
                                           "What do you want to do?: ")
                    if inspect_choice == "inspect nest":
                        print("You inspect the nest and see an egg. Suddenly the egg moves, and a baby pigeon hatches from it.\n"
                              "You ask the baby pigeon if it would like to be your companion, and it answers with 'gurrrrr!' \n"
                              "Of course, that means 'yes,' so you put the baby pigeon in your bag.\n")
                        break
                    elif inspect_choice == "do not inspect nest":
                        print("But suddenly you hear a soft 'gurrrrrr' and look into the nest. You see a little baby pigeon that has obviously just hatched.\n"
                              "You ask the baby pigeon if it would like to be your companion, and it answers with 'gurrrrr!' \n"
                              "Of course, that means 'yes,' so you put the baby pigeon in your bag.\n")
                        break
                    else:
                        print("Invalid input. Please try again.")
            else:
                print("Invalid input. Please try again.")
            break

 

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
pigeon_house = PigeonHouse("pigeon house", "An abandoned pigeon house.")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,

    # Add your room key-value pairs here:
    "pigeon_house": pigeon_house
}
