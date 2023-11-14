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
    
    
class CoffeeChamber(Room):
    
    list_coffee = ["Black", "Milk", "Latte Macchiato"]
    
    
    def run_story(self, user_items):
        print("Welcome to the ZDD Coffee Chamber where you get the best coffe within the whole campus. \n(Inner thoughts) When you walk into the chamber you see a small but cozy little room with some realxing seatting arragements.")
        print("As you walk in, a friendly voice starts speaking to you.\n")
        print("She ask you what you would like to order?\n")
        
        
        while True:
            
            input_choice = input("Type 'yes' if you want to order and 'no' if not: ")

            if input_choice == "no":
                print("\nWhat a pity! Come back if you change your mind!\n")
                return user_items
            
            elif input_choice == "yes":
                print("\n\nGreat, how would you like your coffee?" f"\nWe have {','.join(self.list_coffee)} coffee. \n\n")
                
                user_choice = input("How would you like your coffee? ")
                
                if user_choice == "Black": 
                
                    print(f"Here you go, enjoy your {user_choice} coffee, till next time.")
                    print("Since coffee is an esstential for people working in this industry, you dont have to pay anything!")
                    Cup_of_coffee_black = Item("Cup of strong black coffee","Cup of Coffee", movable=True)
                    user_items.append(Cup_of_coffee_black)
                    
                elif user_choice == "Milk":
                    
                    print(f"Here you go, enjoy your {user_choice} coffee, till next time.")
                    print("Since coffee is an esstential for people working in this industry, you dont have to pay anything!")
                    
                    Cup_of_coffee_milk = Item("Cup of milk coffee","Cup of Coffee", movable=True)
                    user_items.append(Cup_of_coffee_milk)
                    
                else:
                    
                    print(f"Here you go, enjoy your {user_choice} coffee, till next time.")
                    print("Since coffee is an esstential for people working in this industry, you dont have to pay anything!")

                    Cup_of_coffee_LM = Item("Cup of strong Latte Macchiato","Cup of Coffee", movable=True)
                    user_items.append(Cup_of_coffee_LM)
                    
            return user_items
                         
## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
coffee_chamber = CoffeeChamber("Coffee Chamber", "An little cozy coffee chamber within the ZDD.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "coffee_chamber": coffee_chamber
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
