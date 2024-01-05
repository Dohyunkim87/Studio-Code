import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Dohyun's mouse game")

x_pos = background.get_size()[0]//2  # 240
y_pos = background.get_size()[1]//2  # 120

fps = pygame.time.Clock()

play = True
while play:
    deltaTime = fps.tick(120) 
    for event in pygame.event.get():
        pygame.mouse.set_visible(0)  # 마우스 커서 사라지게 하는 코드
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()

        background.fill((0,0,0))
        pygame.draw.circle(background, (255,0,255), (x_pos, y_pos), 10)
        pygame.display.update()
            

pygame.quit()