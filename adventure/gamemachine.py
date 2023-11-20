import random
class GameRoom_game():
    def play_gamemachine(self, won_game=0):
        print("It's Rock Paper Scissors but with microversebattery, purposerobot and jerrysmrmeeseeks. You get the point. No? mh..\n",
                "Just play already or I will suffer eternal pain ....")
        self.won_game = won_game
        keep_playing = True
        while keep_playing:
            user_action = input("\nEnter a choice (microversebattery as 'mvb', purposerobot as 'pr', jerrysmrmeeseeks as 'mee'): ")
            possible_actions = ["mvb", "pr", "mee"]
            com_action = random.choice(possible_actions)

            print(f"\nYou chose {user_action}, I chose {com_action}.\n")

            if user_action == com_action:
                print(f"We both selected {user_action}... Don't go away with a tie. YEAH JUST DON'T OKAY? Play again.")

            elif user_action == "mvb":
                if com_action == "pr":
                    print("-->The microverse battery works effectively with more unnessecary pain than purposerobot! mvb obviously wins. Yeah you won.")
                    self.won_game += 1
                else:
                    print("-->Being Jerry's MrMeeseeks is a greater challenge than working in the mvb! You lose.")
            elif user_action == "pr":
                if com_action == "mvb":
                    print("-->The purpose robot cuts butter. Yeah, definitely better than working in the mvb. You win!")
                    self.won_game += 1
                else:
                    print("Jerry's Mr Meeseeks is blue. Of course you lose.")
            elif user_action == "mee":
                if com_action == "pr":
                    print("-->Jerry's Mr Meeseeks is blue. Of course you win!")
                    self.won_game += 1
                else:
                    print("-->Sorry, the microverse battery doesn't have the luxury to die as MrMeeseeks. Uhm, idk you still lose.")

            play_again = input("\nwanna play again? (y/n): ")
            if play_again.lower() == "y":
                print("yeah yeah, just give me uhh .. STEVE !... uhh give me like 4, 5 g crystals.",
                        "You have none? Fuck off!! I need to keep digging.... WHERE ARE MY CRYSTALS!!...")
            elif play_again.lower() != "y":
                print("\n\n no no no no no no no..ah..nonono")
                keep_playing = False

#startgame = GameRoom_game()
#startgame.play_gamemachine(0)
#print(startgame.won_game)