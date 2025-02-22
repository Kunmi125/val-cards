import pygame
import time

pygame.init()

HEIGHT = 800
WIDTH = 590


sc = pygame.display.set_mode((HEIGHT, WIDTH))
bg = pygame.image.load("image1.jpg")

bg1 = pygame.transform.scale(bg,(HEIGHT, WIDTH))

while True:
    font = pygame.font.SysFont("Arial", 35)
    img = pygame.image.load("v-day1.png")
    text = font.render("Happy Valentines",True, (255,0,0))
    sc.blit(img, (0,0))
    sc.blit(text, (150,50))
    pygame.display.update()
    time.sleep(2)


    font = pygame.font.SysFont("Arial", 35)
    img = pygame.image.load("v-day2.png")
    text = font.render("Happy Valentines",True, (255,0,0))
    sc.fill((0,0,0))
    sc.blit(img, (90,0))
    sc.blit(text, (150,50))
    pygame.display.update()
    time.sleep(2)
