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


#display a screen
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game by Sampang')

clock = pygame.time.Clock()


font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [round(1), round(dis_height/2)])
 

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    #for changing postion of moving snake
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width-snake_block)/10) *10
    foody = round(random.randrange(0, dis_height-snake_block)/10) *10

    while not game_over:
        while game_close==True:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Continue again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
  
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
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis, red, [foodx,foody,10,10])
        pygame.draw.rect(dis, blue, [x1,y1,10,10])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print('Yummy!')

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()