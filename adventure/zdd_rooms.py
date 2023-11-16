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
        self.user_items = user_items
        
        # Introduction and initial choices
        print("You walk towards the noise ..... \n"
                    "There is a sign 'please wait outside'\n")
             

        #First Choice: wait for somebody to show up or just walk in
        action = input("Do you want to wait or explore what is behind that door?\n"
                       "type 'wait' to keep waiting or 'explore' to enter the room:\n").lower()
        
        if action == "wait":
            print("hmmmmmm... nobody is coming, it sounds like music is playing in there tho")
            action = input("Do you want to keep waiting?\n"
                                "type 'wait' to keep waiting or 'leave' to leave.: \n").lower()

            #Seond Choice: keep waiting or leaving the room
            if action == "wait": 
                print("\n\nSECURITY GUARD: 'Oh sorry didn't see you there. You can go in if you want.")

                #Third Choice: taking the item stamp card 
                action = input("Ouh here take the stampcard!\n"
                                    "Do you accept the card? type 'yes' or 'no':\n").lower()
                    
                if action == "yes":
                 # add the stampcard to the inventory
                     club_stampcard = Item("stamp card", "a card used to buy drinks and snacks inside the club", movable=True)
                     user_items.append(club_stampcard)
                     print("\n\n###You picked up the Item 'stamp card' ###\n\n")
                     
                     print("\n\nYou enter the room")
                 
                     #setting card to true
                     self.bar_story(False, True)
                     
                elif action == "no":
                    print("SECURITY GUARD:'Nahhh you have to, can't get any drinks without one'\n\n")

                    club_stapmcard = Item("stamp card", "a card used to buy drinks and snacks inside the club", movable=True)
                    user_items.append(club_stampcard)
                    print("\n\n###You picked up the Item 'stamp card' ###\n\n")

                    print("You enter the club\n\n")
                    
                    #setting card to true
                    self.bar_story(False, True)
                    
                else:
                    print("Invalid Input")
                    
            elif action == "leave":
                return user_items
                
        #user decides to walk in and not wait
        elif action == "explore":
            
            print("You try to enter the club\n\n")
            print("SECURITY GUARD: WOAAHH STOP\n"
                  "Can't you read, it says right here 'please wait outside'\n"
                  "....\n"
                  "Come on show me your HSD-Card!\n\n")
            
            #Sedcurity Guard asks for ur ID
            action = input("Do you want to show them your HSD Card?\n (yes/no):\n\n").lower()
            if action == "yes":
                print("Luckily you got one last semester.\n\n")
                print("SECURITY GUARD:'Alright get in....'\n")
                
                #user did not get the stamp card in this story line
                card = False
                
                self.bar_story(False, False)
                
                
            elif action == "no":
                #user does not want to show card, results in not being let in --> leave room
                print("SECURITY GUARD:'Cant let you in without one'\n\n SECURITY GUARD:'have a nice day.'")
                return user_items
                #break
            else:
                print("Invalid Input")
           
        else:
            print("Invalid Input")
               
            action = input("\n Do you want to restart the story or leave the room?\n (restart/leave):").lower()
               
            if action == "restart":
                #story begins at the start
                self.run_story()
            else:
                #end the story and give possibility to leave the room
                return user_items
            
                   
           
       
    def bar_story(self, drink = False, card = True):
        
           
        print("\n\nHmmm ... seems like nobody is here.\n"
                  "Maybe there is someone at the bar?\n"
                  "...\n"
                  "...\n"
                 "BARTENDER:'Good day, would you like something to drink?'" )
            
        action = input("type 'yes' to get a drink, type 'no' to stay clean:").lower()
        
        #user decides to get a drink
        if action == "yes":
            #check if stamp card in inventory
            if "stamp card" in [x.name for x in self.user_items]:
                print("You give the bartender your stamp card")
                print("BARTENDER:'all right'\n"
                     "BARTENDER *mumbling*: 'Are they even 18?'\n 'ahhh I dont get paid enough to bother'\n"
                     "...\n"
                     "Here you go, enjoy it, get lit!")
                
                #drink gets added to the inventory
                club_drink = Item("drink", "the drink you got at the bar inside the club", movable=True)
                self.user_items.append(club_drink)
                print("\n\n###You picked up the Item 'drink' ###\n\n")
                
                self.explore_club()
              
                action = ("Do you want to stay at the bar?\n (yes/no):\n")
                if action == "yes":
                    action = input("Do you want to get another drink?\n(yes/no):")
                    
                    if action == "yes":
                        if "drink" in [x.name for x in self.user_items]:
                        
                            print("BARTENDER: 'You have to finish the one you got earlier first'")
                     
                            self.explore_club()
                    
                    elif action == "no":
                      
                        self.explore_club()
            else:
                print("BARTENDER:'Sorry I cant sell you anything without a stampacard, maybe try getting one at the entrance'")
                drink = False
              
                self.explore_club()
              
        elif action == "no":
            print("BARTENDER:'ouh man I am going to get fired for sure'")
          
            action = ("Do you want to stay at the bar?\n (yes/no):\n")
            if action == "yes":
                if "stamp card" not in [x.name for x in self.user_items]:
                    print("BARTENDER: 'Still no stamp card huh?'")
                  
                    self.explore_club()
                 
                elif "stamp card" in [x.name for x in self.user_items]:
                    print("BARTENDER: 'Ahh you made it, just wait a second.'\n"
                        "...\n"
                        "BARTENDER: 'Here you go.'\n")
                    
                    club_drink = Item("drink", "the drink you got at the bar inside the club", movable=True)
                    self.user_items.append(club_drink)
                    print("\n\n###You picked up the Item 'drink' ###\n\n")
                     
                    self.explore_club()
            else:
                self.explore_club()
                
                
    def explore_club(self):
        print("\n\n You look around...\n\n")
        
        print("Where is the DJ?\n\n")
        
        action = input("Would you like to go to the DJ-Desk?\n (yes/no):")
        
        if action == "yes":
            print("\n\n You go to the desk...\n\n"
                  "hmmmm the Laptop is unlocked ...\n\n"
                  "YOU: 'Club-playlist 2023???,\n no wunder no one wants to be here")
            
            action = input("Would you like to play another Playlist?\n (yes/no):").lower()
            
            if action == "yes":
                print("Seems like its the only playlist on the laptop...\n\n"
                      "###TIP: ASK THE OTHER STAFF ABOUT THE MUSIC###")
                
                self.searchformusic()
                
            elif action == "no":
                return
            
        elif action == "no":
            action = input("So you want to leave the Club?\n(yes/no):")
            if action == "yes":
                return
            elif action == "no":
                print("You go to the DJ-Desk, there isnt anything to do else")
                self.searchformusic()
                    
    def searchformusic(self):
        action = input("Would you like to ask the security guard or the barkeeper?\n (security guard/barkeeper):").lower()
        
        
        #user wants to ask the barkeeper about the music
        if action == "barkeeper":
            print("BARKEEPER: 'Oh you want another drink?'\n\n"
                  "YOU:'No thanks, but whats going on with the music?'\n\n"
                  "BARKEEPER: 'I dont know, havent seen the DJ for quite some time now'\n\n But they left this here, do you need it?\n\n"
                  "YOU:'Sure, do you mind if I put something else on?'\n\n"
                  "BARKEEPER: 'I dont really care to be honest.'")
            
            #usb_stick = True
            #Add the usb stick to the inventory
            club_usb_stick = Item("usb stick", "the stick you got from the barkeeper at the club", movable=True)
            self.user_items.append(club_usb_stick)
            print("\n\n###You picked up the Item 'usb stick' ###\n\n")
            
            print("You go back to the laptop...\n\n")
            
            while True:
                action = input("Would you like to plug in the usb stick?\n (yes/no):").lower()
                
                if action == "yes":
                    #remove the usb stick from inventory
                    
                    
                    print("the random noises turned into music")
                    print("♫♫♫     ♫♫♫     ♫♫♫    ♫♫♫    ♫♫♫\n\n")
                    
                    print("You take the random glow stick laying next to the laptop to lighten up the mood .... your own mood...\n\n")
                    #add glowstick item here

                    club_glow_stick = Item("glow stick", "the glow stick you found at the club and used to dance", movable=True)
                    self.user_items.append(club_glow_stick)
                    print("\n\n###You picked up the Item 'glow stick' ###\n\n")
                    print("♫♫♫     ♫♫♫     ♫♫♫    ♫♫♫    ♫♫♫")
                    return [x for x in self.user_items if x.name != "usb stick"]
                  
                
                #did not want to plug it in, has to anyway
                elif action == "no":
                    print("Why did you get it then?\n\n")
                    
                     
        #user wants to ask the security guard about the music
        elif action == "security guard":#user wont get the usb_stick in this story line
            print("SECURITY GUARD: 'Already going?'\n\n"
                  "YOU:'No i just wanted to ask if you know where the DJ is at,?'\n\n"
                  "SECURITY GUARD: 'HAHAHHAHA, yeah I do.\n\n.....\n\n"
                  "YOU:'And?'\n\n"
                  "SECURITY GUARD: 'And what?'\n\n"
                  "YOU:'Where are they?'\n\n"
                  "SECURITY GUARD: 'Ouh hahaha, I am the DJ! \n\tDo you like my set?'\n\n"
                  "YOU:'Ouh.... yeah.... sure'\n\n")
            
            
            
            print("YOU: 'What a weird club'\n\nyou leave the club")
            return
            
            
                



                        
   
#club_stampcard = Item("stamp card", "a card used to buy drinks and snacks inside the club", movable=True)

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
techno_club = TechnoClub("Club", "Nobody knows who's idea the club was.")



ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
   "techno_club": techno_club}
   
