import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("The penguin return")
clock = pygame.time.Clock()
ground = pygame.image.load("Ground.jpg")
sky = pygame.image.load("sky.png")
penguin = pygame.image.load("penguin.png")
snail = pygame.image.load("snail.png")

# we use get_rect method as it is easier for students to code collision as well as position the object.
# Please explain them about what get_rect actually do
# get_rect method,will draw a rectangle surrounding the penguin

penguin_rect = penguin.get_rect(midbottom=(30,320))
snail_rect = snail.get_rect(midbottom=(800,320))

#some young students might not understand the word 'gravity'. It is best to refer it as falling speed.
falling_speed = 20
direction = "right"
jump = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True

# code for penguin to jump
    if jump == True:
        penguin_rect.y -= falling_speed
        falling_speed -= 1
        #print(falling_speed)
        if falling_speed < -20:
            jump = False
            falling_speed = 20

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 320))
    screen.blit(penguin, penguin_rect)
    screen.blit(snail, snail_rect)

# Codes for penguin to move back and forth
    # step 1: set direction for penguin
    if penguin_rect.right >= 800:
        direction = "left"
    elif penguin_rect.left <= 0:
        direction = "right"
    # step 2: move penguin on x coordinate as per the direction set
    if direction == "right":
        penguin_rect.x += 1
    else:
        penguin_rect.x -= 1
# Codes for penguin to move from left to right
    snail_rect.x -= 1.5
    if snail_rect.x <= 0:
        snail_rect.x = 800

    if snail_rect.colliderect(penguin_rect):
        pygame.quit()
        exit()
   # updating the screen
    pygame.display.update()
    clock.tick(60)  # to slow down the reloading of the all the frames/object so that it is not too fast
