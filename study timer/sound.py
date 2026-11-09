import pygame

pygame.mixer.init()
pygame.mixer.music.load("bell.mp3")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play()


pygame.time.wait(200000)  # Wait for 1 second (1000 milliseconds) to allow the sound to play

