import pygame
import sys






pygame.init()
screen = pygame.display.set_mode((1200, 800))
character_image = pygame.image.load('bug.svg')
font = pygame.font.SysFont('malgungothic', 36)
clock = pygame.time.Clock()
size =character_image.get_size()
print(size)
x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= size[0]/1
            if event.key == pygame.K_RIGHT:
                x += size[0]/1

    if x > 1200-size[0]:
        x= 1200-size[0]
    if x < 0:
        x=0
    clock.tick(60)
    screen.fill((250,250,250))
    screen.blit(character_image, (x, 100))
    a=font.render('버그', True, (255, 0, 0))
    screen.blit(a, (100,10))
    pygame.display.update()



# charater_image = pygame.