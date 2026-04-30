import pygame  
import time
from WAKE_UP import wake_up
import GLOBAL_VARS

pygame.mixer.init()
elevatormusic_sound = 'Sounds/elevatormusic2.wav'
wake_up_sound = pygame.mixer.Sound(elevatormusic_sound)
wake_up_sound.play()
time.sleep(0.1) 

GLOBAL_VARS.name = input("Hi! Welcome to a day in the life at Smith College! What's your name? ").strip().capitalize()

GLOBAL_VARS.major = input(f"It's nice to meet you, {GLOBAL_VARS.name}! What's your major? If you're undecided, what subject is your favorite? ").strip().capitalize()

GLOBAL_VARS.house = input(f"{GLOBAL_VARS.major} sounds like such a fun thing to study! What house are you in? ").strip().capitalize()

wake_up()

