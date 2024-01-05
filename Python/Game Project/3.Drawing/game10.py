import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Dohyun's drawing game")

x = background.get_size()[0]//2  # 240
y = background.get_size()[1]//2  # 120

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    background.fill((255,255,255))
    # 각종 도형이 가능하다, 원, 사각형, 타원 등등
    # 원: circle(화면, 색, 중심좌표, 반지름, 선굵기), 선굵기 지정시에는 원의 테두리만 그려짐
    
    # pygame.draw.circle(background, (0,255,0), (240,180), 50)
    # pygame.draw.circle(background, (255,0,0), (240, 180), 50, 5)

    # 사각형: rect(화면, 색, 위치와크기(점좌표1,점좌표2,가로길이,세로길이), 선굵기)
    # 사각형의 위치에서는 점좌표1,2가 사각형의 가장 왼쪽위를 의미하므로 주의해야함
    # pygame.draw.rect(background, (0,255,0), (240,180,100,50))
    # pygame.draw.rect(background, (0,123,123), (240,180,100,50), 5)

    # 타원: ellipse(화면, 색, 위치와크기, 선굵기)
    # 사각형과 동일하나, 가상의 왼쪽 상단(꽉 찬 사각형의 기준)의 좌표
    # pygame.draw.ellipse(background, (0,255,0), (240,180,100,50))
    # pygame.draw.ellipse(background, (0,123,123), (240,180,100,50), 5)

    # 다각형: polygon(화면, 색, 점들의 위치, 선 굵기)
    # pygame.draw.polygon(background, (255,255,0), [[100,100], [0,200], [200,200]])
    # pygame.draw.polygon(background, (255,255,0), [[100,100],[0,200],[200,200]], 5)
    # pygame.draw.polygon(background, (255,255,0), ((146,0), (291,106), (236,277), (56,277),(0,106)))
    pygame.draw.polygon(background, (255,255,8), ((146,0),(291,106),(236,277),(56,277),(0,106)), 5)

    pygame.draw.line(background, (0,0,0), (x,0), (x,y*2))
    pygame.draw.line(background, (0,0,0), (0,y), (x*2,y))
    pygame.display.update()

pygame.quit()



