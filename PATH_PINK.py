import pygame  
import time
import GLOBAL_VARS
from GAME_OVER import game_over


def PATH_PINK_start():
    print("")
    print("You grab your food and head to the library for a serious study-sesh.")
    print("After you grab some food at Compass, it’s time for class!")
    print("What do you have at 1:20?")
    print("1. Your major course")
    print("2. I don’t have class, I’m done for the day")
    print("3. Sports practice")

    while True:
        choice = input("Choose 1, 2, or 3: ").strip()

        match choice:
            case "1": 
                GLOBAL_VARS.show_major = True
                print ("")
                print(f"Your {GLOBAL_VARS.major} class was so fun!!")
                PATH_PINK_major_class()
                break
            case "2":
                GLOBAL_VARS.show_doneforday = True
                PATH_PINK_done_for_day()
                break
            case "3":
                GLOBAL_VARS.show_sportspractice = True
                PATH_PINK_sports_practice()
                break
            case _:
                print("Error: please enter 1, 2, or 3.")



# ---------- 1) MAJOR CLASS BRANCH ----------

def PATH_PINK_major_class():
    print("")
    print("It’s time for dinner — what’s your plan?")
    print("1. Head to the quad for stir-fry")
    print("2. Wait until 7pm for CC dinner")
    print("3. Go downtown with friends to T. Roots")

    while True:
        dinner = input("Choose 1, 2, or 3: ").strip()
        match dinner:
            case "1":
                GLOBAL_VARS.show_stirfry = True
                GLOBAL_VARS.show_full = True
                GLOBAL_VARS.show_smithbedpink = True
                print("You head to the quad for stir-fry. Delicious! But now it’s late.")
                PATH_PINK_bedtime()
                break
            case "2":
                GLOBAL_VARS.show_CCdinner = True
                PATH_PINK_CC_wait()
                break
            case "3":
                GLOBAL_VARS.show_troots = True
                GLOBAL_VARS.show_full = True
                GLOBAL_VARS.show_smithbedpink = True
                print("Dinner downtown was soooo yummy. But it’s late!")
                PATH_PINK_bedtime()
                break
            case _:
                print("Error: please choose 1, 2, or 3.")

def PATH_PINK_CC_wait():
    print("")
    pygame.mixer.init()
    fairyapproaching_sound = 'Sounds/fairyapproaching.wav'
    fairy_sound = pygame.mixer.Sound(fairyapproaching_sound)
    fairy_sound.play()
    time.sleep(0.1) 
    print("A fairy approaches you: “They might not have what you want… you should go to a dining hall.”")
    fairy = input("Still wanna wait for the CC menu? (y/n): ").strip().lower()

    if fairy == "y":
        GLOBAL_VARS.show_bibble = True
        GLOBAL_VARS.show_hungry = True
        GLOBAL_VARS.show_smithbedpink = True
        print("Everything sold out in two seconds. You go to bed hungry.")
        game_over()

    elif fairy == "n":
        GLOBAL_VARS.show_bibble = True
        GLOBAL_VARS.show_full = True
        print("You wisely avoid disaster and head to another dining hall instead.")
        PATH_PINK_bedtime()
        GLOBAL_VARS.show_smithbedpink = True
    
    else:
        print("Error: please enter y or n.")
        PATH_PINK_CC_wait()


# ---------- 2) DONE FOR THE DAY BRANCH ----------

def PATH_PINK_done_for_day():
    print("")
    GLOBAL_VARS.show_noclass = True
    print("You’re free for the rest of the day!")
    print("Time for a morning walk — where are you heading?")
    print("1. Mill River Path")
    print("2. Your UMass class")
    print("3. Dunkin’ for a snack")
        
    while True:
        walk = input("Choose 1, 2, or 3: ").strip()
        match walk:
            case "1":
                GLOBAL_VARS.show_millriver = True
                GLOBAL_VARS.show_bearattack = True
                print("You got attacked by a bear.")
                game_over()
                break
            case "2":
                print("2. Your UMass class")
                GLOBAL_VARS.show_Umass = True
                GLOBAL_VARS.show_smithbedpink = True
                print("Your prof canceled class on the walk over. You walk home and fall asleep immediately.")
                game_over()
                break
            case "3":
                GLOBAL_VARS.show_pothole = True
                GLOBAL_VARS.show_dunkin = True
                print("Uh oh! You fell into a pothole in the road.")
                game_over()
                break
            case _:
                print("Error: please enter 1, 2, or 3.")


# ---------- 3) SPORTS PRACTICE BRANCH ----------

def PATH_PINK_sports_practice():
    print("")
    print("What sport are you playing?")
    print("1. Rowing")
    print("2. Field Hockey")
    print("3. Cross Country")

    while True:
        sport = input("Choose 1, 2, or 3: ").strip()
        match sport:
            case "1":
                GLOBAL_VARS.show_rowing = True
                GLOBAL_VARS.show_fallintowater = True
                GLOBAL_VARS.show_youdied = True
                print("You fall out of the boat and drown.")
                game_over()
                break
            case "2":
                GLOBAL_VARS.show_fieldhockey = True
                GLOBAL_VARS.show_hitbyball = True
                GLOBAL_VARS.show_youdied = True
                print("The ball hits you in the head and you pass out.")
                game_over()
                break
            case "3":
                GLOBAL_VARS.show_xc = True
                GLOBAL_VARS.show_trampled = True
                GLOBAL_VARS.show_youdied = True
                print("You are trampled by your teammates and can’t get up.")
                game_over()
                break
            case _:
                print("Error: please choose 1, 2, or 3.")


# ---------- BEDTIME LOGIC ----------

def PATH_PINK_bedtime():
    print("")
    print("Dinner was soooo yummy, but now it’s late. Time for bed?")
    choice = input("yes or no? ").strip().lower()
    if choice == "yes":
        print("Yay! Goodnight!")
        game_over()
    elif choice == "no":
        PATH_PINK_fairy_stay_awake()
    else:
        print("Error: please type yes or no.")
        PATH_PINK_bedtime()


def PATH_PINK_fairy_stay_awake():
    pygame.mixer.init()
    fairyapproaching_sound = 'Sounds/fairyapproaching.wav'
    fairy_sound = pygame.mixer.Sound(fairyapproaching_sound)
    fairy_sound.play()
    time.sleep(0.1) 
    print("")
    print("A fairy approaches you: “You should really get some sleep...”")
    stay_up = input("Still wanna stay awake? (y/n): ").strip().lower()
    if stay_up == "y":
        GLOBAL_VARS.show_bibble = True
        print("You pass out in the middle of the quad. RIP.")
        game_over()
    elif stay_up == "n":
        GLOBAL_VARS.show_bibble = True
        print("Good choice. You go to bed safely!")
        game_over()
    else:
        print("Error: please enter y or n.")
        PATH_PINK_fairy_stay_awake()



