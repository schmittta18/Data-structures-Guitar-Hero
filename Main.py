"""
Guitar Hero Main Prototype
"""
import pygame
import Chart
import sys
import pygame.freetype
import os

from pygame.locals import *

#Initialize
pygame.init()
canvas = pygame.display.set_mode((1380,720))
pygame.mixer.pre_init(44100, -16, 2, 2048)
keyConstants = [pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g,pygame.K_h]
BLACK = (0, 0, 0)
WHITE = (255,255,255)

#Set up the font for the scoreboard
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Fonts","GFSTheokritos.otf")
font_size = 20
pygame.freetype.init()
myfont = pygame.freetype.Font(font_path, font_size)


class Fret(pygame.sprite.Sprite):
    """
    Create a 'Fret' class, as a subclass of .Sprite
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
            
                  
        

class Note(pygame.sprite.Sprite):
    """
    A note will be a blue circle, with a radius of 15
    The background has an alpha layer, so anything behind
    the area outside of the circle but within the 30 x 30 square
    can be seen 'through' the sprite's Surface
    """

    def __init__(self, location, color):
        super().__init__()
        
        colors = ['green', 'red', 'yellow', 'blue', 'orange']
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.color.Color(colors[color]), (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(location)
        self.move_y = 10
        

    # The .update method gets called when calling the sprite group's
    # .update method
    def update(self):
        # If this note collides with any fret
        if pygame.sprite.spritecollide(self, fret_spritegroup, False):
            
            #Kill the sprite
            self.kill()

        # Move the note by the current direction and distance (10 up or down)
        self.rect.move_ip((0, self.move_y))
### Scoreboard Function###########################################
def Scoreboard(score,location):
    myfont.render_to(canvas, location, "Score:"+str(score), WHITE, None, size=64)
    
        
        


# These will group our frets and notes, so we can
# place and update them with a single command
note_spritegroup = pygame.sprite.Group()
fret_spritegroup = pygame.sprite.Group()
song = Chart.Chart(int(input('Enter Song Number: ')), int(input('Enter difficulty: ')))

rightNotes = 0

'''
Resolution is 192 for the majority of songs but may need to change
based on future song decisions, BPM will need to vary as well
'''
resolution = song.getResolution()
bpm = song.getBPM()*1.04
    

# Use a pygame .Clock to slow this down
clock = pygame.time.Clock()

first = True
done = False



song.getMusic()[0].play(1)
song.getMusic()[1].play(1)
song.getMusic()[2].play(1)

while not done:
    
    

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        pressed_keys = pygame.key.get_pressed()
        
        
        
        if pressed_keys[K_a]:
            fret_spritegroup.add(Fret((60,650),pygame.K_a))
        if pressed_keys[K_s]:
            fret_spritegroup.add(Fret((60+100,650),pygame.K_s))
        if pressed_keys[K_d]:
            fret_spritegroup.add(Fret((60+200,650),pygame.K_d))
        if pressed_keys[K_f]:
            fret_spritegroup.add(Fret((60+300,650),pygame.K_f))
        if pressed_keys[K_g]:
            fret_spritegroup.add(Fret((60+400,650),pygame.K_g))
        
        collisions = pygame.sprite.groupcollide(note_spritegroup,fret_spritegroup,True,False,None)
        rightNotes+= len(collisions)
        
                  
    
    
            

    canvas.fill(BLACK)
    
    #generate new group of notes
    #we need to make sure we're separating adequately
    
    
    if first:
        nextNote = pygame.time.get_ticks() + int(((song.getFirstNote() * 60) / (bpm * resolution)))*1000
    
    if nextNote <= pygame.time.get_ticks():
        
        noteTime = ((int(song.getTime()) * 60) / (bpm * resolution))
        
        note = song.pop()
        note_spritegroup.add(Note((60 + 100 * note, 0), note))  
        
        
        nextNote = pygame.time.get_ticks() + noteTime * 1000
    
    if first:
        syncTime = pygame.time.get_ticks() + int(((song.getSyncTime() * 60) / (bpm * resolution)))*1000
        print(song.getSyncTime())
        first = False
    
    if syncTime <= pygame.time.get_ticks():
        bpm = song.bpmChange() * 1.04
        syncTime = pygame.time.get_ticks() + int(((song.getSyncTime() * 60) / (bpm * resolution)))*1000
        print(bpm)
        
        
        
    # Draw frets and notes
    fret_spritegroup.draw(canvas)
    note_spritegroup.draw(canvas)
    Scoreboard(rightNotes,(900,4))
    
    

    # Show the new canvas
    pygame.display.flip()

    # Call the .update method of each ball
    # This will move them up and/or down
    note_spritegroup.update()
    fret_spritegroup.update() 
    
    
    
    # Wait a little bit if necessary
    # so this will 30 times per second
    # i.e. 30 frames per second (fps)
        
    
    clock.tick(75)