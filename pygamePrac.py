import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
x_pos = 50
y_pos = 50
to_x = 0
to_y = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y -= 1
            if event.key == pygame.K_DOWN:
                to_y += 1
            if event.key == pygame.K_LEFT:
                to_x -= 1
            if event.key == pygame.K_RIGHT:
                to_x += 1
        if event.type == pygame.KEYUP:
            to_x = 0
            to_y = 0
    x_pos += to_x
    y_pos += to_y
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,255,255), (x_pos,y_pos), 2)
    pygame.display.update()