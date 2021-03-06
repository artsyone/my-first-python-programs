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
laugh3 = pygame.mixer.Sound("sounds/laugh3.ogg")
magic = pygame.mixer.Sound("sounds/laugh3.ogg")
hurt = pygame.mixer.Sound("sounds/posion.ogg")

#images
terror = pygame.image.load("images/terror.png")
pug1 = pygame.image.load("images/happy-pug.jpg")
person = pygame.image.load("images/scarycute.jpg")
pug2 = pygame.image.load("images/goodpug.jpg")
pug3 = pygame.image.load("images/pug3.jpg")
pug4 = pygame.image.load("images/pug4.jpg")
pug5 = pygame.image.load("images/pug5.jpg")
over = pygame.image.load("images/gameover.png")
uni = pygame.image.load("images/uni1.png")
posion = pygame.image.load("images/posion.png")



# Make a player
player1 = [200, 150, 25, 25]
vel1 = [0, 0]
player1_speed = 5
score1 = 0
#Font
MY_FONT = pygame.font.Font(None,30)
gameover = pygame.font.Font("fonts/game.ttf",60)

# make walls

w1 =  [300 , 275, 400, 25]
w2 =  [195, 200, 200, 25]
w3 =  [100, 100, 25, 200]
w4 =  [350, 100, 25, 200]
w5 =  [425, 100, 25, 200]
w6 =  [100, 550, 25, 50]
w7 =  [250, 500, 25, 150]
w8 =  [500, 300, 25, 250] 
w9 =  [350, 100, 25, 200] 
w10 =  [425, 200,400, 25]
w11 =  [50,445,375, 25]
w12 =  [-20,0,25, 800]
w13 =  [795,0,25, 800]
w14 =  [0,595,800, 25]
w15 =  [0,100,300, 25]
w16 =  [100,275,100, 25]
w17 =  [100,385,320, 25]
w18 =  [40,185,25, 375]
w19 =  [700,75,25, 125]
w20 =  [300,350,25, 50]
w21 =  [560,350,25, 150]
w22 =  [625,450,25, 150]




walls = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [380, 240, 25, 25]
coin3 = [150, 175, 25, 25]
coin4 = [475, 235, 25, 25]
coin5 = [10, 500, 25, 25]
coin6 = [200, 500, 25, 25]
coin7 = [100, 500, 25, 25]

u1 =[453,380,40,40]
u2 =[737,240,40,40]
u3 =[160,500,40,40]
u4 =[300,155,40,40]


p1 =[553,380,40,40]
p2 =[237,240,40,40]
p3 =[260,500,40,40]
p4 =[400,155,40,40]


# stages
START = 0
PLAYING = 1
END = 2



def setup():
    global player1_pos,player1_vel, size, stage,time_remaining,ticks,coins,sad,fun,unicorn,my_coins,jelly
    
    player1_pos = [375, 275]
    player1_vel = [0, 0]
    size = 50
    stage = START
    time_remaining = 60
    ticks = 0
    fun = (random.choice ([pug1,pug2,pug3,pug4,pug5]))
    sad = (random.choice([terror,person]))
    coins = [coin1]
    unicorn = []
    jelly = [p1,p2,p3,p4]
    
    


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
             pygame.mouse.get_pressed()
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    
            elif stage == PLAYING:
                   pass
               
                    
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()
                if event.key == pygame.K_l:
                    done = True


   
        
    # Game logic (Check for collisions, update points, etc.)

    mouse_pos = pygame.mouse.get_pos()
    
    ''' get block edges (makes collision resolution easier to read) '''
    left = player1[0]
    right = player1[0] + player1[2]
    top = player1[1]
    bottom = player1[1] + player1[3]

    if stage == PLAYING:

        
        
        sec = ticks//60
        if  sec <= 2:
                player1 = [100, 10, 25, 25]
                
                    
        else:
            if sec > 2 :
                player1 = [mouse_pos[0], mouse_pos[1], 25, 25]
        ticks += 1
        
        ''' move block '''        
        for c in coins:
            if intersects.rect_rect(player1, c):
                hit_list.append(c)
         
        hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
        
        for hit in hit_list:
            
            coins.remove(hit)
            
            score1 += 1
            laugh3.play()
            
            
            print("sound!")
            
        if len(coins) == 0:
            win = True
            stage = END




        ''' move block '''        
        
         
        stuff_list = [u for u in unicorn if intersects.rect_rect(player1, u)]
        
        for stuff in stuff_list:
            unicorn.remove(stuff)
            
            coins = [coin1,coin2,coin3,coin4,coin5]
            magic.play()
            
            
            print("sound!")



        
        things_list = [p for p in jelly if intersects.rect_rect(player1, p)]
        
        for things in things_list:
            jelly.remove(things)
            posion.play()
            
            
            
            print("sound!")
        
          
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

    
    for u in unicorn:
        
        screen.blit(uni, (u[0],u[1]))

    for p in jelly:
        screen.blit(posion, (p[0],p[1]))   
        
    if stage == START:
        
        
        
        pygame.draw.rect(screen, BLACK, [0,0,800,600])
        text3 = MY_FONT.render(" To win collect all the coins before the timer runs out", True, WHITE)
        text2 = MY_FONT.render(" AVOID THE WALLS OR YOU WILL LOSE", True, WHITE)
        text1 = MY_FONT.render(" Your MOUSE is your player, dont be fooled this game can be won ", True, WHITE)
        text4 = MY_FONT.render("(Press SPACE to play.)", True, WHITE)

        
        
        screen.blit(text1, [100, 150])
        screen.blit(text2, [100, 200])
        screen.blit(text3, [100, 250])
        screen.blit(text4, [100, 350])
        player1 = [mouse_pos[0], mouse_pos[1], 25, 25]
      
    elif stage == END:
        
        player1 = [mouse_pos[0], mouse_pos[1], 25, 25]
        pygame.mixer.music.pause()
        
        if win:
            
            screen.blit(fun ,(0,0))
            laugh.play()
            sec = ticks//60
            
            if  5 < sec <= 7:
                    g = gameover.render(" You Win ", True, BLACK)
                    screen.blit(g,(225,250))
    
            else:
                 if sec >= 7:
                    pygame.draw.rect(screen, BLACK, [0,0,800,600])
                    text2 = MY_FONT.render(" To quit the game, press L, for loser  ", True, WHITE)
                    text4 = MY_FONT.render(" To try again,(Press SPACE to play.)", True, WHITE) 
                      
                    screen.blit(text2, [125, 200])
                    screen.blit(text4, [125, 300])
                    
            font = pygame.font.Font(None, 48)
            text1 = font.render("Score:" + str(score1) , 1, BLACK)
            screen.blit(text1, [0, 0])
            aviod = 0
           
           
        else:
            
            screen.blit(sad,(0,0))
            
            yell.play()
            
            font = pygame.font.Font(None, 48)
            
            text1 = font.render("Score:" + str(score1), 1, BLACK)
            screen.blit(text1, [0, 0])
            sec = ticks//60
            if  5 < sec <= 7:
                    g = gameover.render(" GAME OVER ", True, WHITE)
                    screen.blit(g,(225,250))
                    
            else:
                 if sec >= 7:
                    pygame.draw.rect(screen, BLACK, [0,0,800,600])
                    text2 = MY_FONT.render(" To quit the game, press L, for loser  ", True, WHITE)
                    text4 = MY_FONT.render(" To try again,(Press SPACE to play.)", True, WHITE) 
                      
                    screen.blit(text2, [125, 200])
                    screen.blit(text4, [125, 300])
            
            player1 = [mouse_pos[0], mouse_pos[1], 25, 25]
         
        ticks += 1
                
    
            
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
