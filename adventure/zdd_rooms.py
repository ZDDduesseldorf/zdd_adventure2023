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
      
# CoffeeChamber class inherits from the Room class
class CoffeeChamber(Room):

    # List of available coffee types in the CoffeeChamber
    list_coffee = ["Black", "Milk", "Latte Macchiato"]

    # Method to run the story in the coffee chamber
    def run_story(self, user_items):

        # Welcome message for the CoffeeChamber
        print("Welcome to the ZDD Coffee Chamber where you get the best coffee within the whole campus.")
        print("(Inner thoughts) When you walk into the chamber you see a small but cozy little room with some relaxing seating arrangements.")
        print("As you walk in, a friendly voice starts speaking to you.")
        print("She asks you what you would like to order?\n")

        # Infinite loop for ordering
        while True:

            # User is asked if they want to order
            input_choice = input("Type 'yes' if you want to order and 'no' if not: ")

            # If the user enters 'no', exit the loop
            if input_choice == "no":
                print("\nWhat a pity! Come back if you change your mind!\n")
                return user_items

            # If the user enters 'yes', ask for coffee choice
            elif input_choice == "yes":
                print(f"\n\nGreat, how would you like your coffee? We have {','.join(self.list_coffee)} coffee.\n")

                # User enters their desired coffee type
                user_choice = input("How would you like your coffee? ")

                # Depending on the user's choice, perform different actions
                if user_choice == "Black":
                    print(f"Here you go, enjoy your {user_choice} coffee, till next time.")
                    print("Since coffee is essential for people working in this industry, you don't have to pay anything!")
                    # Create a new item (Cup_of_coffee_black) and add it to the user_items list
                    Cup_of_coffee_black = Item("Cup of strong black coffee", "Cup of Coffee", movable=True)
                    user_items.append(Cup_of_coffee_black)

                elif user_choice == "Milk":
                    print(f"Here you go, enjoy your {user_choice} coffee, till next time.")
                    print("Since coffee is essential for people working in this industry, you don't have to pay anything!")
                    # Create a new item (Cup_of_coffee_milk) and add it to the user_items list
                    Cup_of_coffee_milk = Item("Cup of milk coffee", "Cup of Coffee", movable=True)
                    user_items.append(Cup_of_coffee_milk)

                else:
                    print(f"Here you go, enjoy your {user_choice} coffee, till next time.")
                    print("Since coffee is essential for people working in this industry, you don't have to pay anything!")
                    # Create a new item (Cup_of_coffee_LM) and add it to the user_items list
                    Cup_of_coffee_LM = Item("Cup of strong Latte Macchiato", "Cup of Coffee", movable=True)
                    user_items.append(Cup_of_coffee_LM)

        # Return the user_items list (this statement should be outside the loop)
        return user_items


toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")




toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
# Add your room instance here, similar to the example below:
soda_machine = SodaMachine("soda","mysterious soda machine.")
pigeon_house = PigeonHouse("pigeon house", "An abandoned pigeon house.")
movieTheater_2ndFloor = MovieTheater_2ndFloor("movie theater","You can see rows of seats facing a large screen.")
coffee_chamber = CoffeeChamber("Coffee Chamber", "An little cozy coffee chamber within the ZDD.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "soda_machine": soda_machine,
    "pigeon_house": pigeon_house,
    "movieTheater_2ndFloor": movieTheater_2ndFloor,
    "coffee_chamber": coffee_chamber
}
