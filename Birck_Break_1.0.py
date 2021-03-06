import pygame, sys
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('brickbreak')


game = 0

ball_x = 320
ball_y = 240
ball_r = 9
Bx_move = 1
By_move = 1

paddle_x = 275
paddle_y = 470
paddle_W = 90
paddle_H = 8
Px_move = 1.4
Py_move = 1.4

bricks = []
bricks_cols = 3
bricks_rows = 7
brick_H = 20
brick_W = 75
brick_padding = 10
brick_Offsettop = 30
brick_Offsetleft = 30

key = [False, False, False]

font = pygame.font.Font(None, 70)
font2 = pygame.font.Font(None, 20)
text = font.render("GAME OVER", 0, (125, 125, 125), (240, 240, 240))
text2 = font2.render("press space to restart", 0, (125, 125, 125), (240, 240, 240))
text3 = font.render("Congratulation!", 0, (125, 125, 125), (240, 240, 240))


def Brickinit():
    global bricks_cols, bricks_rows, brick_H, brick_W, brick_padding, brick_Offsettop, brick_Offsetleft
    for col in range(bricks_cols):
        for row in range(bricks_rows):
            state = 1
            x = brick_Offsetleft + row*(brick_W + brick_padding)
            y = brick_Offsettop + col*(brick_H + brick_padding)
            bricks.append([x, y, state])

def data_update():
    global ball_x, ball_y, Bx_move, By_move, paddle_x, paddle_y, game

    if ball_x <= ball_r/2 or ball_x >= 640 - ball_r/2:
        Bx_move = -Bx_move
    if ball_y <= ball_r/2:
        By_move = -By_move
    if ball_y >= 480:
        game = 1
        return
    if ball_y >= 480 - paddle_H - ball_r/2 and paddle_x + paddle_W >= ball_x >= paddle_x:
        By_move = -By_move
    ball_x += Bx_move
    ball_y += By_move

    game = 2
    for brick in bricks:
        if brick[2] == 1:
            game = 0
            if brick[0] <= ball_x <= brick[0] + brick_W and brick[1] <= ball_y - ball_r/2 <= brick[1] + brick_H:
                By_move = -By_move
                brick[2] = 0
    else:
        if game == 2:
            return

    if key[0] == True and paddle_x >= 0:
        paddle_x -= Px_move
    if key[1] == True and paddle_x + paddle_W <= 640:
        paddle_x += Px_move

def draw_ball():
    pygame.draw.circle(screen, (60, 180, 255), (ball_x, ball_y), ball_r, 0)

def draw_brick():
    global bricks_cols, bricks_rows, brick_H, brick_W, brick_padding, brick_Offsettop, brick_Offsetleft, bricks
    for brick in bricks:
        if brick[2] == 1:
            pygame.draw.rect(screen, (255, 60, 180), (brick[0], brick[1], brick_W, brick_H), 0)

def draw_paddle():
    pygame.draw.rect(screen, (60, 150, 255), (paddle_x, paddle_y, paddle_W, paddle_H), 0)

def draw():
    draw_ball()
    draw_paddle()
    draw_brick()

Brickinit()

while True:
    screen.fill((240, 240, 240))
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                key[0] = True
            if event.key == K_RIGHT:
                key[1] = True
            if event.key == K_SPACE:
                key[2] = True

        if event.type == KEYUP:
            if event.key == K_LEFT:
                key[0] = False
            if event.key == K_RIGHT:
                key[1] = False
            if event.key == K_SPACE:
                key[2] = False


    if game == 0:
        data_update()
        draw()
    elif game == 1:
        screen.blit(text, (180, 200))
        screen.blit(text2, (250, 250))

        if key[2] == True:
            ball_x = 320
            ball_y = 240
            paddle_x = 275
            paddle_y = 470
            bricks = []
            Brickinit()
            game = 0
    else:
        screen.blit(text3, (150, 200))
        screen.blit(text2, (250, 250))

        if key[2] == True:
            ball_x = 320
            ball_y = 240
            paddle_x = 275
            paddle_y = 470
            bricks = []
            Brickinit()
            game = 0


    pygame.time.delay(5)
    pygame.display.update()