import pygame
import time
import random

pygame.init()

blue = [0,0,255]
red = [255,0,0]
black = [0,0,0]
white = (255, 255, 255)
yellow = (255, 255, 102)    

dis_width = 800
dis_height = 600

snake_speed = 30
snake_block = 10


#display a screen
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game by Sampang')

clock = pygame.time.Clock()


font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [round(1), round(dis_height/2)])
 
def snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, blue, [x[0],x[1],snake_block,snake_block])

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

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

    snake_List = []
    Length_of_snake = 1
    direction = ''

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
                keyPressed = event.key
                if keyPressed == pygame.K_LEFT and direction!='right':
                    x1_change = -10
                    y1_change = 0
                    direction = 'left'
                if keyPressed == pygame.K_RIGHT and direction!='left':
                    x1_change = 10
                    y1_change = 0
                    direction = 'right'
                if keyPressed == pygame.K_UP and direction!='down':
                    x1_change = 0
                    y1_change = -10
                    direction = 'up'
                if keyPressed == pygame.K_DOWN and direction!='up':
                    x1_change = 0
                    y1_change = 10
                    direction = 'down'
        

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis, red, [foodx,foody,snake_block,snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List)>Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width-snake_block)/10) *10
            foody = round(random.randrange(0, dis_height-snake_block)/10) *10
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()