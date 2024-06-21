import random

import pygame

arr_circles = []

pygame.init()
font = pygame.font.SysFont("Times New Roman", 15)
pygame.display.set_caption('Игра "Лопаем шарики"')
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
running = True

clock = pygame.time.Clock()

countScreen = 0
count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            f = False
            iters = len(arr_circles)
            i = 0
            while i < iters:
                k = ((event.pos[0] - arr_circles[i][2][0]) ** 2 + (event.pos[1] - arr_circles[i][2][1]) ** 2) ** 0.5
                if k <= 10:
                    count += 1
                    f = True
                    arr_circles[i] = arr_circles[len(arr_circles) - 1]
                    arr_circles.pop()
                    iters -= 1
                i += 1
            if not f:
                count -= 1
    screen.fill("black")
    iters = len(arr_circles)
    i = 0
    while i < iters:
        arr_circles[i][2] = (arr_circles[i][2][0] + random.randrange(-2, 3), arr_circles[i][2][1] + 2)
        if arr_circles[i][2][1] > screen.get_height() + 10:
            count -= 5
            arr_circles[i] = arr_circles[len(arr_circles) - 1]
            arr_circles.pop()
            iters -= 1
        pygame.draw.circle(*arr_circles[i])
        i += 1
    string = "Очки: " + str(count) + "; Время: " + str(60 - countScreen // 30)
    screen_text = font.render(string, False, "yellow")
    screen.blit(screen_text, (0, 0))

    clock.tick(30)
    pygame.display.flip()
    countScreen += 1
    if countScreen == 30 * 60:
        running = False
    if countScreen % 30 == 0:
        arr_circles.append([screen, (random.randrange(100, 255),
                                     random.randrange(100, 255),
                                     random.randrange(100, 255)),
                            (random.randrange(10, screen.get_width() - 10), 0), 10])
pygame.quit()
