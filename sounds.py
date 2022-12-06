import pygame
def mp():
    pygame.mixer.init()
    pygame.mixer.music.load('files/audio.mp3')
    pygame.mixer.music.play()