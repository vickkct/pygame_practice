import random

import pygame

arr_circles = []

pygame.init()
pygame.display.set_caption('Игра "Лопаем шарики"')
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
running = True

clock = pygame.time.Clock()

count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for c in arr_circles:
        c[2] = (c[2][0], c[2][1] + 5)
        pygame.draw.circle(*c)
    clock.tick(30)
    pygame.display.flip()
    count+=1
    if count == 30*60:
        running = False
    if count % 30 == 0:
        arr_circles.append([screen, (random.randrange(255), random.randrange(255), random.randrange(255)), (random.randrange(20, screen.get_width()-20), 0), 20])
pygame.quit()
