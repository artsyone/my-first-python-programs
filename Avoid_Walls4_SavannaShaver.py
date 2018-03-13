import pygame
import intersects
import random


# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Aviod Wall Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
# Sound effect
theme = pygame.mixer.music.load("sounds/theme.ogg")
laugh = pygame.mixer.Sound("sounds/laugh.ogg")
yell = pygame.mixer.Sound("sounds/yell.ogg")

#images
terror = pygame.image.load("images/terror.png")
pug1 = pygame.image.load("images/happy-pug.jpg")
person = pygame.image.load("images/scarycute.jpg")
pug2 = pygame.image.load("images/goodpug.jpg")
pug3 = pygame.image.load("images/pug3.jpg")
pug4 = pygame.image.load("images/pug4.jpg")
pug5 = pygame.image.load("images/pug5.jpg")
over = pygame.image.load("images/gameover.png")


# Make a player
player1 = [200, 150, 25, 25]
vel1 = [0, 0]
player1_speed = 5
score1 = 0
#Font
MY_FONT = pygame.font.Font(None,30)

# make walls

wall1 =  [300, 275, 400, 25]
wall2 =  [195, 200, 200, 25]
wall3 =  [100, 100, 25, 200]
wall4 =  [350, 100, 25, 200]
wall5 =  [425, 100, 25, 200]
wall6 =  [100, 500, 25, 200]
wall7 =  [250, 500, 25, 200]
wall8 =  [500, 300, 25, 250] 
wall9 =  [350, 100, 25, 200] 
wall10 =  [425, 200,400, 25]
wall11 =  [0,445,400, 25]
wall12 =  [-20,0,25, 800]
wall13 =  [795,0,25, 800]
wall14 =  [0,595,800, 25]

walls = [wall1, wall2, wall3, wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [380, 240, 25, 25]
coin3 = [150, 175, 25, 25]
coin4 = [475, 235, 25, 25]
coin5 = [0, 500, 25, 25]


case = 1

# stages
START = 0
PLAYING = 1
END = 2



def setup():
    global player1_pos,player1_vel, size, stage,time_remaining,ticks,coins,sad,fun
    
    player1_pos = [375, 275]
    player1_vel = [0, 0]
    size = 50
    stage = START
    time_remaining = 60
    ticks = 0
    fun = (random.choice ([pug1,pug2,pug3,pug4,pug5]))
    sad = (random.choice([terror,person]))
    coins = [coin1,coin2,coin3,coin4,coin5]


# Game loop
setup()
pygame.mixer.music.play(-1)
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    
            elif stage == PLAYING:
                   pass
               
                    
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()


   
        
    # Game logic (Check for collisions, update points, etc.)

    mouse_pos = pygame.mouse.get_pos()
    
    player1 = [mouse_pos[0], mouse_pos[1], 25, 25]
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]


    ''' get block edges (makes collision resolution easier to read) '''
    left = player1[0]
    right = player1[0] + player1[2]
    top = player1[1]
    bottom = player1[1] + player1[3]

    if stage == PLAYING:
        ''' move block '''        
        for c in coins:
            if intersects.rect_rect(player1, c):
                hit_list.append(c)
         
        hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
        
        for hit in hit_list:
            coins.remove(hit)
            score1 += 1
            print("sound!")
            
        if len(coins) == 0:
            win = True
            stage = END

      
          
        ''' end game on wall collision '''
    avoid = []
    for w in walls:
            if intersects.rect_rect(player1, w):
                avoid.append(w)
                stage = END
    avoid = [w for w in walls if intersects.rect_rect(player1, w)]
    
    ''' timer stuff '''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
            ''' and other stuff could happen here too '''

        
    ''' if the block is moved out of the window, nudge it back on. '''
    if left < 0:
            player1[0] = 0
    elif right > WIDTH:
            player1[0] = WIDTH - player1[2]

    if top < 0:
            player1[1] = 0
    elif bottom > HEIGHT:
            player1[1] = HEIGHT - player1[3]
   
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    ''' timer text '''
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [50, 50])

    pygame.draw.rect(screen, WHITE, player1)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    if case == 1:
        color = RED
        pygame.draw.rect(screen, color, [wall1[0], wall1[1],wall1[2],wall1[3]])
        pygame.draw.rect(screen, color, [wall2[0], wall2[1],wall2[2],wall2[3]])
        pygame.draw.rect(screen, color, [wall3[0], wall3[1],wall3[2],wall3[3]])
        pygame.draw.rect(screen, color, [wall4[0], wall4[1],wall4[2],wall4[3]])
        pygame.draw.rect(screen, color, [wall5[0], wall5[1],wall5[2],wall5[3]])
        pygame.draw.rect(screen, color, [wall6[0], wall6[1],wall6[2],wall6[3]])
        pygame.draw.rect(screen, color, [wall7[0], wall7[1],wall7[2],wall7[3]])
        pygame.draw.rect(screen, color, [wall8[0], wall8[1],wall8[2],wall8[3]])
        pygame.draw.rect(screen, color, [wall9[0], wall9[1],wall9[2],wall9[3]])
        pygame.draw.rect(screen, color, [wall10[0], wall10[1],wall10[2],wall10[3]])
        pygame.draw.rect(screen, color, [wall11[0], wall11[1],wall11[2],wall11[3]])
        pygame.draw.rect(screen, color, [wall12[0], wall12[1],wall12[2],wall12[3]])
        pygame.draw.rect(screen, color, [wall13[0], wall13[1],wall13[2],wall13[3]])
        pygame.draw.rect(screen, color, [wall14[0], wall14[1],wall14[2],wall14[3]])
        pygame.draw.rect(screen, WHITE, [player1[0], player1[1], player1[2], player1[3]])

   

    if stage == START:
        
        pygame.draw.rect(screen, BLACK, [0,0,800,600])
        text = MY_FONT.render("Block", True, WHITE)
        text3 = MY_FONT.render(" To win collect all the coins before the timer runs out", True, WHITE)
        text2 = MY_FONT.render(" AVOID THE WALLS OR YOU WILL LOSE", True, WHITE)
        text1 = MY_FONT.render(" Your MOUSE is your player, dont be fooled this game can be won ", True, WHITE)
        text4 = MY_FONT.render("(Press SPACE to play.)", True, WHITE) 
        screen.blit(text1, [125, 150])
        screen.blit(text2, [125, 200])
        screen.blit(text3, [125, 250])
        screen.blit(text4, [125, 300])
      
    elif stage == END:
        pygame.mixer.music.pause()

        if win:
            
            screen.blit(fun ,(0,0))
            laugh.play()
            font = pygame.font.Font(None, 48)
            text = font.render("You Win!", 1, BLACK)
            screen.blit(text, [400, 200])
            text1 = font.render("Score:" + str(score1) , 1, BLACK)
            screen.blit(text1, [0, 0])
            aviod = 0
            
        else:
            
            screen.blit(sad,(0,0))
            
            yell.play()
            
            font = pygame.font.Font(None, 48)
            screen.blit(over,(225,100))
            text1 = font.render("Score:" + str(score1), 1, BLACK)
            screen.blit(text1, [0, 0])
            
            
#cant get the setup too work
#need to make it so u lose if u exit the screen u lose
#Make sure to fix the image random list
       

   
        
    
        
       
        
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    pygame.draw.rect(screen, WHITE, player1)
    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
