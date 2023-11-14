"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import random as random
#import random for a random soda

class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print(
                "While you wash your hands, the book slips out of your backpack ...right into the water."
            )
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            return [x for x in user_items if x.name != "old book"]
        return user_items

## ----------------------------------------------------------------
## List here all rooms

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

class HiddenLaboratory(Room):
    def run_story(self, user_items):
        print("Stepping through a heavy metal door, you enter a hidden laboratory.\n"
              "As you walk through the laboratory, you see another heavy door.\n"
              "Do you want to open it?\n"
              )
        while True:
            choice = input("yes / no: ")
            if choice == "yes":
                print("The room you entered is being faintly lit by old light bulbs in a greenish tint.\n"
                      "As you walk through the room you see some kind of ancient apparatus and unidentified substances.\n"
                      "You figure it must be an abandoned facility.\n"
                      "In a closet, you find some dusty chalkboards with incomplete formulas.\n"
                      "You need to complete these equations to move forward.\n")
                while True:
                    equation = input("1 + 2 = ")
                    if equation == "3":
                        print("Correct. Next Riddle.")
                        equation = input("8 - 2 = ")
                        if equation == "6":
                            print("Correct. You completed all the tasks.\n"
                                  "You are now able to enter the hidden room and see a mysterious glow under some debris.\n"
                                  "You take the mirror and as soon as you touch it, runes start to glow on the frame of the mirror.\n")
                            ethereal_mirror = Item("Ethereal Mirror", "A mirror with the ability to reveal hidden messages and clues.")
                            user_items.append(ethereal_mirror)
                            return user_items
                        else:
                            print("Wrong Answer. Please try again.")
                    else:
                        print("Wrong Answer. Please try again.")
    
            elif choice == "no":
                print("You don't open the second door and exit the laboratory shortly after.")
                break
            else:
                print("Please enter 'yes' or 'no'.")
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

def print_separator():
    print("-" * 50)  # Adjust the number of dashes as needed

# Adding my new room: the vr_room and its functionalities aka its ITEM
class VrRoom(Room):
    def run_story(self, user_items):
        print(
            "You walk into a really bright room, lightened up by purple LED lights all over the ceiling.\n"
            "You ask yourself if you should just turn around and leave, but something catches your attention..\n"
            "In the middle of the room, you find a station.\n"
            "Do you want to look at the station or turn around?"
        )

        # First choice: Look at the station or leave
        input_choice = input(
            "Type 'look at station' to find out more or 'turn around' to leave the room.\n"
            "What do you think you will do?: "
        )

        print_separator()

        if input_choice == "turn around":
            # If User decides to leave the room
            print("You leave the room; it probably was the best choice to do..right?\n")
            return user_items

        elif input_choice == "look at station":
            # If User decides to look at the station (trigger for the next choice)
            print(
                "You find yourself standing in the middle of the room, looking at a little station with a VR headset in it.\n"
                "It doesn't really surprise you to find this here; you wonder what it can do?"
            )

            # Second choice: Putting the headset on or leaving it behind
            headset_choice = input(
                "Type 'put it on' to use the headset or 'forget it' to leave the headset behind.\n"
                "What will your choice be?: "
            )

            print_separator()

            if headset_choice == "forget it":
                # If User decides to leave the headset behind
                print(
                    "You think to yourself how dangerous that could be, putting an unknown VR headset on.\n"
                    "So obviously, the best decision is to forget about it and leave it behind.\n"
                )
                
            elif headset_choice == "put it on":
                # If User decides to put the headset on (trigger for the DAISY-puzzle)
                print(
                    "WOAH! EVERYTHING'S MOVING! EVERYTHING HAPPENS SO FAST.. various pictures are flashing in front of your eyes.\n"
                    "You start to feel a lot of pressure on your head and shortly after a clicking sound. All the pressure is suddenly gone.\n"
                    "'MUAHAHAHA!' - you hear an evil voice speaking through the headset - 'NOBODY CAN SOLVE MY MOST DIFFICULT RIDDLE AND ESCAPE, MUAHAHA!\n"
                    "Oh no! You realize you have been trapped by someone very evil; you try to take the headset off but it just wouldn't come off.. what now?\n"
                    "After some time, one picture is being displayed very clearly for you to look at.\n"
                    "You figured out what the picture is; it's supposed to be a puzzle. You ask yourself if this was the riddle that the creepy voice told you about.\n"
                    "The text underneath the picture says 'If you solve this puzzle, you will be able to take the headset off and you will even be rewarded...'\n"
                )

                # Puzzle Logic
                puzzle_sequence = [4, 1, 9, 19, 25]
                puzzle_word = "".join([chr(position + 64) for position in puzzle_sequence])

                # Third choice: User needs to solve the puzzle
                answer_choice = input(
                    f"Type either a, b, c or d for the sequence {puzzle_sequence}:\n"
                    f"a) 'DAHSY'\n"
                    f"b) 'DAISY'\n"
                    f"c) 'DAISX'\n"
                    f"d) 'DASIY'\n"
                    "What is your choice?: "
                )
                
                print_separator()

                if answer_choice.lower() == "b":
                    print("'NOOOOO HOW DID YOU SOLVE MY PUUZZLEEE-' you hear the creepy voice saying. The headset unlocks, and you can take it off.")

                    # Last Choice: If User wants to keep the headset or not
                    last_choice = input(
                        "With this headset in your inventory, you can check various information such as the presence of other people in the building\n"
                        "or other relevant details that could help you.\n"
                        "Do you want to keep the headset? Type 'yes' or 'no'.\n"
                    )

                    if last_choice == "yes":
                        # User decides to keep the headset (trigger for the Class Item)
                        print("It might be helpful to keep this after all..\n")
                        vr_headset = Item(
                            "vr headset",
                            "A VR headset that allows the player to check various information about other people in the building, etc.",
                            movable=True,
                        )
                        user_items.append(vr_headset)

                    elif last_choice == "no":
                        # User decides to leave it behind
                        print("It's too risky; what if the headset is cursed and brings you bad luck? You're probably better off without it..")

                else:
                    print("Incorrect answer. The headset is still locked.")

            else:
                print("You used your last try.")

        else:
            print("Invalid input. Try again.")

        return user_items

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
# Add your room instance here, similar to the example below:
gym_first_floor = Gym("Gym on the first floor", "This is the new gym in the ZDD")
vr_room = VrRoom(
    "vr_room", "You can see all those lights in the room, you wonder what it can be.."
)
soda_machine = SodaMachine("soda","mysterious soda machine.")
pigeon_house = PigeonHouse("pigeon house", "An abandoned pigeon house.")
movieTheater_2ndFloor = MovieTheater_2ndFloor("movie theater",
                                              "You can see rows of seats facing a large screen."
                                              )
hidden_laboratory = HiddenLaboratory("hidden laboratory", "Secret lab for data science experiments.")
darkroom = DarkRoom("darkroom", "A mysterious darkroom with a surprise")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "gym_first_floor": gym_first_floor,
    "vr_room": vr_room,
    "soda_machine": soda_machine,
    "pigeon_house": pigeon_house,
    "movieTheater_2ndFloor": movieTheater_2ndFloor,
    "hidden_laboratory": hidden_laboratory,
    "dark_room": darkroom
}

