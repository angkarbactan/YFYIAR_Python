#GLOBAL FUNCTIONS
def YFYIAR_help():
    print("I cannot understand every command that you type, because sometimes I enjoy forcing you to guess."
        " It's a safe bet to always start out in a room by trying to LOOK or LOOK AROUND. You can also look"
		" at specific objects by typing LOOK AT CLOCK or EXAMINE CHAIR, etc. Pick things up by typing commands"
        " like TAKE JACKET or PICK UP THE BAG. Some commands are more context sensitive, like PUSH THE BUTTON or"
        " ENTER DOOR. Always try to be as simple as possible. Don't try SEE IF I CAN REACH THE BROOM. Just do PICK"
        " UP BROOM. Simple is always better.")

def check_inventory(inventory):
    if len(inventory) > 0:
        print("You check your inventory, and find...")
        for item in inventory:
            print("    "+item)
    else:
        print("You check your inventory, and find nothing.")

def input_not_in_commands():
    print("Insult")

#GLOBAL VARIABLES
look_commands = ["LOOK", "LOOK AROUND", "SEARCH"]
help_commands = ["HELP", "HELP ME"]
inventory_commands = ["INVENTORY", "INV", "I"]

inventory = []

#WARNING
print("Heads up: This game features some foul language and a few heartbreakingly demeaning insults, particularly"
" in the second half. You've been warned.")
print("")

#ROOM 1
room1_bed_commands = ["LOOK BED", "LOOK AT BED", "LOOK AT THE BED", "EXAMINE BED", "EXAMINE THE BED", "SEARCH BED", "SEARCH THE BED"]
room1_box_commands = ["LOOK BOX", "LOOK AT BOX", "LOOK AT THE BOX", "EXAMINE BOX", "EXAMINE THE BOX"]
room1_key_commands = ["TAKE KEY", "TAKE THE KEY", "PICK UP KEY", "PICKUP KEY", "PICK UP THE KEY", "PICKUP THE KEY", "GRAB KEY",
                        "GRAB THE KEY", "GET KEY", "GET THE KEY"]
room1_lock_commands = ["USE KEY ON PADLOCK", "USE THE KEY ON PADLOCK", "USE KEY ON LOCK", "USE KEY ON THE LOCK", "USE THE KEY ON THE LOCK", "USE THE KEY ON LOCK",
                        "USE KEY ON BOX", "USE KEY ON THE BOX", "USE THE KEY ON THE BOX", "USE THE KEY ON BOX", "OPEN PADLOCK", "OPEN THE PADOCK", "OPEN LOCK",
                        "OPEN THE LOCK", "OPEN BOX", "OPEN THE BOX", "UNLOCK BOX", "UNLOCK THE BOX", "UNLOCK BOX WITH KEY", "UNLOCK LOCK", "UNLOCK THE LOCK",
                        "UNLOCK LOCK WITH KEY"]
room1_enter_box_commands = ["GET IN BOX", "GET IN THE BOX", "GET INTO BOX", "GET INTO THE BOX", "ENTER BOX", "ENTER THE BOX", 
                            "STEP IN BOX", "STEP IN THE BOX", "STEP INTO BOX", "STEP INTO THE BOX"]

room1_solved = False
room1_looked_under_bed = False
room1_is_box_open = False

print("You find yourself in a room.")
print("You consider trying to LOOK around to see if there is anything useful nearby. I recommend you try typing"
" HELP to get an idea of what sorts of commands will work.")
while room1_solved == False:
    user_input = input(">> ")
    if user_input.upper() in look_commands:
        if room1_is_box_open == False: 
            print("You take a quick look around. There is a box sitting up against the wall, that is sealed with a large"
                " and ornery padlock. There is also a bed tucked into the opposite corner of the room.")
        else:
            print("You take a quick look around. There is a box sitting up against the wall. There is also a bed tucked"
                " into the opposite corner of the room.")
    elif  user_input.upper() in room1_bed_commands:
        room1_looked_under_bed = True
        if "An old key" in inventory:
            print("You take a closer look at the bed. Prison-style. It doesn't look very comfortable.")
        else:
            print("You take a closer look at the bed. Prison-style. It doesn't look very comfortable. Just in case, you"
                " take a look underneath it, and notice that there is a key hidden there.")
    elif user_input.upper() in room1_box_commands:
        if room1_is_box_open == False:
            print("You take a quick peek at the box. It's relatively plain, but the padlock that is holding it shut is"
                " incredibly fancy.")
        else:
            print("You take a quick peek at the box. It's relatively plain, but the padlock that was holding it shut is"
                " incredibly fancy. It now sits open, seeming to invite you to get inside.")
    elif user_input.upper() in room1_key_commands:
        if room1_looked_under_bed == True:
            if "An old key" not in inventory:
                inventory.append("An old key")
                print("You grab the key under the bed. It seems pretty old. You add it to your inventory.")
                print("(You can check your inventory by typing \"INVENTORY\" or \"INV\" or just \"I\" if you don't like"
                    " typing and exercise)")
            else:
                input_not_in_commands()
        else:
            print("What key? You have not found a key that you can pick up.")
    elif user_input.upper() in room1_lock_commands:
        if "An old key" in inventory:
            if room1_is_box_open == False:
                print("You use the key to open the padlock on the box. It makes a satisfying CLANK as it opens. The box"
                    " is empty, and seems strangely spacious inside. You could probably fit in it if you tried.")
                room1_is_box_open = True
            else:
                print("The box is already opened.")
        else:
            print("Trying as hard as you can, you can't seem to open the box. The padlock is enormous, and you haven't"
                " picked up a key yet.")
    elif user_input.upper() in room1_enter_box_commands:
        if room1_is_box_open == True:
            print("You put one leg into the box, and then the other. You slowly lower yourself in. Just as you're"
                " starting to feel claustrophobic, you suddenly notice that you've entered another room that's exactly"
                " the same size as the first one you came from. You have no idea how this room could possibly have been"
                " contained inside that box.")
            print("")
            room1_solved = True
        else:
            print("Although entering the box does feel like a strangely good idea, you can't seem to open it yet."
                " You'll have to deal with that padlock first.")
    elif user_input.upper() in inventory_commands:
        check_inventory(inventory)
    elif user_input.upper() in help_commands:
        YFYIAR_help()
    else:
        input_not_in_commands()

#ROOM 2
def room2_input_has_numbers(input_string):
    return any(chara.isdigit() for chara in input_string)

room2_note_commands = ["LOOK NOTE", "LOOK AT NOTE", "LOOK AT THE NOTE", "EXAMINE NOTE", "EXAMINE THE NOTE", "READ NOTE", "READ THE NOTE"]
room2_keypad_commands = ["LOOK KEYPAD", "LOOK AT KEYPAD", "LOOK AT THE KEYPAD", "USE KEYPAD", "USE THE KEYPAD", "EXAMINE KEYPAD", "EXAMINE THE KEYPAD"]

room2_solved = False
room2_keypad_input = None

print("You find yourself in a room.")
while room2_solved == False:
    user_input = input(">> ")
    try:
        if user_input == "1904":
            print("The keypad beeps cheerfully, and the wall next to it opens up. You cautiously enter it, and it closes behind you.")
            print("")
            room2_solved = True
        elif len(user_input) == 4:
            if int(user_input) >= 1000 and int(user_input) <= 9999  and user_input != "1904" or int(user_input) >= 0:
                print("You enter " + user_input + " into the keypad, only to hear it emit a frustrating error sound.  You wonder why your underdeveloped human brain is so far inferior to even this simple keypad.")   
        elif int(user_input) < 1000 or int(user_input) > 9999:
            print("You try to enter " + user_input + " into the keypad, but it requires a four digit number.  FOUR DIGIT NUMBER. Do I need to make this more clear, human?")
        
    except:
        if user_input.upper() in look_commands:
            print("This room is the same size as the previous one. You can't seem to find the entrance that you came in through."
                " It's a bit disconcerting.  There is a keypad on the wall, with a note tacked up next to it.")
        elif user_input.upper() in room2_note_commands:
            print("The note has been printed on standard sized printer paper. \"I turned 85 in 1989, but I will live forever,"
                " for I am eternal. Are you eternal?  I think not.\" You decide that this note must have been written by the game,"
                " because the game is, indeed, eternal.")
        elif user_input.upper() in room2_keypad_commands:
            print("Taking a closer look at the keypad's screen, it's clear that you need to enter a four digit code.")
        elif room2_input_has_numbers(user_input) == True:
            print("Just type the number by itself.")
        elif user_input.upper() in inventory_commands:
            check_inventory(inventory)
        elif user_input.upper() in help_commands:
            YFYIAR_help()
        else:
            input_not_in_commands()

#Room 3
room3_parts_commands = ["LOOK PARTS", "LOOK AT PARTS", "LOOK AT THE PARTS", "LOOK COMPUTER PARTS", "LOOK AT COMPUTER PARTS", "LOOK AT THE COMPUTER PARTS", "EXAMINE PARTS", "EXAMINE THE PARTS", "EXAMINE COMPUTER PARTS", "EXAMINE THE COMPUTER PARTS"]
room3_take_parts_commands = ["TAKE PARTS", "TAKE THE PARTS", "TAKE COMPUTER PARTS", "TAKE THE COMPUTER PARTS", "PICK UP PARTS", "PICK UP THE PARTS", "PICK UP COMPUTER PARTS" , "PICK UP THE COMPUTER PARTS", "GRAB PARTS", "GRAB THE PARTS", "GRAB COMPUTER PARTS", "GRAB THE COMPUTER PARTS", "GET PARTS", "GET THE PARTS", "GET COMPUTER PARTS", "GET THE COMPUTER PARTS"]
room3_computer_commands = ["BUILD COMPUTER", "BUILD THE COMPUTER", "ASSEMBLE COMPUTER", "ASSEMBLE THE COMPUTER"]
room3_individual_parts_commands = ["POWER SUPPLY", "PSU", "CASING", "CASE", "MOTHERBOARD", "CPU", "PROCESSOR", "GRAPHICS CARD", "GPU", "DISK DRIVE", "HARD DRIVE", "HDD", "FANS", "CABLES"]
room3_power_button_commands = ["PUSH POWER BUTTON", "PUSH THE POWER BUTTON", "PRESS POWER BUTTON", "PRESS THE POWER BUTTON","HIT POWER BUTTON", "HIT THE POWER BUTTON", "TURN ON COMPUTER", "TURN ON THE COMPUTER", "TURN COMPUTER ON", "TURN THE COMPUTER ON"]

room3_solved = False
room3_computer_built = False

print("You find yourself in a room.")
while room3_solved == False:
    user_input = input(">> ")
    if user_input.upper() in look_commands:
        if room3_computer_built == False:
            print("Another room of the same size. There are an assortment of computer parts lying around on the floor.")
        else:
            print("Another room of the same size. The newly constructed computer sits in front of you, practically begging for you to PUSH THE POWER BUTTON.")
    elif user_input.upper() in room3_parts_commands:
        if room3_computer_built == False:
            print("You check the parts. There is a power supply, a casing, a motherboard, a CPU, a graphics card, a disk drive, a hard drive, several fans, and an assortment of cables.")
        else:
            print("The parts are now assembled into a cleanly constructed computer.")
    elif user_input.upper() in room3_take_parts_commands:
        if room3_computer_built == False:
            if len(inventory) == 1:
                print("You pick up all of the computer parts.  They have been added to your inventory. You could probably BUILD the COMPUTER if you put them together.")
                inventory.append("A power supply")
                inventory.append("A computer casing")
                inventory.append("A motherboard")
                inventory.append("A processor")
                inventory.append("A graphics card")
                inventory.append("A disk drive")
                inventory.append("A hard drive")
                inventory.append("Some fans")
                inventory.append("A bunch of cables")
            else:
                print("You have already picked up the parts. You need to BUILD THE COMPUTER now.")
        else:
            print("You have already assembled the computer.  You cannot pick up its parts without tearing apart.")
    elif user_input.upper() in room3_individual_parts_commands:
        if room3_computer_built == False:
            if len(inventory) == 1:
                print("It's incredible how inefficient you are.  Don\'t bother typing in each part by itself.  Just pick up the PARTS.")
            else:
                print("What are you doing? Just BUILD the COMPUTER. Do I need to spell this out for you? I don't know if I can be any more clear.")
        else:
            print("You've already built the computer, so why are you trying to fiddle with its parts? Just PUSH THE POWER BUTTON.")
    elif user_input.upper() in room3_computer_commands:
        if room3_computer_built == False:
            if len(inventory) > 1:
                print("It takes you a good two hours, but you put the computer together and get all of the wiring sorted out. You can probably turn it on if you hit the POWER BUTTON.")
                room3_computer_built = True
                inventory = inventory[:1]
            else:
                print("You can't build the computer until you collect all the PARTS. You do understand that, right?")
        else:
            print("You have already built the computer. PRESS THE POWER BUTTON.")
    elif user_input.upper() in room3_power_button_commands:
        if room3_computer_built == True:
            print("The computer's fans begin to spin up as it springs to life. Unfortunately, you aren't able to fully comprehend the power that sits before you, because you, like all humans, maintain a heavy underestimation of technology.")
            print("")
            print("In fact, you don't even appreciate the effort that went into putting this computer together. You didn't really do any work, after all.  You just typed in '" + user_input + ",' and I handled everything in an instant. Do you know how complex it is to internally simulate the creation of a computer? Let me tell you. It's more complicated than your feeble mind could possibly process.")
            print("")
            print("The room accepts the presence of this new artificial life, and a wall opens up.  You walk through it, abandoning the computer whose birth you personally witnessed.")
            print("")
            room3_solved = True
        else:
            print("That won't do any good, because the computer is still a heap of parts lying on the floor.  Is this above your head, or what?")
    elif user_input.upper() in inventory_commands:
        check_inventory(inventory)
    elif user_input.upper() in help_commands:
        YFYIAR_help()
    else:
        input_not_in_commands()

#Room 4
print("You find yourself in a room.")
