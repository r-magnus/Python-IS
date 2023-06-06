import pygame
 
pygame.init()
 
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
X = 400
Y = 400
 
display_surface = pygame.display.set_mode((X, Y))

font = pygame.font.Font(None, 32)
text = font.render('Help', True, (0,0,0))
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)

while True:

    display_surface.fill(white)
 
    display_surface.blit(text, textRect)
 
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
 
            pygame.quit()

            quit()
 
        pygame.display.update()

