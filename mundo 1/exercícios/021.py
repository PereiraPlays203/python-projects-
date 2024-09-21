import pygame

pygame.init()
pygame.mixer.music.load('oi.mp3')
pygame.mixer.music.play()
pygame.event.wait()