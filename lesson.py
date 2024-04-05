#https://clipart.com/
#https://www.klipartz.com/

import pygame
pygame.init()
import time

winddow_size = (800, 600)
screen = pygame.display.set_mode(winddow_size)
pygame.display.set_caption('тестовый проект')
image1 = pygame.image.load('python.png')
image_rect1 = image1.get_rect()

image2 = pygame.image.load('kip.png')
image_rect2 = image2.get_rect()

#speed = 2# скорость движения #стрелками движение

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX - 40
            image_rect1.y = mouseY - 40

    if image_rect1.colliderect(image_rect2):
        print("столкновение")
        time.sleep(1)

    #keys = pygame.key.get_pressed()#стрелками движение
    #if keys[pygame.K_LEFT]:
        #image_rect.x -= speed
    #if keys[pygame.K_RIGHT]:
        #mage_rect.x += speed
    #if keys[pygame.K_UP]:
        #image_rect.y -= speed
    #if keys[pygame.K_DOWN]:
        #image_rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

pygame.quit()
