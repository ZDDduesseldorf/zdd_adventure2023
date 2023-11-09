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

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


class KitchenFirstFloor(Room):
    def enter_room(self, user_items, command_handler):
        """Main method of Room class."""
        self.visited += 1
        print(40 * "-")

        while True:
            action = input(">> 'leave' to exit the room, 'inspect' to look around: ").lower()

            command_handler.handle_global_commands(action)
            if not command_handler.game.game_active:  # If game is not active anymore, break
                return user_items
            if action == "leave":
                print("You leave the room...")
                return user_items
            elif action == "inspect":
                # Show items to collect and fridge
                user_items = self.show_items(user_items)
                print("The fridge... \nWould you like to take a look inside?")
                while action != "no":
                    action = input(">> Enter 'no' to go back or 'look inside' to take a look: ").lower()
                    if action == "look inside":
                        # Start kitchen-story
                        user_items = self.run_story(user_items)
                    elif action != "no":
                        print("Invalid command!")
            else:
                print("Invalid command!")
    
    def run_story(self, user_items):
        print("You open the fridge and look inside...")

        # Check if the fridge elements not already exist (to keep track what already has been removed from it)
        ingredients = ["eggs", "pasta", "rice", "bread", "ice cream"]
        if not hasattr(self, 'ingredients_objects'):
            self.ingredients_objects = []

            for ingredient in ingredients:
                item_object = Item(ingredient, f"Just {ingredient}.", movable=True)
                self.ingredients_objects.append(item_object)
        
        # Save items (not in inventory) before, that they can be used again afterwards
        old_self_items = self.items
        self.items = self.ingredients_objects

        user_items = self.show_items(user_items)

        # Save which items are in inventory already
        self.ingredients_objects = self.items

        # Recover old items (not in inventory)
        self.items = old_self_items

        # Allow the user to choose an item to eat from ingredients_objects
        while True:
            # Check if there are edible items from the fridge in the user_items
            edible_items = [food for food in ingredients if food in [item.name for item in user_items]]
            
            if not edible_items:
                print("There are no edible items in your inventory anymore.")
                break

            print("What would you like to eat? Enter the item name or 'not hungry' to finish eating.")
            choice = input(">> ").lower()

            if choice == 'not hungry':
                break

            # Check if the choosen item is edible and in the inventory
            if choice in edible_items and choice in [item.name for item in user_items]:
                for item in user_items:
                    if item.name == choice:
                        #Remove item
                        user_items.remove(item)
                        print(f"You ate the {choice}.")
                        break
            else:
                print("Invalid choice! Please select an edible item from the fridge.")
                # Show remaining items to eat
                edible_items_in_inventory = ', '.join(edible_items)
                print("Edible items from the fridge in your inventory: ", edible_items_in_inventory)          
        return user_items
    

rice_recipe = Item("rice recipe", "A recipe for delicious rice dishes.", movable=True)
pasta_recipe = Item("pasta recipe", "A recipe for mouth-watering pasta.", movable=True)
bread_recipe = Item("bread recipe", "A recipe for freshly baked bread." , movable=True)
icecream_recipe = Item("icecream recipe", "A recipe for creamy ice cream.", movable=True)
fridge = Item("fridge", "A large fridge with various ingredients.", movable=False)
kitchen_first_floor = KitchenFirstFloor("kitchen", "Wondrous aromas, bubbling pots, a feast of flavors.", [
                            rice_recipe, pasta_recipe, bread_recipe, icecream_recipe, fridge])


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "kitchen_first_floor": kitchen_first_floor
}
