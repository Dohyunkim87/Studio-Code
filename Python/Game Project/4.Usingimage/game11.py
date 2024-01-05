import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("Dohyun's image game")

image_bg = pygame.image.load("/Users/dohyunkim/Studio-Code/Python/Game Project/4.Usingimage/1.jpeg")
image_banana = pygame.image.load("/Users/dohyunkim/Studio-Code/Python/Game Project/4.Usingimage/2.jpeg")
image_monkey = pygame.image.load("/Users/dohyunkim/Studio-Code/Python/Game Project/4.Usingimage/3.jpeg")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_banana_width = image_banana.get_rect().size[0]
size_banana_height = image_banana.get_rect().size[1]

x_pos_banana = size_bg_width/2 - size_banana_width/2
y_pos_banana = 0

size_monkey_width = image_monkey.get_rect().size[0]
size_monkey_height = image_monkey.get_rect().size[1]

x_pos_monkey = size_bg_width/2 - size_monkey_width/2
y_pos_monkey = size_bg_height - size_monkey_height

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        background.blit(image_bg, (0,0))
        background.blit(image_monkey, (x_pos_monkey, y_pos_monkey))
        background.blit(image_banana, (x_pos_banana, y_pos_banana))
        pygame.display.update()

pygame.quit()