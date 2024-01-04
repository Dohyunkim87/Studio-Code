import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Dohyun's keyboard game")

play = True   # while 문을 지속하기 위해서 true로 설정
while play:   # 창을 지속하려면 while 문이 참으로 작동하고 있어야한다.
    for event in pygame.event.get():   # for에서 pygame.event에서 event를 가져온다.
        # print(event.type)
        if event.type == pygame.QUIT:  # event의 type가 QUIT이면 play가 false로 바뀌고
            play = False

pygame.quit()  # 게임창을 닫는다

print(pygame.K_0)