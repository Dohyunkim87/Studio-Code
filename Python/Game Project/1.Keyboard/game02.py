import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Dohyun's keyboard game")

# 각 값은 선택되어있는 display의 절반 값이다. 이는 수치로 입력이 가능하지만, 아래와 같이 입력할 수도 있다.
x_pos = background.get_size()[0]//2 #240
y_pos = background.get_size()[1]//2 #180

# print(background.get_size()) 를 통해 확인하면 480, 360을 확인할 수 있고 첫번째([0]칸), 두번째([1]칸)으로 수치를 정할 수 있다

play = True
while play:   
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            play = False
        if event.type == pygame.KEYDOWN:
            # print(event.key) 키보드를 누를때(KEYDOWN) 각 키의 아스키값을 출력한다
            if event.key==pygame.K_UP:
                print('UP')
            elif event.key==pygame.K_DOWN:
                print('DOWN')
            elif event.key==pygame.K_LEFT:
                print('LEFT')
            elif event.key==pygame.K_RIGHT:
                print('RIGHT')

pygame.quit()  

# print(pygame.K_1)   이를 통해서 각 키의 아스키값도 알 수 있다
# print(pygame.K_a)
# print(pygame.K_KP_ENTER)