"""
Using sprites in pygame
Bouncing balls
"""


import pygame
from pygame.locals import *


BLACK = (0, 0, 0)

keyConstants = [pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g,pygame.K_h]





pygame.init()

canvas = pygame.display.set_mode((1380,720))




class Brick(pygame.sprite.Sprite):
    """
    Create a 'Brick' class, as a subclass of .Sprite
    """
    def __init__(self, location,keyConstant):
        # initialise the super (.Sprite) class
        super().__init__()

        # Create a 50 x 30 brown Surface
        # A sprite must have a .image attribute
        # The .image gets drawn when drawing the sprite
        self.image = pygame.Surface((50, 30))
        self.image.fill(pygame.color.Color('brown'))
    

        # A sprite must have a .rect
        # This is where the .image gets drawn
        self.rect = self.image.get_rect()

        # Move the .rect to the specified location
        self.rect = self.rect.move(location)
        
                                
        
        #Store the keyConstant
        self.keyConstant = keyConstant
        
        
    def update(self):
        #If key not held down
        if not pressed_keys[self.keyConstant]:
            self.kill()
            
                  
        
    
        
        
        
            
    
        
        
        
        
        



class Ball(pygame.sprite.Sprite):
    """
    A ball will be a blue circle, with a radius of 15
    The background has an alpha layer, so anything behind
    the area outside of the circle but within the 30 x 30 square
    can be seen 'through' the sprite's Surface
    """

    def __init__(self, location):
        super().__init__()

        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.color.Color('blue'), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(location)
        self.move_y = 10

    # The .update method gets called when calling the sprite group's
    # .update method
    def update(self):
        # If this ball collides with any brick
        if pygame.sprite.spritecollide(self, fret_spritegroup, False):
            #Kill the sprite
            self.kill()

        # Move the ball by the current direction and distance (10 up or down)
        self.rect.move_ip((0, self.move_y))


# These will group our bricks and balls, so we can
# place and update them with a single command
brick_spritegroup = pygame.sprite.Group()
ball_spritegroup = pygame.sprite.Group()
fret_spritegroup = pygame.sprite.Group()



    

# Use a pygame .Clock to slow this down
clock = pygame.time.Clock()
timeMeasure=0
done = False
while not done:

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        pressed_keys = pygame.key.get_pressed()
        
        
        if pressed_keys[K_a]:
            fret_spritegroup.add(Brick((15,500),pygame.K_a))
            
        if pressed_keys[K_s]:
            fret_spritegroup.add(Brick((15+60,500),pygame.K_s))
        if pressed_keys[K_d]:
            fret_spritegroup.add(Brick((15+120,500),pygame.K_d))
        if pressed_keys[K_f]:
            fret_spritegroup.add(Brick((15+180,500),pygame.K_f))
        if pressed_keys[K_g]:
            fret_spritegroup.add(Brick((15+240,500),pygame.K_g))
                  
    
    
            

    canvas.fill(BLACK)
    
    #generate new group of balls
    #we need to make sure we're separating adequately
    if timeMeasure %10 == 0:
        
        for i in range(6):
            ball_spritegroup.add(
            Ball((25 + 60 * i, 0))
            )           

    # Draw bricks and balls
    fret_spritegroup.draw(canvas)
    ball_spritegroup.draw(canvas)

    # Show the new canvas
    pygame.display.flip()

    # Call the .update method of each ball
    # This will move them up and/or down
    ball_spritegroup.update()
    fret_spritegroup.update()

    # Wait a little bit if necessary
    # so this will 30 times per second
    # i.e. 30 frames per second (fps)
    timeMeasure+=1
    clock.tick(30)


        
        



