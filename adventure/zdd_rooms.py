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

## ----------------------------------------------------------------
## List here all rooms
class MovieTheater_2ndFloor(Room):
    
    #This method is structured differently, because the player cannot take any items from this room               
    def run_story(self, user_items):
            print("\nThe room is filled with the soft glow of ambient lighting...\n"
                  "You notice rows of seats facing a massive screen."
                  )
            return user_items
   

class PigeonHouse(Room):
    def run_story(self, user_items):
        # Introduction and initial choices
        print("You walk through an old, slightly broken door.\n"
              "Inside, there are no pigeons.\n"
              "You see an old window, do you want to open it?")
        
        # First Choice: Open or Don't Open the Window
        while True:
            choice = input("Type 'open window' or 'do not open window'\n"
                           "What do you want to do?: ")
            if choice == "open window":
                # Outcome: User chooses to open the window
                print("The window opens, and you hear something fall to the floor behind you. You go there and see a broken egg and a baby pigeon on the floor.\n")
                break
            elif choice == "do not open window":
                # Outcome: User decides not to open the window
                print("You decide not to open the window and look around the room. You see an abandoned pigeon's nest in a corner.\n")
                
                # Second Choice: Inspect the Nest or Don't Inspect
                while True:
                    inspect_choice = input("Type 'inspect nest' or 'do not inspect nest'\n"
                                           "What do you want to do?: ")
                    if inspect_choice == "inspect nest":
                        # Outcome: User decides to inspect the nest
                        print("You inspect the nest and see an egg. Suddenly the egg moves, and a baby pigeon hatches from it.\n")
                        break
                    elif inspect_choice == "do not inspect nest":
                        # Outcome: User decides not to inspect the nest
                        print("But suddenly you hear a soft 'gurrrrrr' and look into the nest. You see a little baby pigeon that has obviously just hatched.\n")
                        break
                    else:
                        # Handling invalid inputs
                        print("Invalid input. Please try again.")
            else:
                # Handling invalid inputs
                print("Invalid input. Please try again.")
            
            break  # Exiting the first while loop

        # Third Choice: Ask the pigeon to be a companion
        while True:
            choice = input("Do you want to ask the pigeon to be your companion? (yes/no): ")
            if choice == "yes":
                # Outcome: User decides to make the pigeon their companion
                print("It answers 'gurrr!' which (of course) means yes, so you put it into your bag.")
                pigeon = Item("baby pigeon", "A baby pigeon which only makes 'gurrr!'", movable=True)
                user_items.append(pigeon)
                break
            elif choice == "no":
                # Outcome: User decides not to make the pigeon their companion
                print("The pigeon looks at you with its big round eyes and says 'gurrr!'. Maybe you should think about it again.")
            else: 
                # Handling invalid inputs
                print("Invalid input. Please try again.")
            
        return user_items

class FunnyGunnyShop(Room):

    def run_story(self, user_items)
        
        #Introduction to the room:
        print("As you approach the door, you hear a weird sounding melody, which gets louder and louder.\n" 
              "Is someone singing? Or is it a ritual?\n"
              "Do you still want to get in?\n")
        
        while True:
            #First Choice: To go in or not
            choice = input("Type 'yes' if you still want to go in or type 'no' if you want to leave... " )

            #If input is "yes" the user gets into the room
            if choice == r"[Yy]es":
                
                print("You enter the room and you see a man behind something looking like a counter.\n"
                      "For how long is he standing there and why does he not react on your approach?\n"
                      "Do you want to talk to him or do you want to slap him?\n")
                
                while True:
                    #Second Choice: Slap him or speak with him
                    slap_choice = input("Type 'slap him' or 'talk to him'")

                    if slap_choice == r"[Ss]lap [Hh]im":

                        print("Little aggressive don't you think?\n"
                            "Well the man did not flinch or move and keeps on going with those weird noises.\n"
                            "What do you want to do now?")
                    
                    elif slap_choice == r"[Tt]alk to him":
                        
                        print("Wow looks like he can speak. He welcomed you and introduced you to his shop.\n"
                              "He is saying that, he offers some items but he only offers one of them each time you enter the room\n"
                              "Do you want to know which item he sells now?\n")




                
                

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Add your room instance here, similar to the example below:
pigeon_house = PigeonHouse("pigeon house", "An abandoned pigeon house.")
movieTheater_2ndFloor = MovieTheater_2ndFloor("movie theater",
                                              "You can see rows of seats facing a large screen."
                                              )
funny_gunny_shop = 

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    "pigeon_house": pigeon_house,
    "movieTheater_2ndFloor": movieTheater_2ndFloor,
    "funny_gunny_shop":funny_gunny_shop
}
