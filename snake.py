import pygame
import random

dis_height = 600
dis_weight = 800
pygame.init()

dis = pygame.display.set_mode((dis_weight, dis_height))

# pygame.display.update()
pygame.display.set_caption('(Название игры)Snake by PraonardIndustries')

# Color
yellow=(255,255,122)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
# цикл для того чтобы змейка не закрывалась моментально
# пока переменная .игра окончена. 0 выполняется:
game_over = False
game_close = False
# Доп переменные чендж для изменения икса и игрика
# x1=dis_weight/2
# y1=dis_height/2
clock = pygame.time.Clock()
snake_block = 10

# x1_change=0
# y1_change=0


snakes_speed = 20
# Шрифт подписи
font_style = pygame.font.SysFont('bahnschrift', 30)
score_font = pygame.font.SysFont('comicsansms', 35)

def Your_score(score):
    value=score_font.render('You score :'+str(score),True,yellow)
    dis.blit(value,[0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block],2)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_weight / 3.7, dis_height / 2.6])


# ------------------------------------#
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_weight / 2
    y1 = dis_height / 2

    snake_list = []
    Length_of_snake = 1
    x1_change = 0
    y1_change = 0
    foodx = round(random.randrange(snake_block, dis_weight - snake_block) / 10.0) * 10
    foody = round(random.randrange(snake_block, dis_height - snake_block) / 10.0) * 10
    # -----------------------------------#
    while not game_over:

        while game_close == True:

            dis.fill(black)
            message('Press Q- to quit or S-to play again', red)
            Your_score(Length_of_snake // 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_s:
                        gameLoop()
                    if event.type == pygame.QUIT:
                        game_over = True
                    if event.type == pygame.QUIT:
                        game_close = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            # эвенты змейки,конкретно ее движение
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        # Условия выхода из игры:
        if x1 >= dis_weight or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # Изменение координат змейки
        x1 += x1_change
        y1 += y1_change
        # закраска полей черным (0,0,0)
        dis.fill(black)
        # рисование головы змеи
        #pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append((snake_Head))
        if len(snake_list) > Length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_list)
        Your_score(Length_of_snake // 50)
        # Параметры куска змейки
        #    pygame.draw.rect(dis,blue,(200,150,10,10))

        # Изменение экрана(перезапись полностью)
        pygame.display.update()
        # (Закоменчено так как не нужно(координаты))print(event)#выводит на экран все действия игры(ее нет)

        if x1 == foodx and y1 == foody:
            message('BRUH', red)
            foodx = round(random.randrange(snake_block, dis_weight - snake_block) / 10.0) * 10
            foody = round(random.randrange(snake_block, dis_height - snake_block) / 10.0) * 10
            Length_of_snake += 50
            pygame.display.update()
        #print(foodx, foody)
        clock.tick(snakes_speed)
        #print(event)
        #message()
    # частота изменения кадров,другими словами скорость змейки
    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()
    quit()


print('Hello!\nYou are in cosole:')
gameLoop()
