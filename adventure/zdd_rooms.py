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

# Adding my new room: the vr_room and its functionalities aka its ITEM
class VrRoom(Room):
    def run_story(self, user_items):
        print("You walk into a really bright room, lightened up by purple LED lights all over the ceiling.\n"
              "You ask yourself if you should just turn around and leave, but something catches your attention..\n"
              "In the middle of the room, you find a station.\n"
              "Do you want to look at the station or turn around?")
        
        # First choice: Look at the station or leave
        while True:
            input_choice = input("Type 'look at station' to find out more or 'turn around' to leave the room.\n"
                                "What do you think you will do?: ")
            
            if input_choice == "turn around":
                # If User decides to leave the room
                print("You leave the room, it probably was the best choice to do..right?\n")
                break 

            elif input_choice == "look at station":
                # If User decides to look at the station (trigger for the next choice)
                print("You find yourself standing in the middle of the room, looking at a little station with a vr headset in it.\n"
                      "It doesn't really surprise you to find this here.. you wonder what it can do?")

                # Second choice: Putting the headset on or leaving it behind
                while True:
                    headset_choice = input("Type 'put it on' to use the headset or 'forget it' to leave the headset behind.\n"
                                           "What will your choice be?: ")
                    
                    if headset_choice == "forget it":
                        # If User decides to leave the headset behind
                        print("You think to yourself how dangerous that could be, putting an unknown vr headset on.\n"
                              "So obviously, the best decision is to forget about it and leave it behind.\n")
                        break

                    elif headset_choice == "put it on":
                        # If User decides to put the headset on (trigger for the DAISY-puzzle)
                        print("WOAH! EVERYTHING'S MOVING! EVERYTHING HAPPENS SO FAST.. various pictures are flashing in front of your eyes.\n"
                              "You start to feel a lot of pressure on your head and shortly after a clicking sound. All the pressure is suddenly gone.\n"
                              "'MUAHAHAHA!' - you hear an evil voice speaking through the headset - 'NOBODY CAN SOLVE MY MOST DIFFICULT RIDDLE AND ESCAPE, MUAHAHA!\n"
                              "Oh no! You realize you have been trapped by someone very evil, you try to take the headset off but it just wouldn't come off.. what now?\n"
                              "After some time, one picture is being displayed very clearly for you to look at.\n"
                              "You figured out what the picture is, it's supposed to be a puzzle. You ask yourself, if this was the riddle that the creepy voice told you about.\n"
                              "The text underneath the picture says 'If you solve this puzzle, you will be able to take the headset off and you will even be rewarded...'\n")
                        
                        # Puzzle Logic
                        puzzle_sequence = [4, 1, 9, 19, 25]
                        puzzle_word = "".join([chr(position + 64) for position in puzzle_sequence])

                        # Third choice: User needs to solve a puzzle
                        while True:
                            answer_choice = input(f"Type the correct word for the sequence {puzzle_sequence}:\n"
                                                  f"a) 'DAHSY'\n"
                                                  f"b) 'DAISY'\n"
                                                  f"c) 'DAISX'\n"
                                                  f"d) 'DASIY'\n"
                                                  "What is your choice?: ")

                            if answer_choice.lower() == 'b':
                                print("'NOOOOO HOW DID YOU SOLVE MY PUUZZLEEE-' you hear the creepy voice saying. The headset unlocks and you can take it off.")
                                break
                            else:
                                print("Incorrect answer. The headset is still locked. Try again.")
                        break 
                    else:
                        print("Invalid input. Try again.")

            # Exiting the first while loop
            break 


        # Last choice for the user_item input
        while True:
            last_choice = input("With this headset in your inventory, you are able to check various information such as the presence of other people in the building or other relevant details that could help you.\n"
                            "Do you want to keep the headset? Type 'yes' or 'no'.\n")
        
            if last_choice == "yes":
                # User decides to keep the headset (trigger for the Class Item)
                print("It might be helpful to keep this after all..\n")
                vr_headset = Item("vr headset", "A vr headset that allows the player to check various information about other people in the building, etc.", movable=True)
                user_items.append(vr_headset)
                break

            elif last_choice == "no":
                # User decides to leave it behind
                print("It's too risky, what if the headset is cursed and brings you bad luck? You're propably better off without it..")

            else:
                # Handling invalid inputs from the Player
                print("Invalid input. Please try again.")

        # Exiting the second loop after the puzzle
        return user_items 


toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
vr_room = VrRoom("vr_room", "You can see all those lights in the room, you wonder what it can be..")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "vr_room": vr_room 
}
