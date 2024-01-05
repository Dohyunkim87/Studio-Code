import pygame

pygame.init()

background = pygame.display.set_mode((480,360))  # 480, 360 창 만들기!
pygame.display.set_caption("Dohyun's mouse game")  # 이 디스플레이 이름은 요거!

fps = pygame.time.Clock()

play = True
while play:  # 플레이가 참일 때 작동하는 while 문!
    deltaTime = fps.tick(120) 
    for event in pygame.event.get():  # 작동 중일때 이벤트 for - in
        if event.type == pygame.QUIT:    # play가 거짓이면 종료
            play = False
        if event.type == pygame.MOUSEMOTION:  # 마우스 이동시 메시지 띄우기
            print('MOUSEMOTION')

        if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 버튼 누를 시 띄우기
            print('MOUSEBUTTONDOWN')

        if event.type == pygame.MOUSEBUTTONUP:  # 마우스 버튼 땔 때 띄우기
            print('MOUSEBUTTONUP')

            

pygame.quit()