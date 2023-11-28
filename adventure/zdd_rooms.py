"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
from time import sleep
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

#issue9and10: game room & trophy, for context: it's Rick & Morty themed
class GameRoom(Room):
    def run_story(self, user_items):
        print("Blinking, flashing lights at the end of the room. It comes from one weirdly shaped, wobbly game machine.\n",
                "You walk up there as the rest of the room is dark and empty.\n",
                "you slowly touch the machine and it it... ew. slimey. what the fuck.\n",
                "suddenly the machine starts talking to you in an annoying, slightly whiney voice:\n\n",
                "'HEY! hey hey hey noooo you won't leave me pleaaaase' it gets aggressive... 'NO YOU STAY.'\n",
                "You can hear the door locking behind you. You look behind, then, a little afraid, back to the machine...")
        startgame = GameRoom_game()
        startgame.play_gamemachine(0)
        print(f"\n\n\ntotal won games in this stay: {startgame.won_game}\n\n\n")
        if startgame.won_game > 0:
            print(f"'you won?? wow. Your reward iiiissss.....'\n\n",
                    "'a PLUMBUS!!! Nice, everyone needs that. Nothing wrong with plumbuses in your house. Or bag.' \n",
                    "'In fact, it's great. Wouldn't prefer any other gift!! I mean, in my opinion.'\n\n",
                    "uhm.. who was that talking? Do you know, npc-player34019? Uhm i meant '{'34019_name'}'? No?\n",
                    "Yeah Idc just go away now..")
            plumbus = Item("Plumbus", "It's a plumbus. Everyone needs plumbuses.", movable=True)
            user_items.append(plumbus)
        elif startgame.won_game == 0:
            print("'Wow okay you didn't win the fucking plumbus? whack as hell, wo:man.'\n",
                    "'I mean, what are you gonna do now? Everyone needs a Plumbus!! Shit.'\n",
                    "'I would take a mind-clearing walk and try again. But it's up to you, if you wanna die..'\n",
                    "Ok, well. Idk who that was. Don't worry, i guess..")
        else:
            print("something went wrong..")
        return user_items
    

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

                    club_stampcard = Item("stamp card", "a card used to buy drinks and snacks inside the club", movable=True)
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
            #user will not get the stamp card in this story line
            action = input("Do you want to show them your HSD Card?\n (yes/no):\n\n").lower()
            if action == "yes":
                print("Luckily you got one last semester.\n\n")
                print("SECURITY GUARD:'Alright get in....'\n")
                
                
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
                self.run_story(user_items)
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
        while True:
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
                
                
            else:
                print("\nInavalid input, try again!")
                True
                
            
            
            
                



                        
   
#club_stampcard = Item("stamp card", "a card used to buy drinks and snacks inside the club", movable=True)

class BubbleteaShop(Room):

    # List of flavors for tea and boba
    list_boba = ["kiwi", "mango", "coffee"]
    list_tea = ["crazygrape", "tangomango", "limeblossom"]

    def run_story(self, user_items):
        print("You enter the Bubbletea Shop...\n",
              "In there is an old lady, a well-known face that was serving you in the Cafeteria before.\n",
              "She starts talking to you...\n\n\n",
              "Hey lovely, would you like to order a Bubbletea today?\n")

        # Choice if user wants to order
        while True:
            input_choice = input("Type 'yes' if you want to order and 'no' if not: ")

            if input_choice == "no":
                print("\nWhat a pity! Come back if you change your mind!\n")
                return user_items

            elif input_choice == "yes":
                print("\n\nGreat, we have 3 types of tea and 3 types of boba!\n",
                      "What flavour would you like to have for your Tea?\n",
                      f"We have {', '.join(self.list_tea)}\n")

                # Choice of tea
                while True:
                    input_choice_tea = input(f"Type one of: {', '.join(self.list_tea)}: ")

                    if input_choice_tea not in self.list_tea:
                        print("Invalid choice, try again")
                        continue
                    break
                
                # Choice of boba
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

                # Create item and add it to items
                bubbletea = Item(f"{input_choice_tea}-Bubbletea", f"{input_choice_tea} flavour Bubbletea with {input_choice_boba}", movable=True)
                user_items.append(bubbletea)
                print("\n-Bubbletea added to your inventory successfully-\n")

                return user_items
              
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

class SmallBookCorner(Room):
    def run_story(self, user_items):
        # Introduction and initial choice
        print("As you walk along the floor, you find a small, comfy looking place just around the corner.\n"
              "There are bookshelves along the walls, two couches with a lot of pillows and a working desk surrounded by two chairs.\n"
              "Someone has seemingly forgotten their Laptop on the desk. They must have left in a hurry, the Laptop is still emitting light of the screensaver.\n"
              "Do you want to take a closer look at it?")
        
        #First Choice: Inspect or don't inspect the open Laptop
        while True:
            choice = input("Type 'inspect laptop' or 'do not inspect laptop'\n"
                           "What do you want to do?: ")
            if choice == "inspect laptop":
                # Outcome: User chooses to inspect the glowing Laptop
                print("The 3D Animation of pipes is giving you whiplash to the early 2000s. The person who was working here seems to be quite old.\n"
                      "The Screensaver stops as you touch the keypad. The dreaded words of 'Please enter your password' appear")
                
            elif choice == "do not inspect laptop":
                # Outcome: User decides to not inspect the open Laptop
                print("You decide to not inspect the Laptop. Data protection and safety is a big concern to you.\n"
                      "Instead your view is trailing towards the bookshelves. Do you want to see what kind of books are stored there?")
                
                # Second Choice: Inspect the Books or don't inspect the Books
                while True:
                    inspect_choice = input("Type 'inspect books' or 'do not inspect books'\n"
                                           "What do you want to do?: ")
                    if inspect_choice == "inspect books":
                        # Outcome: User decides to inspect the books
                        print("You inspect the books. They range from varying topics, which none are really that much of an interest to you.\n"
                              "One Book seems to have been put back in a hurry, it's nearly falling from the shelf.\n"
                              "There seems to be a piece of paper hanging on by a thread, nearly falling out of the pages.\n"
                              "There seems to be something written on that piece of paper.")
                        break
                    elif inspect_choice == "do not inspect books":
                        # Outcome: User decides not to inspect the books
                        print("Books? Nah, are you what, like 80 years old? They don't even have an Ebook-Reader laying around here.\n"
                              "As you turn away from the Bookshelves, you hit your head on a badly placed book, and it falls to the floor.\n"
                              "A single piece of paper caught your attention, laying directly next to the fallen book.\n"
                              "There seems to be something written on that piece of paper.")
                        break
                    else:
                        # Handling invalid inputs
                        print("Invalid input. Please try again.")
            else:
                # Handling invalid inputs
                print("Invalid input. Please try again.")
            
            break  # Exiting the first while loop

        # Third Choice: Inspect the paper or don't inspect it
        while True:
            choice = input("Do you want to take a closer look at the written note? (yes/no): ")
            if choice == "yes":
                # Outcome: User decides to take a closer look at the written note
                print("There is a 4 digit code on that piece of paper.... You ask yourself, if someone could really be that stupid.\n"
                      "Your nosiness gets the better of you. You take the piece of paper and walk towards the Laptop.\n"
                      "Do you want to try and enter the 4 digit code as the password?")
                
                # Fourth Choice: Want to steal a Laptop baby?
                while True:
                    hacking_choice = input("Type 'enter code' or 'do not enter code'\n"
                                           "What do you want to do?: ")
                    if hacking_choice == "enter code":
                        # Outcome: User decides to enter Code and take the Laptop with them
                        print("Geez. It actually worked. You are in. An adrenaline rush is flowing through your system.\n"
                              "You are the Hacker non gender defined Person of the Year. You pat yourself on the shoulder after the Hard Work.\n"
                              "You decide to take the Laptop with you, may come in handy or you may find the Person it originally belonged to.\n"
                              "But now its yours. YOURS!!")
                        laptop = Item("laptop", "There's no Internet connection, but it's YOURS!", movable=True)
                        user_items.append(laptop)
                        break
                    elif hacking_choice == "do not enter code":
                        # Outcome: User decides not to be a bad person and doesn't steal the Laptop
                        print("You are making your way to the Laptop, but with each step your conscience is getting heavier and heavier.\n"
                              "You really want to. But no, you shouldn't. But what if....? No, it wouldn't be right.\n"
                              "You are torn. You might want to think about this again a bit longer...")
                        
                    else:
                        # Handling invalid inputs
                        print("Invalid input. Please try again.")
           
                break  # Exiting the first while loop

            elif choice == "no":
                # Outcome: User decides not to take a closer look at the written note
                print("There is nothing else of importance in this room, only that white, shimmering piece of paper.\n"
                      "Something is really telling you to take a closer look at it again!")
            else: 
                # Handling invalid inputs
                print("Invalid input. Please try again.")
            
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
plumbus = Item("Plumbus", "It's a plumbus. Everyone needs plumbuses.", movable=True)
mrpoopybutthole_painting = Item("The Painting Of The Great Mr. Poopybutthole",
                                "Wow, it's a pocket-sized, marvellous Renessaince-Painting of Mr. Poopybutthole (longtime friend of the family).",
                                movable=True)

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
techno_club = TechnoClub("Club", "Nobody knows who's idea the club was.")
teleportation_machine = Item("teleportation machine",
                             "A teleportation machine enables instant, random travel between locations in the game.",
                             movable=False
                             )
bubbletea_shop = BubbleteaShop("bubbletea shop", "Cute little Bubbletea Shop at the ZDD.")
gym_first_floor = Gym("Gym on the first floor", "This is the new gym in the ZDD")
vr_room = VrRoom(
    "vr_room", "You can see all those lights in the room, you wonder what it can be.."
)
soda_machine = SodaMachine("soda","mysterious soda machine.")
pigeon_house = PigeonHouse("pigeon house", "An abandoned pigeon house.")
movieTheater_2ndFloor = MovieTheater_2ndFloor("movie theater",
                                              "You can see rows of seats facing a large screen.",
                                              teleportation_machine
                                              )
small_book_corner = SmallBookCorner("small book corner", "A cozy place to relax and study to.")
hidden_laboratory = HiddenLaboratory("hidden laboratory", "Secret lab for data science experiments.")
darkroom = DarkRoom("darkroom", "A mysterious darkroom with a surprise")
#issue9and10:
game_room = GameRoom("game_room", "mhh maybe not as fun as it sounds..", [mrpoopybutthole_painting])

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "kitchen_first_floor": kitchen_first_floor,
    "bubbletea_shop": bubbletea_shop,
    "gym_first_floor": gym_first_floor,
    "vr_room": vr_room,
    "soda_machine": soda_machine,
    "pigeon_house": pigeon_house,
    "movieTheater_2ndFloor": movieTheater_2ndFloor,
    "small_book_corner": small_book_corner,
    "hidden_laboratory": hidden_laboratory,
    "dark_room": darkroom,
    "techno_club": techno_club,
    "game_room": game_room
}
