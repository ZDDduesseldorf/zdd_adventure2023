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
    



class BubbleteaShop(Room):

    #list of flavors for tea and boba

    list_boba = ["kiwi", "mango", "coffee"]
    list_tea = ["crazygrape", "tangomango", "limeblossom"]

    def run_story(self, user_items):
        print("You enter the Bubbletea Shop...\n",
              "In there is an old lady, a well-known face that was serving you in the Cafeteria before.\n",
              "She starts talking to you...\n\n\n",
              "Hey lovely, would you like to order a Bubbletea today?\n")

        # choice if user wants to order

        while True:
            input_choice = input("Type 'yes' if you want to order and 'no' if not: ")
            

            if input_choice == "no":
                print("\nWhat a pity! Come back if you change your mind!\n")
                return user_items

            elif input_choice == "yes":
                print("\n\nGreat, we have 3 types of tea and 3 types of boba!\n",
                      "What flavour would you like to have for your Tea?\n",
                      f"We have {', '.join(self.list_tea)}\n")

                # choice of tea

                while True:
                    input_choice_tea = input(f"Type one of: {', '.join(self.list_tea)}: ")

                    if input_choice_tea not in self.list_tea:
                        print("Invalid choice, try again")
                        continue
                    break
                
                # choice of boba

                print("\n\nThat is a nice choice. Now tell me, what boba do you want sweetheart\n",
                      f"\nWe have {', '.join(self.list_boba)}")

                while True:
                    input_choice_boba = input(f"\nType one of: {', '.join(self.list_boba)}: ")

                    if input_choice_boba not in self.list_boba:
                        print("Invalid choice, try again")
                        continue
                    break

                print(f"\n\nHere you go, enjoy your {input_choice_tea} Bubbletea with {input_choice_boba} boba!")
                print("Don't worry about paying, in the ZDD everything should be free *.* and dont forget your straw!")
                
                return user_items

                    
## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
bubbletea_shop = BubbleteaShop("bubbletea shop", "Cute little Bubbletea Shop at the ZDD.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "bubbletea_shop": bubbletea_shop
}
