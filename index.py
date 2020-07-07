import pygame
import time
import random

pygame.init()

blue = [0,0,255]
red = [255,0,0]
black = [0,0,0]
white = (255, 255, 255)

dis_width = 800
dis_height = 600

snake_speed = 15
snake_block = 10
x1 = 300
y1 = 300

#for changing postion of moving snake
x1_change = 0
y1_change = 0


#display a screen
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game by Sampang')
game_over = False

clock = pygame.time.Clock()


font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)

    dis.blit(mesg, [round(dis_width/2.3), round(dis_height/2)])
 

foodx = round(random.randrange(0, dis_width-snake_block)/10) *10
foody = round(random.randrange(0, dis_height-snake_block)/10) *10

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
    
    x1 += x1_change
    y1 += y1_change
    dis.fill(black)

    pygame.draw.rect(dis, red, [foodx,foody,10,10])
    pygame.draw.rect(dis, blue, [x1,y1,10,10])

    pygame.display.update()
    clock.tick(snake_speed)
message("You Lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()