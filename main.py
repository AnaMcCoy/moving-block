import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:
    
    screen.fill((0, 0, 0, 0))
    
    pygame.draw.rect(screen, (255,153,153),player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
    # if a is pressed
        player.move_ip(-1, 0)
        #ip = in place, moving left because minus 1 x and not moving y
    elif key[pygame.K_d] == True:
    # if d is pressed
        player.move_ip(1, 0)
        #ip = in place, moving right because plus 1 x and not moving y
    if key[pygame.K_w] == True:
    # if w is pressed
        player.move_ip(0, -1)
        #ip = in place, moving up because not moving x and minus 1 y
    if key[pygame.K_s] == True:
    # if s is pressed
        player.move_ip(0, 1)
        #ip = in place, moving down because not moving x and plus 1 y
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()