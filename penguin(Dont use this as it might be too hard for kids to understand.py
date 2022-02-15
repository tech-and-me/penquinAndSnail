import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("The Snails")
clock = pygame.time.Clock()
ground = pygame.image.load("Ground.jpg")
sky = pygame.image.load("sky.png")
penguin = pygame.image.load("penguin.png")

# we use get_rect method as it is easier for students to code collision as well as position the object.
# Please explain them about what get_rect actually do
# get_rect method,will draw a rectangle surrounding the penguin

penguin_rect = penguin.get_rect(midbottom=(30,320))

#some young students might not understand the word 'gravity'. It is best to refer it as falling speed.
falling_speed = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                falling_speed = -10  # this will work in reverse of the falling speed

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 320))
    screen.blit(penguin, penguin_rect)

    # Gravity codes for penguin
    falling_speed += 0.5
    penguin_rect.y += falling_speed
    if penguin_rect.bottom >= 320:
        penguin_rect.bottom = 320

    # Codes for penguin to move to the right forever and if touching right edge, start again
    penguin_rect.x += 1
    if penguin_rect.right >= 800:
        penguin_rect.x = 0

    # updating the screen
    pygame.display.update()
    clock.tick(60)  # to slow down the reloading of the all the frames/object so that it is not too fast

