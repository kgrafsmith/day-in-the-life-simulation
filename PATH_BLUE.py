import pygame  
import time
import GLOBAL_VARS
from GAME_OVER import game_over
from PATH_PINK import PATH_PINK_done_for_day
from PATH_PINK import PATH_PINK_major_class

def PATH_BLUE_start():
    print("")
    print("Yummy breakfast! What's next?")
    print("1. Go to your 9:25 - you have to be responsible!")
    print("2. Skip class, sleep is more important!")
    print("3. Go to your shift at Compass!")
    while True:
        choice = input("Choose 1, 2, or 3: ").strip()
        match choice:
            case "1":
                PATH_BLUE_go_to_class()
                break
            case "2":
                PATH_BLUE_skip_class()
                break
            case "3":
                PATH_BLUE_compass_shift()
                break
            case _:
                print("Error: please enter 1, 2, or 3.")

# ---------- 1) GO TO CLASS BRANCH ----------

def PATH_BLUE_go_to_class():
    print("")
    GLOBAL_VARS.show_gotoyour925 = True
    print("What class are you going to?")
    print("1. Creative Writing")
    print("2. Organic Chemistry")
    print(f"3. {GLOBAL_VARS.major}")
    
    while True:
        class_choice = input("Choose 1, 2, or 3: ").strip()
        match class_choice:
            case "1":
                print("The ghost of Shakespeare comes back to haunt you... sleep well")
                GLOBAL_VARS.show_creativewriting = True
                GLOBAL_VARS.show_shakespearedeath = True
                GLOBAL_VARS.show_youdied = True
                game_over()
                break
            case "2":
                print("You didn't realize the asperin you synthesized in class today wasn't edible... you died!")
                GLOBAL_VARS.show_organicchem = True
                GLOBAL_VARS.show_aspirindeath = True
                GLOBAL_VARS.show_youdied = True
                game_over()
                break
            case "3":
                GLOBAL_VARS.show_major = True
                print("That was so fun!!")
                PATH_BLUE_choose_org()
                break
            case _:
                print("Error: please enter 1, 2, or 3.")
                

def PATH_BLUE_choose_org():
    print ("Time to go to your club meeting! What org are you a part of?")
    print("1. KPop Dance Club")
    print("2. Ceramics")
    print("3. Ultimate Frisbee")
    
    while True:
        org_choice = input("Choose 1, 2, or 3: ").strip()
        match org_choice:
            case "1":
                GLOBAL_VARS.show_KpopDanceClub = True
                PATH_PINK_major_class()
                break
            case "2":
                GLOBAL_VARS.show_Ceramics = True
                PATH_PINK_major_class()
                break
            case "3":
                GLOBAL_VARS.show_Frisbee = True
                pygame.mixer.init()
                fairyapproaching_sound = 'Sounds/fairyapproaching.wav'
                fairy_sound = pygame.mixer.Sound(fairyapproaching_sound)
                fairy_sound.play()
                time.sleep(0.1) 
                print('A fairy approaches you... "it\'s really cold out, you should stay inside!"')
                inside = input("Still wanna go outside? (y/n) ")
                if inside == "y":
                    GLOBAL_VARS.show_bibble = True
                    GLOBAL_VARS.show_frostbite = True
                    print ("You got frostbite and froze to death.")
                    game_over()
                elif inside == "n":
                    GLOBAL_VARS.show_bibble = True
                    PATH_BLUE_choose_org()
                else:
                    print ('Error: please write "y" or "n"')
                break
            case _:
                print("Error: please enter 1, 2, or 3.")
                

                
# ---------- 2) SKIP CLASS BRANCH ----------
                
def PATH_BLUE_skip_class():
    pygame.mixer.init()
    snoring_sound = 'Sounds/snoring.wav'
    skip_class_sound = pygame.mixer.Sound(snoring_sound)
    skip_class_sound.play()
    time.sleep(0.1) 
    print("")
    GLOBAL_VARS.show_smithbed = True
    print("Where are you gonna crash?")
    print("1. Your bed")
    print("2. Alumnae gym couch")
    print("3. Neilson Learning Commons")

    while True:
        nap_choice = input("Choose 1, 2, or 3: ").strip()
        match nap_choice:
            case "1":
                print("You end up sleeping through the rest of the day...")
                GLOBAL_VARS.show_yourbed = True
                GLOBAL_VARS.show_sleepthroughday = True
                GLOBAL_VARS.show_dreaming = True
                game_over()
                break
            case "2":
                print("You woke up and couldn't find the exit. You starved.")
                GLOBAL_VARS.show_alumnaegym = True
                GLOBAL_VARS.show_maze = True
                GLOBAL_VARS.show_youdied = True
                game_over()
                break
            case "3":
                print("You sleep past closing and the boogeyman gets you!!!")
                GLOBAL_VARS.show_learningcommons = True
                GLOBAL_VARS.show_boogeyman = True
                GLOBAL_VARS.show_youdied = True
                game_over()
                break
            case _:
                print("Error: please enter 1, 2, or 3.")


# ---------- 3) COMPASS BRANCH ----------

def PATH_BLUE_compass_shift():
    print("")
    GLOBAL_VARS.show_compasscafe = True
    print("What drink will you start your shift with?")
    print("1. Dirty chai, extra shot espresso — you are sooo sleepy.")
    print("2. Busy bee latte — you’re ready for a buzz.")
    print("3. Iced tea with lemon — you’re cool, calm, and collected.")

    while True:
        drink_choice = input("Choose 1, 2, or 3: ").strip()
        match drink_choice:
            case "1":
                PATH_BLUE_dirty_chai()
                break
            case "2":
                PATH_BLUE_busy_bee()
                break
            case "3":
                PATH_BLUE_iced_tea()
                break
            case _:
                print("Error: please enter 1, 2, or 3.")
                
def PATH_BLUE_dirty_chai():
    print("")
    GLOBAL_VARS.show_dirtychai = True
    pygame.mixer.init()
    fairyapproaching_sound = 'Sounds/fairyapproaching.wav'
    fairy_sound = pygame.mixer.Sound(fairyapproaching_sound)
    fairy_sound.play()
    time.sleep(0.1) 
    print('A fairy approaches you: "That’s too much caffeine!!"')
    chai_choice = input("Still wanna drink the chai? (y/n): ").strip().lower()
    if chai_choice == "y":
        print("Your heart rate hits 9000. You vibrate into another dimension.")
        GLOBAL_VARS.show_bibble = True
        game_over()
    elif chai_choice == "n":
        print("Good call. You pour it out and restart your shift.")
        GLOBAL_VARS.show_bibble = True
        PATH_BLUE_compass_shift()
    else:
        print("Error: please enter y or n.")
        PATH_BLUE_dirty_chai()

def PATH_BLUE_busy_bee():
    print("")
    GLOBAL_VARS.show_latte = True
    print("What a fun shift this is! Oh no...")
    print("A fight is breaking out over Compass sushi!")
    print("Do you:")
    print("1. Stay at the café")
    print("2. Go home early")
    while True:
        choice = input("Choose 1 or 2: ").strip()
        match choice:
            case "1":
                print("You get hit in the crossfire with a stray California roll.")
                print("It knocks you out cold.")
                GLOBAL_VARS.show_foodfight = True
                GLOBAL_VARS.show_youdied = True
                game_over()
                break
            case "2":
                print("You sneak out successfully and are about to head home....")
                PATH_BLUE_jerry_fires_you()
                break
            case _:
                print("Error: please choose 1 or 2.")
                
def PATH_BLUE_iced_tea():
    print("")
    GLOBAL_VARS.show_icedtealemon = True
    print("A refreshing choice!")
    print("Your shift is smooth and uneventful, good job!")
    PATH_PINK_done_for_day()
    

def PATH_BLUE_jerry_fires_you():
    print("")
    print("Your manager Jerry storms out of the back room, absolutely furious.")
    print('"THAT’S IT. YOU’RE FIRED."')
    print("What do you do?")
    print("1. Fight him")
    print("2. Go home and cry")

    while True:
        jerry_choice = input("Choose 1 or 2: ").strip()
        match jerry_choice:
            case "1":
                print("Jerry swings first. You swing harder. You become a legend on Confesh.")
                GLOBAL_VARS.show_Jerry = True
                GLOBAL_VARS.show_fight = True
                game_over()
                break
            case "2":
                print("You walk home in tears, clutching your Compass apron. Tragic.")
                GLOBAL_VARS.show_Jerry = True
                GLOBAL_VARS.show_cry = True
                game_over()
                break
            case _:
                print("Error: please choose 1 or 2.")
