import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Dohyun's keyboard game")

fps = pygame.time.Clock()  # 게임에서의 fps, 지정하지 않으면 컴퓨터의 연산속도를 초월하여 미친듯이 빠르게도 느리게도 한다.

x_pos = background.get_size()[0]//2
y_pos = background.get_size()[1]//2

# 상태변수를 좌우상하 각각을 두는 것이 좋다. 다루는 키는 4개인데, 변수는 2개라서 문제가 생긴다.
to_x = 0
to_y = 0

play = True
while play:
    deltaTime = fps.tick(120)  # 즉, 1초에 120번간 while문이 동작한다.
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('UP')
                to_y = -1 # 단순하게 이동하는 것이 아닌, 함수를 지정하여 그 값에서 +- 되도록 설정
            elif event.key == pygame.K_DOWN:
                print('DOWN')
                to_y = 1
            elif event.key == pygame.K_LEFT:
                print('LEFT')
                to_x = -1
            elif event.key == pygame.K_RIGHT:
                print('RIGHT')
                to_x = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y = 0
            elif event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_RIGHT:
                to_x = 0
        
    
    x_pos += to_x
    y_pos += to_y
    
    background.fill((255,255,255))
    pygame.draw.circle(background, (0,0,255), (x_pos, y_pos), 5)
    pygame.display.update()

pygame.quit()