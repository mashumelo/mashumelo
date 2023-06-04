#function to ask play again or not
def play_again():
    print("\nDo you want to play again? (y or n)")

    # convert the player's input to lower_case
    answer = input(">").capitalize()

    if "Y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        start()
    elif "N" in answer:
        # if player typed "no" or "n" exit() the program
        exit()
    else:
        # if player selects any choice besides "yes" "y" "no" or "n" prompt the player to enter a choice
        print("You have to make a choice yes or no.")

#define the variable for a game over
def game_over(reason):

    #print the "reason" in a new line (\n)
    print("\n" + reason)
    print("Game Over!")

    #ask player to play again or not by activating play_again() function
    play_again()

#define end() function; end of story at the moment
def end():
    print("As you walk back into the room, your senses begin to become more clear.\n"
          "You begin to see glowing stones on the floor with markings in different letter formations.\n"
          "As you put the markings into place, you begin to realize the three slots for the stones spell out something...\n"
          "FIN.\n")

    #call exit() function
    exit()

#define markings() function
def markings():
    print("You take the right path from the corridor.\n"
          "It leads you into a room with more of those occult markings.\n"
          "You feel a sudden supernatural feeling come over you.\n"
          "You begin to realize you do know those markings.\n"
          "They're markings from your past life, as you begin to think back you realize the door you saw earlier was the exit.\n"
          "You decide to go back.\n")

    #call end() function
    end()

#define deadend() function
def deadend():
    print("As you walk left further into the corridor you stumble upon a dead end room.\n"
          "It seems odd at first, but as you step inside you hear a pressure plate activate and a stone door begins closing quickly behind you.\n"
          "You try clawing and scratching your way out at the door, but you realize there's no use.\n"
          "You're here stuck in this stone room, about to rot out the rest of your days.\n")

    #call game_over("Sometimes our gut instinct isn't always right, huh?") function       
    game_over("Sometimes our gut instinct isn't always right, huh?")

#define cavern2() function
def cavern2():
    print("You decide to investigate further into the tunnels.\n"
          "As you get further in you see a body that has been mutilated laying sprawled across the ground with strange markings on the walls.\n"
          "You notice the markings seem to be some sort of occult markings.\n"
          "You assume that they're from a time period extremely long ago.\n")

    #player inspects the area better around them and finds a key
    print("You inspect the area more closely.\n"
          "You happen to notice a key laying on a shelf.\n"
          "You take the key.\n")

    #the player continues further into the cave
    print("You continue further into the cave, and stumble across a doorway made of stone.\n"
          "On the doorway you notice more of those strange occult markings, and three openings for stones.\n"
          "Across from it is another corridor that leads into total darkness.\n"
          "You see a lamp sitting on the ground with a little fuel left in it.\n"
          "You take it.\n")

    #player continues until they reach another branching path
    print("As you walk into the dark corridor, you feel a tingling sensation in your back.\n"
          "You brush it off, and see another branching pathway.\n"
          "You think to yourself, when is this ever going to end?\n")

    #prompt the player for input to go left or right
    print("Do you go left or do you go right?\n")

    #input
    answer = input(">").capitalize()

    if "L" in answer:
        #if you go left call deadend() function
        deadend()
    
    elif "R" in answer:
        #if you go right you come upon a room with strange markings; call markings() function
        markings()

#if the player chooses to go left
def left():
    print("You take the pathway down to the left hand side.\n"
          "As you walk down the dark corridor, you begin to smell a metallic odor that becomes more pungent the further you travel.\n"
          "You begin to realize it's the smell of blood, and wonder where it's coming from.\n")
    
    #opt for the player to walk further into the cave.
    print("Do you inspect further down the cave? Yes or no?\n")

    answer = input(">").capitalize()

    if "Y" in answer:
        #if answer is "yes" or "y" call cavern2() function
        cavern2()

    elif "N" in answer:
        #if answer is "no" or "n"
        print("You decide to go back the way you came.\n")

        #call leftorright() function
        leftorright()

#if the player chooses not to push the door further
def choice2():
    print("You decide to turn around and go back the way you came.\n")

    #call leftorright() function
    leftorright()

#if the player proceeds further into subarctic cavern
def cavern1():
    print("You begin to walk further into the cavern.\n"
          "You keep hearing screams of something inhuman coming from benath the earth's surface.\n"
          "You're terrified, but there's no way you can turn back now.\n"
          "As you reach the hellish abyss that is nothing below your candle goes out, and everything around you grows dark.\n"
          "The screams get closer, and you feel the darkness envelope you...\n")
    
    #call for the game_over("Everything consumes you when the lights go out...")
    game_over("Everything consumes you when the lights go out...")

#if the player chooses yes to push the door further open
def choice1():
    print("You push the door with a little more force, as it slowly opens you feel a piercing cold gust of air brush against your face.\n"
          "You hear a cracking noise the further the door opens.\n"
          "As you step inside it feels as though you've entered a subarctic climate not made for survival.\n"
          "You see a dead body folded in half laying stiff near the doorway.\n"
          "You decide that must have been the cracking noise you heard as you opened the door.\n")

    #print() information about the subarctic room
    print("You look around the room more and see and old rusty looking door.\n"
          "You think it's going to be impossible to open, and that the handle may break off even by touch.\n"
          "You decide to try to open it, and much to your surprise it opens right up.\n"
          "As the doorway leading deeper into the dark caves opens up, you catch a whiff of the stench of rotting flesh.\n"
          "You hear bloodcurdling screams that don't even sound human in the distance.\n")

    #ask the player to proceed further into cave "yes" or "no"
    print("Do you proceed further into the cave? Yes or no?\n")

    #prompt for player input
    answer = input(">").capitalize()

    if "Y" in answer:
        #if answer is "yes" or "y" call cavern1() function
        cavern1()

    elif "N" in answer:
        #if answer is "no" or "n" print("You decide to turn back the way you came.")
        print("You decide to turn back the way you came.\n")

        #call leftorright() function
        leftorright()

#if the player choices to go right
def right():
    print("You decide to go down the right hand path.\n"
          "You begin walking down the path and feel a small chill.\n"
          "As you get further down the path you see a doorway.\n"
          "You try to open it, but it won't budge.\n")

    #print("Do you try to push it open with a little more force? Y or n?")
    print("Do you try to push it open with a little more force? Y or n?")

    #take player input
    answer = input(">").capitalize()


    if "Y" in answer:
        #if player typed "yes" or "y" call choice1() function
        choice1()
    elif "N" in answer:
        #if player typed "no" or "n" call choice2() function
        choice2()
    
    #if the choice is anything else
    else:
        #else you must pick a choice yes or no
        print("You have to pick a choice, yes or no.")


def leftorright():
    
    #ask for choice to go left or right
    print("You see two caverns, do you head to the left or to the right?\n")

    #player inputs answer for left or right
    answer = input(">").capitalize()
    if "L" in answer:
        #if the choice is left call left() function
        left()
    elif "R" in answer:
        #if the choice is right call right() function
        right()
    else:
        #else you must pick a choice left or right
        print("You must pick a choice, left or right.\n")


#define the start variable to begin the game
def start():
    #player name input
    player_name = input("What is your name? ")

    #first part, input player name, and beginning story
    print(f"Hello {player_name}.\n"
          "You wake up in a dark room.\n"
          "You stumble around for a bit and find a candle.\n"
          "You light it.\n")

    #print() text about waking up in a cavern, and surrounding inspection
    print("You notice you're in a cavern.\n"
          "You inspect your surroundings more closely.\n"
          "You see a warning sign on a shelf. It features a skull and crossbones.\n"
          "You take heed and avoid the contents on the shelf.\n")

    #call leftorright() function
    leftorright()


#start the game
start()
