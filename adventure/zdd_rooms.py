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

class DarkRoom(Room):

    def run_story(self, user_items):

        # first description of the room and the story in there
        print("You look around but don't see that much. It's very dark and mysterious. You don't recognize what room this is.\n"
              "It's very scary but after you look around for a bit longer you notice a little lightswitch and press it.\n"
              "A few red lights turned on and you understand it's a darkroom for photographers\n"
              "But it's still creepy in the room...You hear a few quiet noises...\n"
              "You're scared to death because suddenly a mysterious creature stands in front of you\n"
              "He holds a film camera in it's hands\n"
              "You're really confused cause he tells you to pose for a picture...\n\n"
              "What do you want to do?\n"
              "1: Smile into the camera\n"
              "2: hold up a peace sign\n"
              "3: give it a thumbs up\n"
              "4: run away"
            )
        
        while True:
            # the user can decide which option he wants to choose
            user_choice = input("Please enter the number of your choice: ")

            # so the story continues if the user doesn't run away
            if user_choice in ["1", "2", "3"]:
                
                # smile into the camera
                if user_choice == "1":
                    print("Creature: Wow you have a beautiful smile")

                # hold up a peace sign
                elif user_choice == "2":
                    print("Creature: Nice pose thank you for the picture!")
        
                # give it a thumbs up
                elif user_choice == "3":
                    print("Creature: Finally someone who isn't scared of me and runs away")
                
                # story continues
                print("Because you were so nice to the creature he offers you a camera")

                while True:
                    # user decides whether to accept the camera or not
                    camera_choice = input("Do you want to accept the gift? (yes or no): ")
                    
                    # if the user wants to accept the camera
                    if camera_choice.lower() == "yes":
                        print("Creature: This really means a lot to me!")
                        # creates the camera item and appends it to the inventory
                        camera = Item("film camera", "you can take pictures of the new ZDD", movable=True)
                        user_items.append(camera)
                        break
                    
                    # if the user doesn't want to accept the camera the story in this room ends
                    elif camera_choice.lower() == "no":
                        print("Creature: Okay but if you rethink your choice, feel free to come and visit me here!")
                        break

                    # to intercept other entries than "yes" or "no"
                    else:
                        print("Invalid input! Try to enter yes or no")
            
            # if the user runs away the story in this room ends
            elif user_choice == "4":
                print("You're out of breath because you were running for your life.\n"
                    "Now you're back in the hallway of the cellar")
                break
            # to intercept other entries than 1,2,3 or 4
            else:
                print("Invalid input! Try to enter a number of 1-4") 

            break
        return user_items


toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Add your room instance here, similar to the example below:
pigeon_house = PigeonHouse("pigeon house", "An abandoned pigeon house.")
movieTheater_2ndFloor = MovieTheater_2ndFloor("movie theater",
                                              "You can see rows of seats facing a large screen."
                                              )
darkroom = DarkRoom("darkroom", "A mysterious darkroom with a surprise")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    "pigeon_house": pigeon_house,
    "movieTheater_2ndFloor": movieTheater_2ndFloor,
    "dark_room": darkroom
}

