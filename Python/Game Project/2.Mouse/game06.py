import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Dohyun's mouse game"

fps = pygame.time.Clock()

play = True
while play:
    deltaTime = fps.tick(120) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION
            # print('MOUSEMOTION')
            # print(pygame.mouse.get_pos())
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print('MOUSEBUTTONDOWN')
            # print(pygame.mouse.get_pos())
            # print(event.button)
            if event.button == 1:
                print('왼쪽 클릭')
            if event.button == 2:
                print('휠 클릭')
            if event.button == 3:
                print('오른쪽 클릭')
            if event.button == 4:
                print('휠 올리기')
            if event.button == 5:
                print('휠 내리기')
        if event.type == pygame.MOUSEBUTTONUP:
            # print('MOUSEBUTTONUP')
            # print(pygame.mouse.get_pos())
            pass
            

pygame.quit()