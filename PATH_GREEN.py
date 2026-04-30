import pygame  
import time
from PATH_BLUE import PATH_BLUE_go_to_class
import PATH_PINK
import GLOBAL_VARS
from GAME_OVER import game_over


def PATH_GREEN_start():
    print("")
    print("You decide: no breakfast today.")
    print("What now?")
    print("1. Go to CC and steal food")
    print("2. Go outside and eat with the squirrels")
    print("3. Starve <3")

    while True:
        choice = input("Choose 1, 2, or 3: ").strip()
        match choice:
            case "1":
                GLOBAL_VARS.show_stealfromcc = True
                GREEN_steal()
                break
            case "2":
                GLOBAL_VARS.show_minisquirreltable = True
                GREEN_squirrel()
                break
            case "3":
                GLOBAL_VARS.show_starve = True
                GREEN_starve()
                break
            case _:
                print("Error: please enter 1, 2, or 3.")
                
# ---------- 1) CC HEIST BRANCH ----------

def GREEN_steal():
    print("")
    print("You approach CC like a mastermind thief.")
    print("Do you:")
    print("1. Steal from retail dining table")
    print("2. Chat with the student workers, they'll hook you up ")
    print("3. Sprint to the back and hope you're fast enough")
    

    while True:
        steal_choice = input("Choose 1, 2, or 3: ").strip()
        match steal_choice:
            case "1":
                GLOBAL_VARS.show_stealfromretailtable = True
                GLOBAL_VARS.show_campo = True
                GLOBAL_VARS.show_youdied = True
                print("Oh no! You got caught by Campo! womp womp womp")
                game_over()
                break
            case "2":
                GLOBAL_VARS.show_studentworker = True
                GLOBAL_VARS.show_baristacrush = True
                GLOBAL_VARS.show_yourbedgreen4 = True
                print("You spark a romance with your new  barista crush!")
                game_over()
                break
            case "3":
                GLOBAL_VARS.show_runfromCC = True
                GLOBAL_VARS.show_tripandfall = True
                GLOBAL_VARS.show_youdied = True
                print("Trip. Fall. You died hungry")
                game_over()
                break
            case _:
                print("Error: please choose 1, 2, or 3.")
                
# ---------- 2) SQUIRREL BRANCH ----------
                
def GREEN_squirrel():
    pygame.mixer.init()
    squirrelchatter_sound = 'Sounds/squirrelchatter.wav'
    squirrel_sound = pygame.mixer.Sound(squirrelchatter_sound)
    squirrel_sound.play()
    time.sleep(0.1) 
    print("")
    print("Oh no! People are starting to look at you weird...")
    print("Do you:")
    print("1. Hiss at them. You reign over humans in the squirrel monarch!")
    print("2. Enjoy your squirrel breakfast unbothered :)")
    print("3. Make squirrel friends and have them chase your enemies.  Hunt them all!!!!!")
    while True:
        s = input("Choose 1, 2, or 3: ").strip()
        match s:
            case "1":
                GLOBAL_VARS.show_hissatthem = True
                GREEN_arranged_marriage()
                break
            case "2":
                GLOBAL_VARS.show_unbotheredbreakfast = True
                PATH_BLUE_go_to_class()
                break
            case "3":
                GLOBAL_VARS.show_huntthemall = True
                PATH_BLUE_go_to_class()
                break
            case _:
                print("Error: please choose 1, 2, or 3.")
                
def GREEN_arranged_marriage():
    print("")
    print("Oh no! You were forced in an arranged marriage with the squirrel princess! What do you do first?")
    print("Do you:")
    print("1. Leave her at the alter! Shes a squirrel you two cant get married!")
    print("2. Tell your partner about your unfaithfulness.")
    print("3. Get married! She looks cute enough!")

    while True:
        fate = input("Choose 1, 2, or 3: ").strip()
        match fate:
            case "1":
                pygame.mixer.init()
                fairyapproaching_sound = 'Sounds/fairyapproaching.wav'
                fairy_sound = pygame.mixer.Sound(fairyapproaching_sound)
                fairy_sound.play()
                time.sleep(0.1) 
                print ("A fairy approaches you: \"Do you really want to do this? Once you decide to leave her at the alter there is no turning back...\" ")
                fate_choice = input("Leave her? (y/n) ")
                if fate_choice == "y":
                    GLOBAL_VARS.show_bibble = True
                    GLOBAL_VARS.show_leavebrideatalter = True
                    GLOBAL_VARS.show_huntforsustinence = True
                    print ("The squirrels hunt you down and use you for sustinance.")
                    game_over()
                elif fate_choice == "n":
                    GLOBAL_VARS.show_bibble = True
                    print("Good idea.. let's try again...")
                    GREEN_arranged_marriage()
                else:
                    print("Error: please choose 1, 2, or 3.")
                break
            case "2":
                GREEN_honest_partner()
                break
            case "3":
                GLOBAL_VARS.show_getmarried = True
                GLOBAL_VARS.show_dogkingdom = True
                print ("Dog kingdom ambushes the wedding and assassinates you and your squirrel-to-be!")
                game_over()
            case _:
                print("Error: please choose 1, 2, or 3.")
                
def GREEN_honest_partner():
    print ("")
    print ("You two make up and plan to save the princess from a kingdom that oppresses her.")
    print ("Do you:")
    print ("1. Save her and let her live in your dorm! Throuple energy~~~~")
    print ("2. Save her and let her free! But your partner might get jealous...")
    while True:
        save = input("Choose 1, 2, or 3: ").strip()
        match save:
            case "1":
                GLOBAL_VARS.show_throupleenergy = True
                GLOBAL_VARS.show_rabies = True
                print ("You get rabies and die.")
                game_over()
                break
            case "2":
                GLOBAL_VARS.show_jealouspartner = True
                GLOBAL_VARS.show_partnerkillsyou = True
                print ("Your partner kills you. You die.")
                game_over()
                break
            case _:
                print("Error: please choose 1 or 2.")


# ---------- 3) STARVE BRANCH ----------

def GREEN_starve():
    print("")
    print("Oh no! You passed out on your way to class! Who's helping you?")
    print("1. Schacht center after-hours on-call underpaid nurse")
    print("2. Cooley Dick Urgent Care")
    print("3. Your girlfriend's first aid kid from her backpack")
    while True:
        faint = input("Choose 1, 2, or 3: ").strip()
        match faint:
            case "1":
                GLOBAL_VARS.show_afterhoursnurse = True
                GLOBAL_VARS.show_dieonhold = True
                GLOBAL_VARS.show_youdied = True
                print ("You were left on hold for too long. You died.")
                game_over()
                break
            case "2":
                GLOBAL_VARS.show_coolydicker = True
                GLOBAL_VARS.show_diedinER = True
                GLOBAL_VARS.show_youdied = True
                print ("The doctors gave you penicillin, you had an allergic reaction and died.")
                game_over()
                break
            case "3":
                GLOBAL_VARS.show_girlfriendfirstaidpack = True
                GLOBAL_VARS.show_yourbedgreen = True
                GLOBAL_VARS.show_cupoftea = True
                print ("Your girlfriend tells you to go to bed and sleep the rest of the day to recover. And of course you do anything she tells you to. Sleep well!")
                game_over()
                break
            case _:
                print("Error: please choose 1, 2, or 3.")
           
    
 

