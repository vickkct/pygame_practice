import pygame

def game1():
    pygame.init()
    pygame.display.set_caption('Задача 4.1 "PyGame. Создание окна игры"')
    size = width, height = 500, 350
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()

def game2():
    pygame.init()
    pygame.display.set_caption('Задание 4.6 "Анимация объекта - 1"')
    size = width, height = 500, 350
    screen = pygame.display.set_mode(size)
    running = True
    r = 30
    x = screen.get_width() - r
    v = 60
    clock = pygame.time.Clock()
    color = (0, 255, 0)
    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if x >= r:
            x -= v * clock.tick() / 1000
        else:
            color = (255, 0, 0)
        pygame.draw.circle(screen, color, (x, screen.get_height()-r), r)
        pygame.display.flip()
    pygame.quit()

def game3():
    pygame.init()
    pygame.display.set_caption('Задание 4.7 "Анимация объекта - 2"')
    size = width, height = 500, 350
    screen = pygame.display.set_mode(size)
    running = True
    r = 30
    x = screen.get_width() - r
    v = -120
    clock = pygame.time.Clock()
    color = (0, 255, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        if x < r or x > screen.get_width() - r:
            v = -v
        x += v * clock.tick() / 1000
        pygame.draw.circle(screen, color, (x, screen.get_height()-r), r)
        pygame.display.flip()
    pygame.quit()

def game4():
    pygame.init()
    pygame.display.set_caption('Задание 4.8 "Анимация объекта - 3. Перевозка"')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    is_finish = False

    x = 0
    y = 0
    v = 200
    border = 3
    r = 100

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        if is_finish:
            screen.fill("yellow")
            # pygame.draw.rect(screen, "yellow", (0, 0, screen.get_width(), screen.get_height()))
        else:
            if x <= 0 and v < 0:
                if r <= 0:
                    is_finish = True
                else:
                    border = 5
                    v = -v
            elif x >= screen.get_width()-20 and v > 0:
                r -= 40
                border = 0
                v = -v

            tick = clock.tick()
            x += v * tick / 1000
            y += v * tick / 1000

            pygame.draw.rect(screen, "green", (x, y, 20, 20), border)
            pygame.draw.circle(screen, "red", (400, 100), r)
        pygame.display.flip()
    pygame.quit()

def game5():
    pygame.init()
    pygame.display.set_caption('Задание 4.9 "Вслед за курсором" - выключение по нажатию')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True

    is_visible = True
    x = 0
    y = 0

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                (x, y) = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_visible = not is_visible
        screen.fill("black")
        if is_visible: pygame.draw.circle(screen, "blue", (x, y), 25)
        pygame.display.flip()
    pygame.quit()

def game5_2():
    pygame.init()
    pygame.display.set_caption('Задание 4.9 "Вслед за курсором" - выключение если не двигать')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True

    is_visible = True
    x = 0
    y = 0

    clock = pygame.time.Clock()
    while running:
        is_visible = False;
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                is_visible = True
                (x, y) = event.pos
        screen.fill("black")
        if is_visible: pygame.draw.circle(screen, "blue", (x, y), 25)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def game6_circle():
    size = width, height = 400, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Задание 4.10 "Рисовалка". Круг')

    clock = pygame.time.Clock()
    count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()

def game6_rect():
    size = width, height = 400, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Задание 4.10 "Рисовалка". Квадрат')

    clock = pygame.time.Clock()
    count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                pygame.draw.rect(screen, (0, 0, 255), (x, y, 15, 15))
        pygame.display.flip()
    pygame.quit()

def game7():
    pygame.init()
    pygame.display.set_caption('Задание 4.11 "ЛКМ-ПКМ"')
    size = width, height = 500, 350
    screen = pygame.display.set_mode(size)
    running = True
    x, y = 0, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill("black")
                x, y = event.pos
                if event.button == 1:
                    pygame.draw.circle(screen, "blue", (x, y), 50)
                if event.button == 3:
                    pygame.draw.rect(screen, "red", (x-50, y-50, 100, 100))
        pygame.display.flip()
    pygame.quit()

def game8():
    pygame.init()
    pygame.display.set_caption('"ЛКМ-ПКМ - 2"')
    font = pygame.font.SysFont("Times New Roman", 15)
    size = width, height = 500, 350
    screen = pygame.display.set_mode(size)
    running = True

    count_circles = 0
    count_rect = 0
    x, y = 0, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill("black")
                x, y = event.pos
                if event.button == 1:
                    pygame.draw.circle(screen, "blue", (x, y), 50)
                    count_circles += 1
                if event.button == 3:
                    pygame.draw.rect(screen, "red", (x-50, y-50, 100, 100))
                    count_rect += 1
        string = "Кругов - " + str(count_circles) + ", Квадратов - " + str(count_rect)
        screen_text = font.render(string, False, "yellow")
        screen.blit(screen_text, (0, 0))
        pygame.display.flip()
    pygame.quit()

def game9():
    pygame.init()
    pygame.display.set_caption('Задание 4.12 "Перемещение объекта"')
    size = 500, 350
    screen = pygame.display.set_mode(size)

    x0 = 0
    y0 = 0
    dx = -1
    dy = -1

    width = 80

    running = True
    pygame.draw.rect(screen, "green", (x0, y0, width, width))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0]-x0 <= width and event.pos[1] - y0 <= width:
                    dx = event.pos[0] - x0
                    dy = event.pos[1] - y0
            elif event.type == pygame.MOUSEBUTTONUP:
                dx = -1
                dy = -1
            elif event.type == pygame.MOUSEMOTION:
                if dx >= 0:
                    x0 = event.pos[0] - dx
                    y0 = event.pos[1] - dy
                    screen.fill("black")
                    pygame.draw.rect(screen, "green", (x0, y0, width, width))
        pygame.display.flip()
    pygame.quit()

def game10():
    pygame.init()
    pygame.display.set_caption('Задание 4.12 "Перемещение объекта"')
    font = pygame.font.SysFont("Times New Roman", 15)
    size = 500, 350
    screen = pygame.display.set_mode(size)

    x0 = 0
    y0 = 0
    dx = -1
    dy = -1

    width = 80

    count = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0]-x0 <= width and event.pos[1] - y0 <= width:
                    dx = event.pos[0] - x0
                    dy = event.pos[1] - y0
            elif event.type == pygame.MOUSEBUTTONUP:
                if dx >= 0:
                    count += 1
                dx = -1
                dy = -1
            elif event.type == pygame.MOUSEMOTION:
                if dx >= 0:
                    x0 = event.pos[0] - dx
                    y0 = event.pos[1] - dy
        screen.fill("black")
        pygame.draw.rect(screen, "green", (x0, y0, width, width))
        string = "Перетягиваний - " + str(count)
        screen_text = font.render(string, False, "yellow")
        screen.blit(screen_text, (0, 0))
        pygame.display.flip()
    pygame.quit()

game10()
