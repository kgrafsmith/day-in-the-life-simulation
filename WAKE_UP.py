import pygame  
import time
import GLOBAL_VARS
from PATH_BLUE import PATH_BLUE_start
from PATH_PINK import PATH_PINK_start
from PATH_GREEN import PATH_GREEN_start

def wake_up():
    print("")
    print(f"Good morning, {GLOBAL_VARS.name}! Choose where to go for breakfast:")
    print("   Tyler: you have all the time in the world")
    print("   Chapin: Grab n' Go is the way to go!")
    print("   None: fuck it we ball")

    while True:
        breakfast_choice = input("Your choice? (Tyler, Chapin, None): ").strip().capitalize()

        match breakfast_choice:
            case "Tyler":
                PATH_BLUE_start()
                break
            case "Chapin":
                PATH_PINK_start()
                break
            case "None":
                PATH_GREEN_start()
                break
            case _:
                print("Error: please choose from the given options.")