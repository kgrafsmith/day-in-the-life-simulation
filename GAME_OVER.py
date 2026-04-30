import pygame  
import time
from COLLAGE import create_collage
import GLOBAL_VARS

def game_over():
    pygame.mixer.init()
    trombone_sound = 'Sounds/trombone.wav'
    youdied_sound = pygame.mixer.Sound(trombone_sound)
    youdied_sound.play()
    time.sleep(0.1) 
    print("")
    print ("Game over! I hope you had a fun day at Smith! Here's what your day looked like: ")
    create_collage()
    
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == "y":
        from WAKE_UP import wake_up
        wake_up()
    
