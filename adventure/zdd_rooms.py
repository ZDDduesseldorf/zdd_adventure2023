"""This is to keep all special rooms of the ZDD."""
from main_classes  import Room, Item
from time import sleep

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
    def enter_room(self, user_items, command_handler):
        """Main method of Room class."""
        self.visited += 1
        print(40 * "-")

        # Run whatever happens in this room:
        user_items = self.run_story(user_items)

        while True:
            action = input(">> 'leave' to exit the room, 'inspect' to look around: ").lower()

            command_handler.handle_global_commands(action)
            if not command_handler.game.game_active:  # If game is not active anymore, break
                return user_items

            if action == "leave":
                print("You leave the room...")
                return user_items
            elif action == "inspect":
                user_items = self.show_items(user_items)

                print("\nDo you want to take a journey with the machine?\n\n"
                    "But beware, it might take you to a place you don't want to go. Think about it...\n"
                    )

                while True:
                    
                    input_ = input("If you still want to take a trip, type 'yes', otherwise 'no': ")
                                    
                    if input_ == "yes":
                        print("Are you ready!")
                        [print(x) or sleep(x)  for x in range(1, 4)]
                        print("Oh oh! You're about to exit the game. Goodbye!")
                        exit()
                        
                    elif input_ == "no":
                        break
            else:
                print("Invalid command!")
                        
    #This method is structured differently, because the player cannot take any items from this room               
    def run_story(self, user_items):
            print("\nThe room is filled with the soft glow of ambient lighting...\n"
                  "You notice rows of seats facing a massive screen."
                  )
            return user_items
   

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

teleportation_machine = Item("teleportation machine",
                             "A teleportation machine enables instant, random travel between locations in the game.",
                             movable=False
                             )

movieTheater_2ndFloor = MovieTheater_2ndFloor("movie theater",
                                              "You can see rows of seats facing a large screen.",
                                              teleportation_machine
                                              )


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "movieTheater_2ndFloor": movieTheater_2ndFloor
}
