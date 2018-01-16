import pygame, sys
from GameObject import GameObject

# Initialize PyGame
pygame.init()
pygame.mixer.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()


# Load Resources
ball_image = pygame.image.load("square_ball.png")
pad_image = pygame.image.load("bar.png")
sound = pygame.mixer.Sound("hit_noise.wav")

ball_size = ball_image.get_size()
pad_size = pad_image.get_size()

x,y = 0,0
direction_x, direction_y = 1, 1

def play_sound():
    sound.stop()
    sound.play()

pad = GameObject(window_size[0]/2,window_size[1]*2/3,pad_size[0],pad_size[1])
ball = GameObject(0,0,ball_size[0],ball_size[1])



while True:

    clock.tick(90)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_RIGHT:
                print("To the right, to the right!")
                pad.x += 2
            if event.key  == pygame.K_LEFT:
                print("To the left, to the left.")
                pad.x -= 2
            if event.key  == pygame.K_UP:
                print("And up, and up!")
                pad.y += 2
            if event.key  == pygame.K_DOWN:
                print("And down, and down.")
                pad.y -= 2

    screen.fill((0,0,0))

    screen.blit(ball_image,(ball.x,ball.y))
    screen.blit(pad_image,(pad.x,pad.y))



    ## Bouncing Behaviour

    ball.x += 2 * direction_x
    ball.y += 2 * direction_y

    if ball.x + ball_size[0] > window_size[0] or ball.x <= 0:
        play_sound()
        direction_x *= -1
    if ball.y + ball_size[1] > window_size[1] or ball.y <= 0:
        play_sound()
        direction_y *= -1
    if ball.intersects(pad):
        print("yes!")
        play_sound()
        direction_y *= -1





    pygame.display.update()
