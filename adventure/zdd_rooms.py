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

    list_boba = ["kiwi", "mango", "coffee"]
    list_tea = ["crazygrape", "tangomango", "limeblossom"]

    def run_story(self, user_items):
        print("You enter the Bubbletea Shop and its incredibly cute\n",
              "In there is an old lady, a well-known face that was serving in the Cafeteria before.\n",
              "She starts talking to you...\n\n",
              "Hey lovely, would you like to order a Bubbletea today?\n")

        while True:
            input_choice = input("Type 'yes' if you want to order and 'no' if not: ")

            if input_choice == "no":
                print("What a pity! Come back if you change your mind!\n")
                return user_items

            elif input_choice == "yes":
                print("Great, we have 3 types of tea and 3 types of boba!\n",
                      "What flavour would you like to have for your Tea?\n",
                      "We have Crazy-Grape, Tango-Mango and Lime-Blossom\n")

                input_choice_tea = input("Type 'crazygrape','tangomango' or 'limeblossom': ")

                if input_choice_tea not in self.list_tea:
                    print("Invalid choice, try again")
                    continue

                print(f"{input_choice_tea} is an interesting choice. Now tell me, what boba do you want \n",
                      "We have Coffee, Kiwi, and Mango")

                input_choice_boba = input("Type 'coffee', 'kiwi', or 'mango': ")

                if input_choice_boba not in self.list_boba:
                    print("Invalid choice, try again")
                    continue

                print(f"Here you go, enjoy your {input_choice_tea} tea with {input_choice_boba}!")
                
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
