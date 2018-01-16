import pygame, sys

pygame.init()
pygame.mixer.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)


hello_world = pygame.image.load("square_ball.png")
bar = pygame.image.load("bar.png")

hello_world_size = hello_world.get_size()
sound = pygame.mixer.Sound("hit_noise.wav")


pygame.mouse.set_visible(False)




x,y = 0,0
bar_x,bar_y = window_size[0]/2,window_size[1]*2/3,

direction_x = 1
direction_y = 1

clock = pygame.time.Clock()

while True:

    clock.tick(90)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_RIGHT:
                print("To the right, to the right!")
                bar_x += 2
            if event.key  == pygame.K_LEFT:
                print("To the left, to the left.")
                bar_x -= 2
            if event.key  == pygame.K_UP:
                print("And up, and up!")
                bar_y += 2
            if event.key  == pygame.K_DOWN:
                print("And down, and down.")
                bar_y -= 2

    screen.fill((0,0,0))

    mouse_position = pygame.mouse.get_pos()


    # # Follow the Mouse behaviour
    # x, y = mouse_position
    # if x + hello_world_size[0] > window_size[0]:
    #     x = window_size[0] - hello_world_size[0]
    # if y + hello_world_size[1] > window_size[1]:
    #     y = window_size[1] - hello_world_size[1]

    screen.blit(hello_world,(x,y))
    screen.blit(bar,(bar_x,bar_y))

    ## Bouncing Behaviour

    x += 2 * direction_x
    y += 2 * direction_y

    if x + hello_world_size[0] > window_size[0] or x <= 0:
        sound.stop()
        sound.play()
        direction_x *= -1
    if y + hello_world_size[1] > window_size[1] or y <= 0:
        sound.stop()
        sound.play()
        direction_y *= -1






    pygame.display.update()
