# imports
from asyncio.windows_events import NULL
from pickle import FALSE
import random
import pygame
import pygame.freetype
import os
pygame.init()

# set display
width = 900
height = 500
wn = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

# load images
pac_maze = pygame.image.load('pac_maze.png')
pac = [pygame.image.load('pac_1_right.jpg'), pygame.image.load('pac_2.jpg')]
starting_animation = [pygame.image.load('journey_screen.png'), pygame.image.load('genesis_screen.png'), pygame.image.load('at_first_screen.png'), pygame.image.load('then_screen.png'), pygame.image.load('white_screen.png')]
start_screen = [pygame.image.load('start_screen_s.png'), pygame.image.load('start_screen_c.png'), pygame.image.load('start_screen_l.png')]
controls = pygame.image.load('controls_screen.png')
pong_controls = pygame.image.load('controls_pong.png')
breakout_controls = pygame.image.load('controls_breakout.png')
pac_controls = pygame.image.load('controls_pac.png')
win_screen = pygame.image.load('win_screen.jpg ')
ghost = [pygame.image.load('ghost_red.png'), pygame.image.load('ghost_blue.png')]

# clock
clock = pygame.time.Clock()

# game loop variable
game = True
start = True
select_screen = True
control_screen = False
leaderboard_check = False
selector = 0
move_ticker = 10
instructions_check = True
game_font = pygame.freetype.Font("PressStart2P-Regular.ttf", 70)
osCommandString = "notepad.exe final_leaderboard.txt"

# pong variables
pong = False
pong_rect_x = 25
pong_rect_y = height/2 - 40

pong_circ_x = 450
pong_circ_y = 250
pong_circ_dir_x = -6
pong_circ_dir_y = -6

pong_enemy_x = 875
pong_enemy_y = height/2 - 40
pong_enemy_tracker = True

# breakout variables
breakout = False
breakout_start = False
breakout_rect_x = width
breakout_rect_y = height - 25

breakout_circ_x = 449
breakout_circ_y = breakout_rect_y - 10 - 10
breakout_circ_dir_x = -6
breakout_circ_dir_y = -6

breakout_brick_x1 = [210, 308, 406, 504, 602]
breakout_brick_x2 = [210, 308, 406, 504, 602]
breakout_brick_x3 = [210, 308, 406, 504, 602]
breakout_brick_width = 88
breakout_brick_height = 15
breakout_brick_gap = 5
breakout_row_1_y  = 150
breakout_row_2_y = breakout_row_1_y - breakout_brick_height - breakout_brick_gap
breakout_row_3_y = breakout_row_2_y - breakout_brick_height - breakout_brick_gap
border_1_start = [200, 0]
border_1_end = [200, height]
border_2_start = [700, 0]
border_2_end = [700, height]

# pac man variables
pac_man = False
pac_start = False
pac_maze_y = -400
pac_maze_x = 180
pac_x = 410 - 35/2
pac_y = 220 - 35/2
pac_left = False
pac_right = False
pac_up = False
pac_down = False
t = True
f = False
f1 = [f, f, f, f, f, f, f, f, f, f, f, f]
f2 = [f, f, f, t, t, t, t, t, t, f, f, f]
f3 = [f, f, t, t, f, f, f, f, t, t, f, f]
f4 = [f, t, t, t, t, t, t, t, t, t, t, f]
f5 = [f, t, f, t, f, t, t, f, t, f, t, f]
f6 = [f, t, f, t, f, f, f, f, t, f, t, f]
f7 = [f, t, t, t, t, t, t, t, t, t, t, f]
f8 = [f, f, t, t, f, f, f, f, t, t, f, f]
f9 = [f, f, f, t, t, t, t, t, t, f, f, f]
f10 = [f, f, f, f, f, f, f, f, f, f, f, f]
food = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
animation_select = 0
g_coords = [5, 4]
win_count = 0
g1 = [f, f, f, f, f, f, f, f, f, f, f, f]
g2 = [f, f, f, t, t, t, t, t, t, f, f, f]
g3 = [f, f, t, t, f, f, f, f, t, t, f, f]
g4 = [f, t, t, t, t, t, t, t, t, t, t, f]
g5 = [f, t, f, t, f, t, t, f, t, f, t, f]
g6 = [f, t, f, t, f, f, f, f, t, f, t, f]
g7 = [f, t, t, t, t, t, t, t, t, t, t, f]
g8 = [f, f, t, t, f, f, f, f, t, t, f, f]
g9 = [f, f, f, t, t, t, t, t, t, f, f, f]
g10 = [f, f, f, f, f, f, f, f, f, f, f, f]
grid = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]
ghost1_vel = 5
ghost2_vel = 5
ghost3_vel = -5
ghost4_vel = -5
ghost1_x = 330 - 35/2 + 160
ghost1_y = 100 - 35/2
ghost2_x = 330 - 35/2 + 160
ghost2_y = 100 - 35/2 + 280
ghost1_grid = [8,1]
ghost2_grid = [8, 8]
ghost3_x = 330 - 35/2 - 80
ghost3_y = 100 - 35/2 + 80
ghost3_grid = [1, 3]
ghost4_x = 330 - 35/2 - 80
ghost4_y = 100 - 35/2 + 200
ghost4_grid = [1, 6]

# restart game
def restart():
    global game, control_screen, leaderboard_check, selector, move_ticker, instructions_check, select_screen
    global pong, pong_rect_x, pong_rect_y, pong_circ_x, pong_circ_y, pong_circ_dir_x, pong_circ_dir_y, pong_enemy_x, pong_enemy_y, pong_enemy_tracker
    global breakout, breakout_start, breakout_rect_x, breakout_rect_y, breakout_circ_x, breakout_circ_y, breakout_circ_dir_x, breakout_circ_dir_y, breakout_brick_x1, breakout_brick_x2, breakout_brick_x3, breakout_brick_width, breakout_brick_height, breakout_brick_gap, breakout_row_1_y , breakout_row_2_y, breakout_row_3_y, border_1_start, border_1_end, border_2_start, border_2_end
    global pac_man, pac_start, pac_maze_y, pac_maze_x, pac_x, pac_y, pac_left, pac_right, pac_up, pac_down, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, food, animation_select, g_coords, win_count, ghost1_vel, ghost2_vel, ghost3_vel, ghost4_vel, ghost1_x, ghost1_y, ghost2_x, ghost2_y ,ghost3_x, ghost3_y, ghost4_x, ghost4_y, ghost1_grid, ghost2_grid, ghost3_grid, ghost4_grid, win_check

    # resets game loop variable
    game = True
    select_screen = True
    control_screen = False
    leaderboard_check = False
    selector = 0
    move_ticker = 10
    instructions_check = True

    # resets pong variables
    pong = False
    pong_rect_x = 25
    pong_rect_y = height/2 - 40
    pong_circ_x = 450
    pong_circ_y = 250
    pong_circ_dir_x = -6
    pong_circ_dir_y = -6
    pong_enemy_x = 875
    pong_enemy_y = height/2 - 40
    pong_enemy_tracker = True

    # breakout variables
    breakout = False
    breakout_start = False
    breakout_rect_x = width
    breakout_rect_y = height - 25
    breakout_circ_x = 449
    breakout_circ_y = breakout_rect_y - 10 - 10
    breakout_circ_dir_x = -6
    breakout_circ_dir_y = -6
    breakout_brick_x1 = [210, 308, 406, 504, 602]
    breakout_brick_x2 = [210, 308, 406, 504, 602]
    breakout_brick_x3 = [210, 308, 406, 504, 602]
    breakout_brick_width = 88
    breakout_brick_height = 15
    breakout_brick_gap = 5
    breakout_row_1_y  = 150
    breakout_row_2_y = breakout_row_1_y - breakout_brick_height - breakout_brick_gap
    breakout_row_3_y = breakout_row_2_y - breakout_brick_height - breakout_brick_gap
    border_1_start = [200, 0]
    border_1_end = [200, height]
    border_2_start = [700, 0]
    border_2_end = [700, height]

    # pac man variables
    pac_man = False
    pac_start = False
    pac_maze_y = -400
    pac_maze_x = 180
    pac_x = 410 - 35/2
    pac_y = 220 - 35/2
    pac_left = False
    pac_right = False
    pac_up = False
    pac_down = False
    f1 = [f, f, f, f, f, f, f, f, f, f, f, f]
    f2 = [f, f, f, t, t, t, t, t, t, f, f, f]
    f3 = [f, f, t, t, f, f, f, f, t, t, f, f]
    f4 = [f, t, t, t, t, t, t, t, t, t, t, f]
    f5 = [f, t, f, t, f, t, t, f, t, f, t, f]
    f6 = [f, t, f, t, f, f, f, f, t, f, t, f]
    f7 = [f, t, t, t, t, t, t, t, t, t, t, f]
    f8 = [f, f, t, t, f, f, f, f, t, t, f, f]
    f9 = [f, f, f, t, t, t, t, t, t, f, f, f]
    f10 = [f, f, f, f, f, f, f, f, f, f, f, f]
    food = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    animation_select = 0
    g_coords = [5, 4]
    win_check = 0
    ghost1_vel = 5
    ghost2_vel = 5
    ghost1_x = 330 - 35/2 + 160
    ghost1_y = 100 - 35/2
    ghost2_x = 330 - 35/2 + 160
    ghost2_y = 100 - 35/2 + 280
    ghost1_grid = [8,1]
    ghost2_grid = [8, 8]


    # pong functions
# draw pong rect function
def drawPongRect():
    pygame.draw.rect(wn, (255, 255, 255), (pong_rect_x, pong_rect_y, 15, 80))
    pygame.display.update()

# draw mid line function
def drawMidLine():
    pygame.draw.line(wn, (240, 240, 240), (width/2, 0), (width/2, height), 3)
    pygame.display.update()

# draw pong ball function
def drawPongBall():
    global pong_circ_x
    global pong_circ_y
    global pong_circ_dir_x
    global pong_circ_dir_y

    # detects if pong ball hits side wall and changes direction
    if pong_circ_y <= 10:
        pong_circ_dir_y *= -1
    if pong_circ_y >= height - 10:
        pong_circ_dir_y *= -1
    # detects if pong ball hits either paddle and changes direction and speed
    if pong_circ_x <= pong_rect_x + 15 + 10 and pong_rect_y <= pong_circ_y <= pong_rect_y + 80:
        pong_circ_dir_x *= -1.10
        pong_circ_dir_y *= 1.10
    if pong_circ_x >= pong_enemy_x and pong_enemy_y <= pong_circ_y <= pong_enemy_y + 80:
        pong_circ_dir_x *= -1.10
        pong_circ_dir_y *= 1.10

    # moves pong ball
    pong_circ_x += pong_circ_dir_x
    pong_circ_y += pong_circ_dir_y

    pygame.draw.circle(wn, (255, 255, 255), (pong_circ_x, pong_circ_y), 10)
    pygame.display.update()

    # detects if pong ball gets pass either player
    if pong_circ_x <= 0:
        restart()
    if pong_circ_x >= width:
        startBreakout()

# draw pong enemy rect function
def drawPongEnemy():
    global pong_enemy_x
    global pong_enemy_y

    # enables the enmy paddle to track the balls movement
    pong_enemy_vel = 9
    if pong_enemy_tracker:
        if pong_enemy_y + 40 < pong_circ_y:
            pong_enemy_y += pong_enemy_vel
        elif pong_enemy_y + 40 > pong_circ_y:
            pong_enemy_y -= pong_enemy_vel

    pygame.draw.rect(wn, (255, 255, 255), (pong_enemy_x, pong_enemy_y, 15, 80))
    pygame.display.update()

# draw pong controls function
def drawPongControls():
    wn.blit(pong_controls, (100, -100))
    pygame.display.update()

    # breakout functions
# transition to breakout function
def startBreakout():
    global pong_rect_x
    global pong_rect_y
    global pong_circ_x
    global pong_circ_y
    global pong_circ_dir_x
    global pong_circ_dir_y
    global pong_enemy_x
    global pong_enemy_y
    global pong_enemy_tracker
    global breakout_rect_x
    global breakout_rect_y
    global pong
    global breakout
    global breakout_circ_y

    # ends the pong loop and transfers all the breakout images to the main screen
    pong_enemy_tracker = False
    pong_circ_dir_x = 0
    pong_circ_dir_y = 0
    for i in range(5500):
        wn.fill((0, 0, 0))
        pong_rect_x -= .25
        pong_enemy_x -= .25
        if pong_circ_x >= width/2:
            pong_circ_x -= .25
        else:
            if breakout_rect_x >= width/2 - 50:
                breakout_rect_x -= .25
            if pong_circ_y <= breakout_rect_y - 10 - 10:
                pong_circ_y += .1
            elif pong_circ_y >= breakout_rect_y - 10 - 10:
                pong_circ_y -= .1
        pygame.draw.rect(wn, (255, 255, 255), (breakout_rect_x, breakout_rect_y, 100, 15)) 
        pygame.draw.circle(wn, (255, 255, 255), (pong_circ_x, pong_circ_y), 10)
        pygame.draw.rect(wn, (255, 255, 255), (pong_rect_x, pong_rect_y, 15, 80))
        pygame.draw.rect(wn, (255, 255, 255), (pong_enemy_x, pong_enemy_y, 15, 80))
        pygame.display.update()
    pong = False
    breakout = True

# draw breakout rect
def drawBreakoutRect():
    pygame.draw.rect(wn, (255, 255, 255), (breakout_rect_x, breakout_rect_y, 100, 15))
    pygame.display.update()

# draw breakout ball function
def drawBreakoutBall():
    global breakout_circ_x
    global breakout_circ_y
    global breakout_start
    global breakout_circ_dir_x
    global breakout_circ_dir_y
    global breakout_rect_x
    global breakout_rect_y
    global breakout_brick_x1
    global breakout_brick_x2
    global breakout_brick_x3

    if breakout_start:
        # detects if the ball hits the borders and changes direction
        if breakout_circ_x <= 210:
            breakout_circ_dir_x *= -1
        if breakout_circ_x >= 690:
            breakout_circ_dir_x *= -1
        
        # detects if the ball hits the bricks, gets rid of the bricks and changes the balls direction
        for i in range(len(breakout_brick_x1)):
            if breakout_row_1_y <= breakout_circ_y <= breakout_row_1_y + 25 and breakout_brick_x1[i] <= breakout_circ_x <= breakout_brick_x1[i] + breakout_brick_width + 10:
                breakout_circ_dir_y *= -1
                breakout_brick_x1[i] = 1000
            if breakout_row_1_y <= breakout_circ_y <= breakout_row_1_y + 25 and breakout_brick_x1[i] - 10 <= breakout_circ_x <= breakout_brick_x1[i]:
                breakout_circ_dir_x *= -1
                breakout_brick_x1[i] = 1000
        
        for i in range(len(breakout_brick_x2)):
            if breakout_row_2_y <= breakout_circ_y <= breakout_row_2_y + 25 and breakout_brick_x2[i] <= breakout_circ_x <= breakout_brick_x2[i] + breakout_brick_width + 10:
                breakout_circ_dir_y *= -1
                breakout_brick_x2[i] = 1000
            if breakout_row_2_y <= breakout_circ_y <= breakout_row_2_y + 25 and breakout_brick_x2[i] - 10 <= breakout_circ_x <= breakout_brick_x2[i]:
                breakout_circ_dir_x *= -1
                breakout_brick_x2[i] = 1000

        for i in range(len(breakout_brick_x3)):
            if breakout_row_3_y <= breakout_circ_y <= breakout_row_3_y + 25 and breakout_brick_x3[i] <= breakout_circ_x <= breakout_brick_x3[i] + breakout_brick_width + 10:
                breakout_circ_dir_y *= -1
                breakout_brick_x3[i] = 1000
            if breakout_row_3_y <= breakout_circ_y <= breakout_row_3_y + 25 and breakout_brick_x3[i] - 10 <= breakout_circ_x <= breakout_brick_x3[i]:
                breakout_circ_dir_x *= -1
                breakout_brick_x3[i] = 1000
        
        # detects if the ball hits the 
        if breakout_circ_y >= breakout_rect_y -10 and breakout_rect_x <= breakout_circ_x <= breakout_rect_x + 50:
            breakout_circ_dir_y *= -1
            breakout_circ_dir_x = -6
        if breakout_circ_y >= breakout_rect_y -10 and breakout_rect_x + 50 <= breakout_circ_x <= breakout_rect_x + 100:
            breakout_circ_dir_y *= -1
            breakout_circ_dir_x = 6
        
        if breakout_circ_y <= 10:
            startPac()
        
        if breakout_circ_y >= height:
            restart()
        
        breakout_circ_x += breakout_circ_dir_x
        breakout_circ_y += breakout_circ_dir_y

    pygame.draw.circle(wn, (255, 255, 255), (breakout_circ_x, breakout_circ_y), 10)
    pygame.display.update()

# draw breakout borders function
def drawBreakoutBorders():
    pygame.draw.line(wn, (230, 230, 230), (border_1_start[0], border_1_start[1]), (border_1_end[0], border_1_end[1]), 1)
    pygame.draw.line(wn, (230, 230, 230), (border_2_start[0], border_2_start[1]), (border_2_end[0], border_2_end[1]), 1)
    pygame.display.update()

# draw breakout bricks function
def drawBreakoutBricks():
    global breakout_brick_x1
    global breakout_brick_x2
    global breakout_brick_x3
    global breakout_brick_height
    global breakout_brick_width
    global breakout_brick_gap
    global breakout_row_1_y
    global breakout_row_2_y
    global breakout_row_3_y
    
    colors = (255, 255, 0)
    
    for n in range(len(breakout_brick_x1)):
        pygame.draw.rect(wn, colors, (breakout_brick_x1[n], breakout_row_1_y, breakout_brick_width, breakout_brick_height))
    colors = (255, 255/2, 0)

    for n in range(len(breakout_brick_x2)):
        pygame.draw.rect(wn, colors, (breakout_brick_x2[n], breakout_row_2_y, breakout_brick_width, breakout_brick_height))
    colors = (255, 0, 0)

    for n in range(len(breakout_brick_x2)):
        pygame.draw.rect(wn, colors, (breakout_brick_x3[n], breakout_row_3_y, breakout_brick_width, breakout_brick_height))
    pygame.display.update()

# start pac man transition
def startPac():
    global breakout
    global breakout_row_1_y
    global breakout_row_2_y
    global breakout_row_3_y
    global breakout_brick_x1
    global breakout_brick_x2
    global breakout_brick_x3
    global breakout_brick_height
    global breakout_brick_width
    global breakout_circ_x
    global breakout_circ_y
    global breakout_start
    global breakout_circ_dir_x
    global breakout_circ_dir_y
    global breakout_rect_x
    global breakout_rect_y
    global border_1_start
    global border_1_end
    global border_2_start
    global border_2_end
    global pac_maze_x
    global pac_maze_y
    global pac_man
    global pac_maze

    breakout_circ_dir_y = 0
    breakout_circ_dir_x = 0
    circ_radius = 10
    circ_b = 255

    for i in range(7000):
        wn.fill((0, 0, 0))
        breakout_rect_y += .1
        border_1_start[1] += .15
        border_1_end[1] += .15
        border_2_start[1] += .15
        border_2_end[1] += .15

        colors = (255, 255, 0)
        for i in range(len(breakout_brick_x1)):
            breakout_row_1_y += .025
            pygame.draw.rect(wn, colors, (breakout_brick_x1[i], breakout_row_1_y, breakout_brick_width, breakout_brick_height))
        
        colors = (255, 255/2, 0)
        for i in range(len(breakout_brick_x2)):
            breakout_row_2_y += .025
            pygame.draw.rect(wn, colors, (breakout_brick_x2[i], breakout_row_2_y, breakout_brick_width, breakout_brick_height))
        
        colors = (255, 0, 0)
        for i in range(len(breakout_brick_x3)):
            breakout_row_3_y += .025
            pygame.draw.rect(wn, colors, (breakout_brick_x3[i], breakout_row_3_y, breakout_brick_width, breakout_brick_height))
        
        if breakout_circ_y <= pac_y + 35/2:
            breakout_circ_y += .1
        if circ_radius <= 35/2:
                circ_radius += .005
        else:
            if breakout_circ_x <= pac_x+35/2:
                breakout_circ_x += .15
            elif breakout_circ_x >= pac_x-35/2:
                breakout_circ_x -= .15
            else:
                wn.blit(pac_maze, (180, 40))
            if circ_radius <= 35/2:
                circ_radius += .005
            if circ_b > 0:
                circ_b -= .05
        pygame.draw.line(wn, (230, 230, 230), (border_1_start[0], border_1_start[1]), (border_1_end[0], border_1_end[1]), 1)
        pygame.draw.line(wn, (230, 230, 230), (border_2_start[0], border_2_start[1]), (border_2_end[0], border_2_end[1]), 1)
        pygame.draw.rect(wn, (255, 255, 255), (breakout_rect_x, breakout_rect_y, 100, 15))
        pygame.draw.circle(wn, (255, 255, circ_b), (breakout_circ_x, breakout_circ_y), circ_radius)
        pygame.display.update()
    pac_man = True
    breakout = False

# draw pac man maze function
def drawPacMaze():
    wn.fill((0, 0, 0))
    s_width = 10
    x = 200
    y = 50
    for i in range(12):
        for n in range(10):
            if food[n][i]:
                pygame.draw.rect(wn, (255, 255, 255), (x, y, 20, 20))
            y += 40
        x += 40
        y = 50
    wn.blit(pac_maze, (180, 40))

# draw pac man function
def drawPac():
    global pac_x, pac_y
    global pac_left, pac_right, pac_down, pac_up
    global g_coords
    global food
    global win_count
    global ghost1_x, ghost1_y, ghost1_vel, ghost2_x, ghost2_y, ghost2_vel, ghost3_x, ghost3_y, ghost3_vel, ghost4_x, ghost4_y, ghost4_vel

    vel = 5

    wn.blit(pac[0], (pac_x, pac_y))
    if pac_up and ((pac_x + 35/2) % 40 == 10) and ((pac_y + 35/2) % 40 == 20) and grid[g_coords[1] - 1][g_coords[0]]:
        food[g_coords[1]][g_coords[0]] = f
        pac[0] = pygame.image.load('pac_1_up.jpg')
        g_coords[1] -= 1
        for i in range(8):
            drawPacMaze()
            wn.blit(ghost[0], (ghost1_x, ghost1_y))
            wn.blit(ghost[0], (ghost2_x, ghost2_y))
            wn.blit(ghost[1], (ghost3_x, ghost3_y))
            wn.blit(ghost[1], (ghost4_x, ghost4_y))
            animation()
            clock.tick(27)
            pac_y -= vel
            if ghost1_x == 330 - 35/2:
                ghost1_vel *= -1
            if ghost1_x == 330 - 35/2 + 200:
                ghost1_vel *= -1
            ghost1_x += ghost1_vel
            if ghost2_x <= 330 - 35/2:
                ghost2_vel *= -1
            if ghost2_x >= 330 - 35/2 + 200:
                ghost2_vel *= -1
            ghost2_x += ghost2_vel
            if ghost3_x <= 330 - 35/2 - 80:
                ghost3_vel *= -1
            if ghost3_x >= 330 - 35/2 + 280:
                ghost3_vel *= -1
            ghost3_x += ghost3_vel
            if ghost4_x <= 330 - 35/2 - 80:
                ghost4_vel *= -1
            if ghost4_x >= 330 - 35/2 + 280:
                ghost4_vel *= -1
            ghost4_x += ghost4_vel

            if (ghost1_x == pac_x and ghost1_y == pac_y) or (ghost2_x == pac_x and ghost2_y == pac_y):
                restart()
    elif pac_right and ((pac_x + 35/2) % 40 == 10) and ((pac_y + 35/2) % 40 == 20) and grid[g_coords[1]][g_coords[0] + 1]:
        food[g_coords[1]][g_coords[0]] = f
        pac[0] = pygame.image.load('pac_1_right.jpg')
        g_coords[0] += 1
        for i in range(8):
            drawPacMaze()
            wn.blit(ghost[0], (ghost1_x, ghost1_y))
            wn.blit(ghost[0], (ghost2_x, ghost2_y))
            wn.blit(ghost[1], (ghost3_x, ghost3_y))
            wn.blit(ghost[1], (ghost4_x, ghost4_y))
            animation()
            clock.tick(27)
            pac_x += vel
            if ghost1_x == 330 - 35/2:
                ghost1_vel *= -1
            if ghost1_x == 330 - 35/2 + 200:
                ghost1_vel *= -1
            ghost1_x += ghost1_vel
            if ghost2_x <= 330 - 35/2:
                ghost2_vel *= -1
            if ghost2_x >= 330 - 35/2 + 200:
                ghost2_vel *= -1
            ghost2_x += ghost2_vel
            if ghost3_x <= 330 - 35/2 - 80:
                ghost3_vel *= -1
            if ghost3_x >= 330 - 35/2 + 280:
                ghost3_vel *= -1
            ghost3_x += ghost3_vel
            if ghost4_x <= 330 - 35/2 - 80:
                ghost4_vel *= -1
            if ghost4_x >= 330 - 35/2 + 280:
                ghost4_vel *= -1
            ghost4_x += ghost4_vel

            if (ghost1_x == pac_x and ghost1_y == pac_y) or (ghost2_x == pac_x and ghost2_y == pac_y):
                restart()
    elif pac_down and ((pac_x + 35/2) % 40 == 10) and ((pac_y + 35/2) % 40 == 20) and grid[g_coords[1] + 1][g_coords[0]]:
        food[g_coords[1]][g_coords[0]] = f
        g_coords[1] += 1
        pac[0] = pygame.image.load('pac_1_down.jpg')
        for i in range(8):
            drawPacMaze()
            wn.blit(ghost[0], (ghost1_x, ghost1_y))
            wn.blit(ghost[0], (ghost2_x, ghost2_y))
            wn.blit(ghost[1], (ghost3_x, ghost3_y))
            wn.blit(ghost[1], (ghost4_x, ghost4_y))
            animation()
            clock.tick(27)
            pac_y += vel
            if ghost1_x == 330 - 35/2:
                ghost1_vel *= -1
            if ghost1_x == 330 - 35/2 + 200:
                ghost1_vel *= -1
            ghost1_x += ghost1_vel
            if ghost2_x <= 330 - 35/2:
                ghost2_vel *= -1
            if ghost2_x >= 330 - 35/2 + 200:
                ghost2_vel *= -1
            ghost2_x += ghost2_vel
            if ghost3_x <= 330 - 35/2 - 80:
                ghost3_vel *= -1
            if ghost3_x >= 330 - 35/2 + 280:
                ghost3_vel *= -1
            ghost3_x += ghost3_vel
            if ghost4_x <= 330 - 35/2 - 80:
                ghost4_vel *= -1
            if ghost4_x >= 330 - 35/2 + 280:
                ghost4_vel *= -1
            ghost4_x += ghost4_vel

            if (ghost1_x == pac_x and ghost1_y == pac_y) or (ghost2_x == pac_x and ghost2_y == pac_y):
                restart()
    elif pac_left and ((pac_x + 35/2) % 40 == 10) and ((pac_y + 35/2) % 40 == 20) and grid[g_coords[1]][g_coords[0] - 1]:
        food[g_coords[1]][g_coords[0]] = f
        g_coords[0] -= 1
        pac[0] = pygame.image.load('pac_1_left.jpg')
        for i in range(8):
            drawPacMaze()
            wn.blit(ghost[0], (ghost1_x, ghost1_y))
            wn.blit(ghost[0], (ghost2_x, ghost2_y))
            wn.blit(ghost[1], (ghost3_x, ghost3_y))
            wn.blit(ghost[1], (ghost4_x, ghost4_y))
            animation()
            clock.tick(27)
            pac_x -= vel
            if ghost1_x == 330 - 35/2:
                ghost1_vel *= -1
            if ghost1_x == 330 - 35/2 + 200:
                ghost1_vel *= -1
            ghost1_x += ghost1_vel
            if ghost2_x <= 330 - 35/2:
                ghost2_vel *= -1
            if ghost2_x >= 330 - 35/2 + 200:
                ghost2_vel *= -1
            ghost2_x += ghost2_vel
            if ghost3_x <= 330 - 35/2 - 80:
                ghost3_vel *= -1
            if ghost3_x >= 330 - 35/2 + 280:
                ghost3_vel *= -1
            ghost3_x += ghost3_vel
            if ghost4_x <= 330 - 35/2 - 80:
                ghost4_vel *= -1
            if ghost4_x >= 330 - 35/2 + 280:
                ghost4_vel *= -1
            ghost4_x += ghost4_vel

            if (ghost1_x == pac_x and ghost1_y == pac_y) or (ghost2_x == pac_x and ghost2_y == pac_y):
                restart()
    else:
        for i in range(8):
            drawPacMaze()
            wn.blit(ghost[0], (ghost1_x, ghost1_y))
            wn.blit(ghost[0], (ghost2_x, ghost2_y))
            wn.blit(ghost[1], (ghost3_x, ghost3_y))
            wn.blit(ghost[1], (ghost4_x, ghost4_y))
            animation()
            clock.tick(27)
            if ghost1_x <= 330 - 35/2:
                ghost1_vel *= -1
            if ghost1_x >= 330 - 35/2 + 200:
                ghost1_vel *= -1
            ghost1_x += ghost1_vel
            if ghost2_x <= 330 - 35/2:
                ghost2_vel *= -1
            if ghost2_x >= 330 - 35/2 + 200:
                ghost2_vel *= -1
            ghost2_x += ghost2_vel
            if ghost3_x <= 330 - 35/2 - 80:
                ghost3_vel *= -1
            if ghost3_x >= 330 - 35/2 + 280:
                ghost3_vel *= -1
            ghost3_x += ghost3_vel
            if ghost4_x <= 330 - 35/2 - 80:
                ghost4_vel *= -1
            if ghost4_x >= 330 - 35/2 + 280:
                ghost4_vel *= -1
            ghost4_x += ghost4_vel

            if (ghost1_x == pac_x and ghost1_y == pac_y) or (ghost2_x == pac_x and ghost2_y == pac_y):
                restart()
    
    if (ghost1_x == pac_x and ghost1_y == pac_y) or (ghost2_x == pac_x and ghost2_y == pac_y) or (ghost3_x == pac_x and ghost3_y == pac_y) or (ghost4_x == pac_x and ghost4_y == pac_y):
        restart()

    pygame.display.update()


# animation function
def animation():
    global animation_select
    if not pac_start:
        wn.blit(pac[1], (pac_x, pac_y))
    if pac_start:
        if animation_select <= 3:
            wn.blit(pac[0], (pac_x, pac_y))
            animation_select += 1
        elif animation_select < 6:
            wn.blit(pac[1], (pac_x, pac_y))
            animation_select += 1
        else:
            wn.blit(pac[1], (pac_x, pac_y))
            animation_select = 0
    pygame.display.update()

# win function
def win():
    global pac_man, game, text, game_font
    win_loop = True
    text = ''
    while win_loop:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pac_man = False
                win_loop = False
                game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            restart()
            win_loop = False
        wn.blit(win_screen, (0, 0))
        game_font.render_to(wn, (width/2 - 105, 380), str(round(total_time, 1)), (255, 255, 255))
        game_font.render_to(wn, (50, 380), text, (255, 255, 255))
        pygame.display.update()


# game loop
total_time = 0
all_time = 0
while game:
    while start:
        clock.tick(27)
        
        # exit window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pong = False
                breakout = False
                pac_man = False
                start = False

        for i in range(4):
            wn.blit(starting_animation[i], (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
        wn.blit(starting_animation[4], (0, 0))
        pygame.display.update()
        pygame.time.delay(700)
        select_screen = True
        start = False

    while select_screen:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pong = False
                breakout = False
                pac_man = False
                start = False
                select_screen = False
        
        # detect key press
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if move_ticker == 0:
                move_ticker = 10
                selector -= 1
                if selector == -1:
                    selector = 0
            
        if keys[pygame.K_DOWN]:
            if move_ticker == 0:
                move_ticker = 10
                selector += 1
                if selector == 3:
                    selector = 2
        
        if keys[pygame.K_SPACE]:
            if selector == 0:
                select_screen = False
                pong = True
                start_time = pygame.time.get_ticks()
            if selector == 1:
                control_screen = True
            if selector == 2:
                leaderboard_check = True
        
        if keys[pygame.K_r]:
            control_screen = False
            leaderboard_check = False

        if move_ticker > 0:
            move_ticker -= 1
        if not control_screen and not leaderboard_check:
            wn.blit(start_screen[selector], (0, 0))
        elif control_screen:
            wn.blit(controls, (0, 0))
        elif leaderboard_check:
            os.system(osCommandString)
            leaderboard_check = False

        pygame.display.update()


    while pong:
        clock.tick(27)
        
        if instructions_check:
            instructions_check = False
            wn.fill((0, 0, 0))
            drawMidLine()
            drawPongRect()
            pygame.draw.circle(wn, (255, 255, 255), (pong_circ_x, pong_circ_y), 10)
            drawPongEnemy()
            drawPongControls()
            pygame.time.delay(3500)
            wn.fill((0, 0, 0))
            drawMidLine()
            drawPongRect()
            pygame.draw.circle(wn, (255, 255, 255), (pong_circ_x, pong_circ_y), 10)
            drawPongEnemy()
            pygame.time.delay(2000)

        # exit window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pong = False
                breakout = False
                pac_man = False
        
        # detect key press
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if pong_rect_y >= 0:
                pong_rect_y -= 10
        
        if keys[pygame.K_DOWN]:
            if pong_rect_y <= height - 80:
                pong_rect_y += 10
        
        if keys[pygame.K_r]:
            restart()
        
        wn.fill((0, 0, 0))
        drawMidLine()
        drawPongRect()
        drawPongBall()
        drawPongEnemy()

    while breakout:
        clock.tick(27)
        
        # exit window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pong = False
                breakout = False
                pac_man = False
        
        # detect key press
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if breakout_rect_x >= 200 and breakout_start:
                breakout_rect_x -= 10
        
        if keys[pygame.K_RIGHT]:
            if breakout_rect_x <= 700 - 110 and breakout_start:
                breakout_rect_x += 10
        
        if keys[pygame.K_SPACE]:
            breakout_start = True
        
        if keys[pygame.K_r]:
            restart()

        wn.fill((0, 0, 0))
        wn.blit(breakout_controls, (-80, 0))
        drawBreakoutRect()
        drawBreakoutBall()
        drawBreakoutBorders()
        drawBreakoutBricks()

    while pac_man:
        clock.tick(27)

        # exit window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pong = False
                breakout = False
                pac_man = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                print(wn.get_at(pos)[:3])
        
        # detect key press
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pac_left = True
            pac_right = False
            pac_up=  False
            pac_down = False
            pac_start = True
        
        if keys[pygame.K_RIGHT]:
            pac_right = True
            pac_left = False
            pac_up=  False
            pac_down = False
            pac_start = True
        
        if keys[pygame.K_UP]:
            pac_up = True
            pac_down = False
            pac_left = False
            pac_right = False
            pac_start = True
        
        if keys[pygame.K_DOWN]:
            pac_down = True
            pac_up = False
            pac_left = False
            pac_right = False
            pac_start = True
        
        if keys[pygame.K_r]:
            restart()
        
        drawPacMaze()
        wn.blit(pac_controls, (-100, 0))
        #ghostMove()
        drawPac()
        win_check = 0
        for i in range(10):
            for n in range (12):
                if food[i][n] == f:
                    win_check += 1
        if win_check == 120:
            finish_time = pygame.time.get_ticks()
            total_time = (finish_time - start_time)/1000
            f = open("leaderboard.txt")
            with open("leaderboard.txt", mode='a') as f:
                f.write(str(round(total_time, 1)) + "\n")
            win()
            with open("leaderboard.txt", mode='a') as f:
                f.write(text + "\n")
            selector = 2
            final = open("final_leaderboard.txt","r+")
            final.truncate(0)
            list = []
            with open("leaderboard.txt", mode='r') as f:
                for line in f:
                    list.append(line.strip())
            i = 0
            names = []
            scores = []
            while i < len(list):
                if i % 2 == 0:
                    scores.append(float(list[i]))
                else:
                    names.append(list[i])
                i += 1

            if len(list) > 0:
                scores, names = zip(*sorted(zip(scores, names)))
            with open("final_leaderboard.txt", mode='a') as f:
                for i in range(len(scores)):
                    f.write(names[i] + ' - ' + str(scores[i]) + '\n')
pygame.quit()
