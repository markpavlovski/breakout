import pygame, sys

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriad_pro_font = pygame.font.SysFont("Myriad Pro", 30)
hello_world = myriad_pro_font.render("_", 1, (80,80,255),(255,255,255))
hello_world_size = hello_world.get_size()

print("Hello, World")

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
    screen.blit(hello_world,(x,y))



    x += 4 * direction_x
    y += 4 * direction_y


    if x + hello_world_size[0] > window_size[0] or x <= 0:
        direction_x *= -1
    if y + hello_world_size[1] > window_size[1] or y <= 0:
        direction_y *= -1






    pygame.display.update()
