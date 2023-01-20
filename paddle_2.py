import pygame
import paddle
BLACK = (0, 0, 0)

class Paddle_2(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        
        #the paddles color width and height with a clear background
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        #draw paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()
        
    def moveA(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
          self.rect.x = 0
        
    def moveD(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 700:
          self.rect.x = 700
          
    def moveW(self, pixels):
        self.rect.y -= pixels
        if self.rect.y > 700:
            self.rect.y = 700
            
    def moveS(self, pixels):
        self.rect.y += pixels
        if self.rect.y < 0:
            self.rect.y = 0