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
class TechnoClub(Room):
    def run_story(self, user_items):
       # Introduction and initial choices
       print("You walk towards the noise ..... \n"
                    "There is a sign 'please wait outside'\n")
             

       # First Choice: Open or Don't Open the Window
       while True:
           action = input("Do you want to wait or explore what is behind that door?\n"
                        "type 'wait' to keep waiting or 'explore' to enter the room").lower()
                
           if action == "wait":
               print("hmmmmmm... nobody is coming, it sounds like music is playing in there tho")
               action = input("Do you want to keep waiting?\n"
                                   "type 'wait' to keep waiting or 'explore' to enter the room.").lower()
               if action == "wait": 
                   print("SECURITY GUARD: 'Oh sorry didn't see you there. You can go in if you want.")

                       #club_stapmcard = Item("stamp card", "a card used to buy drinks and snacks inside the club", movable=True)
                   action = input("Ouh here take the stampcard!\n"
                                       "Do you accept the card? type 'yes' or 'no'").lower()
                       
                   if action == "yes":
                    # add the stampcard to the inventory
                    #Item.user_items.append(club_stapmcard)

                        print("You enter the room")
                    
                        card = True
                  
                   elif action == "no":
                       print("SECURITY GUARD:'Nahhh you have to, can't get any drinks without one'")
                    
                       card = True
                   else:
                       print("Invalid Input")
                           
           elif action == "explore":
               # Outcome: User decides not to open the window
               print("You go in")
               print("SECURITY GUARD: WOAAHH STOP\n"
                     "Can't you read, it says right here 'please wait outside'\n"
                     "....\n"
                     "Come on show me your HSD-Card!\n\n")
               
               action = input("Do you want to show them your HSD Card?\n (yes/no):").lower()
               if action == "yes":
                   print("Luckily you got one last semester.")
                   print("SECURITY GUARD:'Alright get in....'\n")
                   
                   card = False
               elif action == "no":
                   print("SECURITY GUARD:'Cant let you in without one'\n\n SECURITY GUARD:'have a nice day.'")
                   return 
                   break
               else:
                   print("Invalid Input")
           #elif action == "exit":
            #   action = "leave"
           else:
               print("Invalid Input")
               #return
           #break
       
       while True:
           print("Hmmm ... seems like nobody is here.\n"
                  "Maybe there is someone at the bar?\n"
                  "...\n"
                  "...\n"
                 "BARTENDER:'Good day, would you like something to drink?'" )
            
           action == input("type 'yes' to get a drink, type 'no' to stay clean:").lower()
            
           if action == "yes":
               #check if stamp card in inventory
               #if "stamp card" in [x.name for x in user_items]:
                if card == True:
                   print("You give the bartender your stamp card")
                   print("BARTENDER:'all right'\n"
                       "BARTENDER *mumbling*: 'Are they even 18?'\n 'ahhh I dont get paid enough to bother'\n"
                       "...\n"
                       "Here you go, enjoy it, get lit!")
                   drink = True
                   #club_drink = Item("drink", "the drink you got at the bar", movable=True)
                   #Item.user_items.append(club_drink)
                else:
                  print("BARTENDER:'Sorry I cant sell you anything without a stampacard, maybe try getting one at the entrance'")
                  drink = False
                  break
              
           elif action == "no":
                print("BARTENDER:'ouh man I am going to get fired for sure'")
                break
               
              
           else:
               # Handling invalid inputs
               print("Invalid input. Please try again.")

           break  # Exiting the first while loop
           
       action = ("Do you want to stay at the bar?\n (yes/no):\n")
       while action == "yes":
           if drink == True:
               print("BARTENDER: 'You have to finish the one you got earlier first'")
               break
           else:
               if card == False:
                   print("BARTENDER: 'Still no stamp card huh?'")
                   break
               elif card == True:
                   print("BARTENDER: 'Ahh you made it, just wait a second.'\n"
                         "...\n"
                         "BARTENDER: 'Here you go.'\n")
                   break
        
"""
       # Third Choice: Ask the pigeon to be a companion
       while True:
           choice = input("Do you want to ask the pigeon to be your companion? (yes/no): ")
           if choice == "yes":
               # Outcome: User decides to make the pigeon their companion
               print("It answers 'gurrr!' which (of course) means yes, so you put it into your bag.")
               break
           elif choice == "no":
               # Outcome: User decides not to make the pigeon their companion
               print("The pigeon looks at you with its big round eyes and says 'gurrr!'. Maybe you should think about it again.")
           else: 
               # Handling invalid inputs
               print("Invalid input. Please try again.")

       return user_items
        #def enter_room(self, user_items, command_handler):
            """
"""
    print("You walk towards the noise ..... \n"
            "There is a sign 'please wait outside'\n")

    action = input("Do you want to wait or explore what is behind that door?\n"
            "type 'wait' to keep waiting or 'explore' to enter the room:\n").lower()
    
    if action == "wait":
        print("\n\nhmmmmmm.... nobody is coming, it sounds like music is playing in there tho\n\n")
        action = input("Do you want to keep waiting?\n"
                        "type 'wait' to keep waiting or 'explore' to enter the room.:\n").lower()
        if action == "wait":
            print("SECURITY GUARD: 'Oh sorry didn't see you there. You can go in if you want.\n\n")

            
            action = input("Ouh here take the stampcard!\n"
                            "Do you accept the card? (yes/no):\n").lower()
            if action == "yes":

                # add the stampcard to the inventory
                user_items.append(club_stapmcard)

                print("\nYou enter the room\n")

                #start the story inside of the room
                #self.run_story()
            
            elif action == "no":
                pass
                #self.run_story()
            else:
                print("Invalid input")
            
        elif action == "explore":
                pass
                #self.run_story()
            
    elif action != "explore":
        #start the story inside of the room
       print("Invalid command!")
        #self.run_story()

    else:
        """

"""def run_story(self, user_items):
        print("Hmmm ... seems like nobody is here.\n"
            "Maybe there is someone at the bar?\n"
            "...\n"
            "...\n"
            "BARTENDER:'Good day, would you like something to drink?'\n\n" )
        
        action = input("type 'yes' to get a drink, type 'no' to stay clean:\n").lower()

        if action == "yes":
            #check if stamp card in inventory
            if "stamp card" in [x.name for x in user_items]:
                print("You give the bartender your card")
                print("BARTENDER:'all right'\n"
                    "BARTENDER *mumbling*: 'Are they even 18?'\n 'ahhh I dont get paid enough to bother'\n"
                    "...\n"
                    "Here you go, enjoy it, get lit!\n\n")
                club_drink = Item("drink", "the drink you got at the bar", movable=True)
                user_items.append(club_drink)
            else:
                print("BARTENDER:'Sorry I cant sell you anything without a stampacard, maybe try getting one at the entrance'\n\n")

            
        elif action == "no":
            print("BARTENDER:'ouh man I am going to get fired for sure'\n\n")
        
        else:
            print("Invalid Input")

        print("That was kind of weird\n\n")
        print("You can take further looks, maybe you will find something interesting\n")
        action == input("type 'explore' to explore the disco, 'stay' to stay at the bar or 'leave' to leave the room.:\n").lower()

        while action == "stay":
            if "drink" in [x.name for x in user_items]:
                print("BARTENDER: 'Finish the one you got earlier first'\n")
                
            else:
                print("BARTENDER: 'Still no stamp card huh?'\n\n")

            print("You can try to find something more interesting")
            action == input("type 'explore' to explore the disco, 'stay' to stay at the bar or 'leave' to leave the room:\n").lower()
        
        print("you leave the room")


        return user_items

                        
   
club_stapmcard = Item("stamp card", "a card used to buy drinks and snacks inside the club", movable=True)
"""
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
techno_club = TechnoClub("Club", "Nobody knows who's idea the club was.")
#pigeon_house = TechnoClub("pigeon house", "An abandoned pigeon house.")



ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
   "techno_club": techno_club}
  #"pigeon_house": pigeon_house,
   