import pygame
pygame.init()
screen = pygame.display.set_mode((1280,800))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill('#919191')
    pygame.draw.rect(screen,'yellow',(250,350,50,50))
    pygame.draw.rect(screen,'green',(0,700,1280,100))
    pygame.draw.rect(screen,'red',(1210,0,70,300))
    pygame.draw.rect(screen,'red',(1210,450,70,250))
    pygame.draw.rect(screen,'red',(930,0,70,150))
    pygame.draw.rect(screen,'red',(930,300,70,400))
    pygame.draw.rect(screen,'red',(650,0,70,250))
    pygame.draw.rect(screen,'red',(650,400,70,300))
    pygame.draw.rect(screen,'red',(370,0,70,300))
    pygame.draw.rect(screen,'red',(370,450,70,250))
    pygame.draw.rect(screen,'red',(130,0,70,300))
    pygame.draw.rect(screen,'red',(130,450,70,250))
    pygame.draw.line(screen,'blue',(200,0),(200,800))
    pygame.draw.line(screen,'blue',(1000,0),(1000,800))
    pygame.display.update()