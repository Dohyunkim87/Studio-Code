import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Dohyun's mouse game")

x_pos = 0
y_pos = 0

fps = pygame.time.Clock()

play = True
while play:
    deltaTime = fps.tick(120) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()
            pygame.draw.circle(background, (255,0,255), (x_pos, y_pos), 10)
            # 마우스 이동 궤적을 따라 핑크색의 원을 계속 그리게 된다
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                background.fill((0,0,0))
            # 마우스 버튼을 누를때 마다 백그라운드를 검정색으로 다시 칠하게 된다
        
        pygame.display.update()
            

pygame.quit()