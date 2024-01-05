import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Dohyun's drawing game")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    background.fill((255,255,255))
    # 아래는 선을 그리기 위한 기본 코드
    # pygame.draw.line(화면, 색, 시작위치, 끝위치, 선 굵기)
    # pygame.draw.line(background, (0,0,0), (240,0), (240,360))
    # pygame.draw.line(background, (0,0,0), (0,180), (480,180))
    # pygame.draw.line(background, (0,0,0), (0,0), (480,360), 5)
    # pygame.draw.line(background, (0,0,0), (0,360), (480,0), 5)

    # for 문으로도 가능하다
    # for i in range(시작, 끝, 간격)
    # p~..line(위치, 색상, 시작점, 종료점)
    for i in range(0,480,30):
        pygame.draw.line(background, (0,0,0), (i,0), (i,360))
    for i in range(0, 360, 30):
        pygame.draw.line(background, (0,0,0), (0,i), (480,i))
    pygame.display.update()

pygame.quit()



