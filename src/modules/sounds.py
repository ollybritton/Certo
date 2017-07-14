import pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(64)

def play(sound, volume = 0.25, indef = False):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play( -1 if indef else 1 )

def stop():
    pygame.mixer.stop()
    pygame.mixer.music.stop()

play("../sounds/win.wav")
