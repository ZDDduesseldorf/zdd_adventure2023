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

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

class SmallBookCorner(Room):
    def run_story(self, user_items):
        # Introduction and initial choice
        print("As you walk along the floor, you find a small, comfy looking place just around the corner.\n"
              "There are bookshelves along the walls, two couches with a lot of pillows and a working desk surrounded by two chairs.\n"
              "Someone has seemingly forgotten their Laptop on the desk. They must have left in a hurry, the Laptop is still emitting light of the screensaver.\n"
              "Do you want to take a closer look at it?")
        
        #First Choice: Inspect or don't inspect the open Laptop
        while True:
            choice = input("Type 'inspect laptop' or 'do not inspect laptop'\n"
                           "What do you want to do?: ")
            if choice == "inspect laptop":
                # Outcome: User chooses to inspect the glowing Laptop
                print("The 3D Animation of pipes is giving you whiplash to the early 2000s. The person who was working here seems to be quite old.\n"
                      "The Screensaver stops as you touch the keypad. The dreaded words of 'Please enter your password' appear")
                
            elif choice == "do not inspect laptop":
                # Outcome: User decides to not inspect the open Laptop
                print("You decide to not inspect the Laptop. Data protection and safety is a big concern to you.\n"
                      "Instead your view is trailing towards the bookshelves. Do you want to see what kind of books are stored there?")
                
                # Second Choice: Inspect the Books or don't inspect the Books
                while True:
                    inspect_choice = input("Type 'inspect books' or 'do not inspect books'\n"
                                           "What do you want to do?: ")
                    if inspect_choice == "inspect books":
                        # Outcome: User decides to inspect the books
                        print("You inspect the books. They range from varying topics, which none are really that much of an interest to you.\n"
                              "One Book seems to have been put back in a hurry, it's nearly falling from the shelf.\n"
                              "There seems to be a piece of paper hanging on by a thread, nearly falling out of the pages.\n"
                              "There seems to be something written on that piece of paper.")
                        break
                    elif inspect_choice == "do not inspect books":
                        # Outcome: User decides not to inspect the books
                        print("Books? Nah, are you what, like 80 years old? They don't even have an Ebook-Reader laying around here.\n"
                              "As you turn away from the Bookshelves, you hit your head on a badly placed book, and it falls to the floor.\n"
                              "A single piece of paper caught your attention, laying directly next to the fallen book.\n"
                              "There seems to be something written on that piece of paper.")
                        break
                    else:
                        # Handling invalid inputs
                        print("Invalid input. Please try again.")
            else:
                # Handling invalid inputs
                print("Invalid input. Please try again.")
            
            break  # Exiting the first while loop


        # Third Choice: Inspect the paper or don't inspect it
        while True:
            choice = input("Do you want to take a closer look at the written note? (yes/no): ")
            if choice == "yes":
                # Outcome: User decides to take a closer look at the written note
                print("There is a 4 digit code on that piece of paper.... You ask yourself, if someone could really be that stupid.\n"
                      "Your nosiness gets the better of you. You take the piece of paper and walk towards the Laptop.\n"
                      "Do you want to try and enter the 4 digit code as the password?")
                
                # Fourth Choice: Want to steal a Laptop baby?
                while True:
                    hacking_choice = input("Type 'enter code' or 'do not enter code'\n"
                                           "What do you want to do?: ")
                    if hacking_choice == "enter code":
                        # Outcome: User decides to enter Code and take the Laptop with them
                        print("Geez. It actually worked. You are in. An adrenaline rush is flowing through your system.\n"
                              "You are the Hacker non gender defined Person of the Year. You pat yourself on the shoulder after the Hard Work.\n"
                              "You decide to take the Laptop with you, may come in handy or you may find the Person it originally belonged to.\n"
                              "But now its yours. YOURS!!")
                        laptop = Item("laptop", "There's no Internet connection, but it's YOURS!", movable=True)
                        user_items.append(laptop)
                        break
                    elif hacking_choice == "do not enter code":
                        # Outcome: User decides not to be a bad person and doesn't steal the Laptop
                        print("You are making your way to the Laptop, but with each step your conscience is getting heavier and heavier.\n"
                              "You really want to. But no, you shouldn't. But what if....? No, it wouldn't be right.\n"
                              "You are torn. You might want to think about this again a bit longer...")
                        
                    else:
                        # Handling invalid inputs
                        print("Invalid input. Please try again.")
           
                break  # Exiting the first while loop

            elif choice == "no":
                # Outcome: User decides not to take a closer look at the written note
                print("There is nothing else of importance in this room, only that white, shimmering piece of paper.\n"
                      "Something is really telling you to take a closer look at it again!")
            else: 
                # Handling invalid inputs
                print("Invalid input. Please try again.")
            
        return user_items

        




# Add your room instance here, similar to the example below:
pigeon_house = PigeonHouse("pigeon house", "An abandoned pigeon house.")
movieTheater_2ndFloor = MovieTheater_2ndFloor("movie theater",
                                              "You can see rows of seats facing a large screen."
                                              )
small_book_corner = SmallBookCorner("small book corner", "A cozy place to relax and study to.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    "pigeon_house": pigeon_house,
    "movieTheater_2ndFloor": movieTheater_2ndFloor,
    "small_book_corner": small_book_corner
}
