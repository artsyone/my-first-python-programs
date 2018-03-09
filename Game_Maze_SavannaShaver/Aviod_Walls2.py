# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
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


# Make a player
player1 =  [200, 150, 25, 25]
vel1 = [0, 0]
player1_speed = 5

# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 450, 200, 25]
wall3 =  [100, 100, 25, 200]

walls = [wall1, wall2, wall3]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]


# stages
START = 0
PLAYING = 1
END = 2


def setup():
    global block_pos, block_vel, size, stage, time_remaining, ticks
    
    block_pos = [375, 275]
    block_vel = [0, 0]
    size = 50

    stage = START
    time_remaining = 10
    ticks = 0

# Game loop
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
                if event.key == pygame.K_LEFT:
                    block_vel[0] -= 2
                    vel1[0] = -player1_speed
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] += 2
                    vel1[0] = player1_speed
                elif event.key == pygame.K_UP:
                    block_vel[1] -= 2
                    vel1[1] = -player1_speed
                elif event.key == pygame.K_DOWN:
                    block_vel[1] += 2
                    vel1[1] = player1_speed
                    
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

    

 
    
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]


    if stage == PLAYING:
        ''' move block '''
        block_pos[0] += block_vel[0]
        block_pos[1] += block_vel[1]

        ''' end game on wall collision '''
        if block_pos[0] < 0 or block_pos[0] > 950 or \
           block_pos[1] < 0 or block_pos[1] > 650:
            stage = END
    

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


    ''' here is where you should resolve player collisions with screen edges '''




    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player1, c)]

    if len(coins) == 0:
        win = True

    ''' timer stuff '''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
            ''' and other stuff could happen here too '''

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])


    
    ''' timer text '''
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [50, 50])
    
    ''' begin/end game text '''
    if stage == START:
        text1 = MY_FONT.render("Block", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, WHITE)
        screen.blit(text1, [350, 150])
        screen.blit(text2, [225, 200])
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])


    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

