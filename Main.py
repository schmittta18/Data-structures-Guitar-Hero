"""
Guitar Hero Main Prototype
"""
import pygame
import pygame_menu
import Chart
import sys
import pygame.freetype
import os
import Scoresheet

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
        #self.birth = pygame.time.get_ticks()
        print(" a fret is born")
        
    

        # A sprite must have a .rect
        # This is where the .image gets drawn
        self.rect = self.image.get_rect()

        # Move the .rect to the specified location
        self.rect = self.rect.move(location)
        
                                
        
        #Store the keyConstant
        self.keyConstant = keyConstant
        
        
    def update(self):
        #If key not held down
        if not pygame.key.get_pressed()[self.keyConstant]:
            self.kill()
        #if (pygame.time.get_ticks() - self.birth) > 5000:
            #print(pygame.time.get_ticks()-self.birth)
            #self.kill()
            
                  
        

class Note(pygame.sprite.Sprite):
    """
    A note will be a blue circle, with a radius of 15
    The background has an alpha layer, so anything behind
    the area outside of the circle but within the 30 x 30 square
    can be seen 'through' the sprite's Surface
    """

    def __init__(self, location, color,fretGroup):
        super().__init__()
        
        colors = ['green', 'red', 'yellow', 'blue', 'orange']
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.color.Color(colors[color]), (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(location)
        self.move_y = 10
        self.fretGroup = fretGroup
        

    # The .update method gets called when calling the sprite group's
    # .update method
    def update(self):
        # If this note collides with any fret
        if pygame.sprite.spritecollide(self, self.fretGroup, False):
            
            #Kill the sprite
            self.kill()

        # Move the note by the current direction and distance (10 up or down)
        self.rect.move_ip((0, self.move_y))
### Scoreboard Function###########################################
def Scoreboard(score,location,name,scoreList):
    myfont.render_to(canvas, location, "Score:"+str(score), WHITE, None, size=64)
    xLocation = location[0]
    yLocation = location[1]
    leaderBoardLocation = (xLocation,yLocation+200)
    
    myfont.render_to(canvas,leaderBoardLocation, "High Scores:",WHITE, None, size = 64)
    firstScoreX = xLocation
    firstScoreY = yLocation+300
    for k in range(0,len(scoreList)):
        myfont.render_to(canvas,(firstScoreX,firstScoreY+100*k),scoreList[k],WHITE,size = 48)
        
        
    
    
    
    
    
class Launcher:
    def __init__(self,songTuple,difficultyTuple,userName):
        self.songNumber = songTuple[1]
        self.difficultyNumber = difficultyTuple[1]
        self.userName = userName
        self.scoreSheet = Scoresheet.LeaderBoard()
       
        self.scoreList = self.scoreSheet.readLeaderBoard((songTuple[0][0],difficultyTuple[0][0]))
        
        
        # These will group our frets and notes, so we can
        # place and update them with a single command
        note_spritegroup = pygame.sprite.LayeredUpdates()
        fret_spritegroup = pygame.sprite.LayeredUpdates()
        song = Chart.Chart(self.songNumber, self.difficultyNumber)
        
        self.rightNotes = 0


        resolution = song.getResolution()
        bpm = song.getBPM()*1.04
            
        
        # Use a pygame .Clock to slow this down
        clock = pygame.time.Clock()
        
        first = True
        done = False



        song.getMusic()[0].play(1)
        song.getMusic()[1].play(1)
        song.getMusic()[2].play(1)
        ###Event Loop
        
        
        while not done:
            
            
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    song.getMusic()[0].stop()
                    song.getMusic()[1].stop()
                    song.getMusic()[2].stop()  
                    self.scoreSheet.writeLeaderBoard((songTuple[0][0],difficultyTuple[0][0]),self.userName,self.rightNotes)
                    
                    done = True
                    
                pressed_keys = pygame.key.get_pressed()
                
                
                
                if pressed_keys[K_a]:
                    existingA = fret_spritegroup.get_sprites_at((60,650))
                    if not existingA:
                        fret_spritegroup.add(Fret((60,650),pygame.K_a))
                if pressed_keys[K_s]:
                    existingS = fret_spritegroup.get_sprites_at((160,650))
                    if not existingS:
                        fret_spritegroup.add(Fret((60+100,650),pygame.K_s))
                if pressed_keys[K_d]:
                    existingD = fret_spritegroup.get_sprites_at((260,650))
                    if not existingD:
                        fret_spritegroup.add(Fret((60+200,650),pygame.K_d))                    
                    
                if pressed_keys[K_f]:
                    existingF = fret_spritegroup.get_sprites_at((360,650))
                    if not existingF:
                        fret_spritegroup.add(Fret((60+300,650),pygame.K_f))                    
                   
                if pressed_keys[K_g]:
                    existingG = fret_spritegroup.get_sprites_at((460,650))
                    if not existingG:
                        fret_spritegroup.add(Fret((60+400,650),pygame.K_g))                    
                    
                
                collisions = pygame.sprite.groupcollide(note_spritegroup,fret_spritegroup,True,False,None)
                self.rightNotes+= len(collisions)
                
                print(fret_spritegroup.sprites()) 
    
    
            

            canvas.fill(BLACK)
            
            #generate new group of notes
            #we need to make sure we're separating adequately
            
            
            if first:
                nextNote = pygame.time.get_ticks() + int(((song.getFirstNote() * 60) / (bpm * resolution)))*1000
            
            if nextNote <= pygame.time.get_ticks():
                
                try:
                    noteTime = ((int(song.getTime()) * 60) / (bpm * resolution))
                except:
                    done = True
                    #print("End of the line")
                
                try :
                    note = song.pop()
                    note_spritegroup.add(Note((60 + 100 * note, 0), note,fret_spritegroup)) 
                except:
                    done = True
                    #print('END OF THE LINE')
                
                
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
            Scoreboard(self.rightNotes,(900,4),self.userName,self.scoreList)
            
            
            
    

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
        ####Here, we write the score to our leaderboard
        
        