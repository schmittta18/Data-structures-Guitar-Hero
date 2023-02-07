import pygame
import os

#Pygame initialization
canvas = pygame.display.set_mode((1380, 720))
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

#Sprite class for note at bottom of screen
class Notes(pygame.sprite.Sprite):
    def __init__(self, location, fillColor):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(pygame.color.Color(fillColor))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(location)

#Individual sprite creation     
note_spritegroup = pygame.sprite.Group()
colors = ['green', 'red', 'yellow', 'blue', 'orange']

for i in range(5):
    location = (600+85*i, 600)
    fillColor = colors[i]
    note_spritegroup.add( Notes( location, fillColor ) )
        
#Music track files
#s = "Guitar Hero III Tracks\Quickplay\Guns N' Roses - Welcome To The Jungle"
s = "Guitar Hero III Tracks\Quickplay\Weezer - My Name Is Jonas"
#s = "Guitar Hero III Tracks\Bonus\The Fall Of Troy - F.C.P.R.E.M.I.X"



guitar = pygame.mixer.Sound((os.path.join(s, 'guitar.ogg')))
rhythm = pygame.mixer.Sound((os.path.join(s, 'rhythm.ogg')))
song = pygame.mixer.Sound((os.path.join(s, 'song.ogg')))

album = pygame.image.load((os.path.join(s, 'album.png')))

chart = os.path.join(s, 'notes.chart')

#Chart read
chartList = []
chartFile = open(chart,"r")

for line in chartFile:
    line = line.strip('\t')
    line = line.strip('\n')
    chartList.append(line)
    
chartFile.close()

difficulty = ['[ExpertSingle]', '[HardSingle]', '[MediumSingle]', ['EasySingle'] ]
startIndex = chartList.index(difficulty[0])+2
chartList = chartList[startIndex:]

endIndex = chartList.index('}')
chartList = chartList[:endIndex]

#Play
guitar.play(1)
rhythm.play(1)
song.play(1)

time = 0
nextTick = 0 


done = False
while (not done):
    
    for event in pygame.event.get():
        if event.type != pygame.KEYDOWN:
            continue    
        elif event.key == pygame.K_q:
            done = True
            guitar.stop()
            rhythm.stop()
            song.stop()
        
    

    #display album cover
    canvas.blit(album, (0,0))
    pygame.display.flip()   
    
    
    #get note time
    
    '''chartList[0] = chartList[0].split()
    
    time = int(chartList[0][0])
    
    if len(chartList) > 1:
        timeEnd1 = chartList[1].index(" ")
        nextTick = int(chartList[1][:timeEnd1])   
    else:
        nextTick = 0
    
    note = colors[int(chartList[0][3])]'''
    
    #sprite = note_spritegroup.sprites()[0]
    #canvas.blit(sprite.image, sprite.rect)
    
    
    pygame.time.delay(time-nextTick)
    
    note_spritegroup.draw(canvas)
    
    pygame.display.flip()  
    #Move the spritegroup around
    
    
    #chartList.pop(0)