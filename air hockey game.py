#imports
import pygame
from brick import Brick
from brick_3 import Brick_3
from brick_4 import Brick_4
#imports paddle class
from paddle import Paddle
from ball import Ball
from paddle_2 import Paddle_2
pygame.init()
#set variables
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

score_2 = 0
score = 0
lives = 3

#open the new screen
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('breakout game')

#list that will contain all sprites
all_sprites_list = pygame.sprite.Group()

#create the paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

paddle_2 = Paddle_2(LIGHTBLUE, 100, 10)
paddle_2.rect.x = 350
paddle_2.rect.y = 75

ball = Ball(BLACK, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

    
#add paddle to list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
all_sprites_list.add(paddle_2)
#sets fps
clock = pygame.time.Clock()

#will run until exited
carryOn = True
#main loop
while carryOn:
    for event in pygame.event.get(): #user does something
        if event.type == pygame.QUIT: #if user clicks exit
            carryOn = False #exit

                
    keys = pygame.key.get_pressed()# move up and down also probably wasd ---------------------------------------
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
    if keys[pygame.K_UP]:
        paddle.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddle.moveDown(5)
        
    if keys[pygame.K_a]:
        paddle_2.moveA(5)
    if keys[pygame.K_d]:
        paddle_2.moveD(5)
    if keys[pygame.K_w]:
        paddle_2.moveW(5)
    if keys[pygame.K_s]:
        paddle_2.moveS(5)
        
    
        
    
    
    
    
            
    #---- game logic
    all_sprites_list.update()
    
    
    if ball.rect.x>= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        
        
        
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]
    
    
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
      
    if pygame.sprite.collide_mask(ball, paddle_2):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
      
    all_bricks_3 = pygame.sprite.Group()
    all_bricks_4 = pygame.sprite.Group()
    for i in range(1):
        brick_4 = Brick_4(RED,250,2)
        brick_4.rect.x = 270 + i* 100
        brick_4.rect.y = 38
        all_sprites_list.add(brick_4)
        all_bricks_4.add(brick_4)
    
    for i in range(1):
        brick_3 = Brick_3(RED, 250,2)
        brick_3.rect.x = 280 + i* 100
        brick_3.rect.y = 600
        all_sprites_list.add(brick_3)
        all_bricks_3.add(brick_3)
    
    
    brick_collision_list_3 = pygame.sprite.spritecollide(ball, all_bricks_3, False)
    for brick_3 in brick_collision_list_3:
        score_2 += 1
        if score_2 == 10:
            font = pygame.font.Font(None, 74)
            text = font.render("Player 2 wins", 1, BLACK)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            carryOn = False
            
            
    brick_collision_list_4 = pygame.sprite.spritecollide(ball, all_bricks_4, False)
    for brick_4 in brick_collision_list_4:
        score += 1
        if score == 10:
            font = pygame.font.Font(None, 74)
            text = font.render("Player 1 wins", 1, BLACK)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            carryOn = False
    
    
           
        
    
    #fill screen
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0, 38], [800, 38], 2)
    pygame.draw.line(screen, RED, [280, 597], [530, 597], 2)
    pygame.draw.line(screen, RED, [270, 38], [520, 38], 2)
    pygame.draw.line(screen, RED, [0, 317.5], [800, 317.5], 7)
    pygame.draw.line(screen, DARKBLUE, [0, 211.6], [800, 211.6], 7)
    pygame.draw.line(screen, DARKBLUE, [0, 423.4], [800, 423.4], 7)
    #displays scores
    font = pygame.font.Font(None, 34)
    text = font.render("Player_1 :" +str(score), 1, BLACK)
    screen.blit(text, (20,10))
    text = font.render("Player_2 :" +str(score_2), 1, BLACK)
    screen.blit(text, (560,10))
    
    #draw sprites
    all_sprites_list.draw(screen)
    
    #update the screen
    pygame.display.flip()
    
    #set fps
    clock.tick(60)
    
pygame.quit()




