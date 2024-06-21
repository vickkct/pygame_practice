import math
import random
import pygame

def game1():
    pygame.init()
    pygame.display.set_caption('Задание 4.14 "Случайные шары"')
    size = width, height = 500, 350
    screen = pygame.display.set_mode(size)
    running = True

    pos = (-100, -100)
    r = 50
    color = (0, 0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                pos = (random.randrange(50, screen.get_width()-50), random.randrange(50, screen.get_height()-50))
                color = (random.randrange(255), random.randrange(255), random.randrange(255))
        screen.fill("white")
        pygame.draw.circle(screen, color, pos, r)
        pygame.display.flip()
    pygame.quit()

def game2():
    pygame.init()
    pygame.display.set_caption('Задание "Круги RGB and White"')
    size = 500, 350
    screen = pygame.display.set_mode(size)
    running = True

    pos = (250, 175)
    r = 50
    color = "white"
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = "red"
                elif event.key == pygame.K_g:
                    color = "green"
                elif event.key == pygame.K_b:
                    color = "blue"
                else:
                    color = "white"
        screen.fill("black")
        pygame.draw.circle(screen, color, pos, r)
        pygame.display.flip()
    pygame.quit()

def game3():
    pygame.init()
    pygame.display.set_caption('Задание 4.15 "Управляем объектом"')
    size = 500, 350
    screen = pygame.display.set_mode(size)
    running = True

    pos_x = 250
    pos_y = 175
    r = 50
    color = "blue"
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pos_x += 5
                elif event.key == pygame.K_LEFT:
                    pos_x -= 5
                elif event.key == pygame.K_UP:
                    pos_y -= 5
                elif event.key == pygame.K_DOWN:
                    pos_y += 5
        screen.fill("white")
        pygame.draw.circle(screen, color, (pos_x, pos_y), r)
        pygame.display.flip()
    pygame.quit()

def game4():
    pygame.init()
    pygame.display.set_caption('Задание 4.16 "Делаем апгрейд программы"')

    FPS = 60
    size = width, height = 600, 300
    WHITE = (255, 255, 255)
    BLUE = (0, 70, 225)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    # координаты и радиус круга
    x = width // 2
    y = height // 2
    r = 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    running = False

        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (x, y), r)
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 3
        if keys[pygame.K_RIGHT]:
            x += 3
        if keys[pygame.K_UP]:
            y -= 3
        if keys[pygame.K_DOWN]:
            y += 3
        pygame.display.flip()
    pygame.quit()

def game5():
    pygame.init()
    pygame.display.set_caption('Задание 4.17 "Карантин"')

    FPS = 60
    size = width, height = 600, 300
    WHITE = (255, 255, 255)
    BLUE = (0, 70, 225)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    # координаты и радиус круга
    x = width // 2
    y = height // 2
    r = 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    running = False

        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (x, y), r)
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if x-3 >= r:
                x -= 3
        if keys[pygame.K_RIGHT]:
            if x+3 <= screen.get_width()-r:
                x += 3
        if keys[pygame.K_UP]:
            if y-3 >= r:
                y -= 3
        if keys[pygame.K_DOWN]:
            if y+3 <= screen.get_height()-r:
                y += 3
        pygame.display.flip()
    pygame.quit()

def test1():
    x1 ,y1 ,r1 = map(int, input().split())
    x2 ,y2 ,r2 = map(int, input().split())

    if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= r1+r2:
        print("YES")
    else:
        print("NO")

def test2():
    x1 ,y1, w1, h1 = map(int, input().split())
    x2 ,y2, w2, h2 = map(int, input().split())

    if (x1 <= x2 <= x1 + w1 or x1 <= x2 + w2 <= x1 + w1) and (y1 <= y2 <= y1 + h1 or y1 <= y2 + h2 <= y1 + h1):
        print("YES")
    else:
        print("NO")

def game6():
    pygame.init()
    pygame.display.set_caption('Задание 3.18 "Загружаем картинки"')
    size = width, height = 500, 350
    screen = pygame.display.set_mode(size)
    running = True
    picture1 = pygame.image.load('005.png')
    picture2 = pygame.image.load('creature.png')
    picture1 = pygame.transform.scale(picture1, (100, 100))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("white")
        screen.blit(picture1, (screen.get_width() - picture1.get_width(), 0))
        screen.blit(picture2, (0, screen.get_height() - picture2.get_height()))
        pygame.display.flip()
    pygame.quit()

def game7():
    pygame.init()
    pygame.display.set_caption('Используя объекты задачи 3.18 реализуйте движение одного из объектов.')
    picture = pygame.image.load('creature.png')

    FPS = 60
    size = width, height = 600, 300
    WHITE = (255, 255, 255)
    x, y = 0, 0
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    running = False

        screen.fill(WHITE)
        screen.blit(picture, (x, y))
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if x-3 >= 0:
                x -= 3
        if keys[pygame.K_RIGHT]:
            if x+3 <= screen.get_width()-picture.get_width():
                x += 3
        if keys[pygame.K_UP]:
            if y-3 >= 0:
                y -= 3
        if keys[pygame.K_DOWN]:
            if y+3 <= screen.get_height()-picture.get_height():
                y += 3
        pygame.display.flip()
    pygame.quit()

game7()