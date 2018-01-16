import pygame, sys

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriad_pro_font = pygame.font.SysFont("Myriad Pro", 30)
hello_world = myriad_pro_font.render("Hello, World", 1, (80,80,255),(255,255,255))
hello_world_size = hello_world.get_size()

x,y = 0,0

direction_x = 1
direction_y = 1

clock = pygame.time.Clock()

while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0,0,0))

    mouse_position = pygame.mouse.get_pos()

    # Follow the Mouse behaviour
    x, y = mouse_position
    if x + hello_world_size[0] > window_size[0]:
        x = window_size[0] - hello_world_size[0]
    if y + hello_world_size[1] > window_size[1]:
        y = window_size[1] - hello_world_size[1]

    screen.blit(hello_world,(x,y))

    # Bouncing Behaviour
    #
    # if x + hello_world_size[0] > window_size[0] or x <= 0:
    #     direction_x *= -1
    # if y + hello_world_size[1] > window_size[1] or y <= 0:
    #     direction_y *= -1
    #
    #




    pygame.display.update()
