#Chart class
'''
Implements all functionality related to music files
Last updated: 1645 Feb 7 2023
'''

import os 
import FIFO
        
class Chart(object):
    
    def __init__(self, songChoice, difficultyChoice):
        '''
        Chart class stores all necessary information from each song as attributes,
        and stores individual notes and note times in two FIFO lists. 
        '''
        
        
        #Song Folder
        self.songPath = self.__loadSong(songChoice)
        
        #Sound Files
        self.guitar = os.path.join(self.songPath, 'guitar.ogg')
        self.rhythm = os.path.join(self.songPath, 'rhythm.ogg')
        self.song = os.path.join(self.songPath, 'song.ogg')
        
        #Album Art
        self.album = os.path.join(self.songPath, 'album.png')
    
        #Note Chart
        self.difficulty = self.__loadDifficulty(difficultyChoice)
        self.chart = self.__loadChart(os.path.join(self.songPath, 'notes.chart'))
        
        #Sync Track for timing
        self.syncTrack = self.__getSync()
        self.syncTime = int(self.syncTrack[0][0])
        self.bpm = self.__getBPM()
        
        #FIFO Linked Lists for notes and note time
        self.firstNote = None
        self.note = None
        self.noteTime = None
        self.__getNotes(self.difficulty)
        
    
####################################################
# FIFO methods

    
    def pop(self):
        '''Return the next note of the song'''
        return self.notes.remove()
    
    def getTime(self):
        '''Return time next note occurs, also unncessary if stored in the class'''
        return self.noteTime.remove()

#####################################################
# Instance Methods
    def getMusic(self):
        '''Return list of track paths for sound mixer in Main'''
        return [self.guitar, self.rhythm, self.song]
    
    def getResolution(self):
        '''Return "resolution", an arbitary number the chart uses to keep 
        track of time signature'''
        return self.resolution
    
    def getSyncTime(self):
        '''Sync time, calculated with resolution and BPM, gives the number of 
        milliseconds between notes'''
        return self.syncTime
    
    def getBPM(self):
        '''Returns BPM, changes throughout most songs'''
        return self.bpm
    
    def getFirstNote(self):
        '''Returns the first note of a song, important for the loop in Main'''
        return self.firstNote
    
    def chord(self):
        '''Return whether or not two notes are part of a chord'''
        
        #####   NOT IMPLEMENTED YET #######
        
        if self.notes[1][0] == self.notes[0][0]:
            return True
        else:
            return False
    
    def bpmChange(self):
        '''Change BPM of song'''
        self.syncTrack.pop(0)
        self.bpm = self.__getBPM()
        self.syncTime = int(self.syncTrack[0][0])
        return self.bpm
            


####################################################
# private methods
    def __loadSong(self, songNumber):
        '''Creates path to song selected in menu'''
        
        songList = ["Guns N' Roses - Welcome To The Jungle", 
                    "Weezer - My Name Is Jonas", 
                    "Pearl Jam - Even Flow",
                    "Heart - Barracuda",
                    "Metallica - One"]
       
        return "Guitar Hero III Tracks New\Quickplay\\" + songList[songNumber]
    
    
    def __loadDifficulty(self, level):
        '''Returns the difficulty selected by the use in the menu'''
        
        options = ['[ExpertSingle]', '[HardSingle]', '[MediumSingle]', '[EasySingle]' ]
        return options[level]    
    
    
    def __loadChart(self, chart):
        '''Reads chart for the song selected in the Menu, returns as list'''

        chartList = []
        chartFile = open(chart,"r")
        
        for line in chartFile:
            line = self.__parseLine(line)
            chartList.append(line)
            
            if 'Resolution' in line:
                self.resolution = int(line[2])
            
        chartFile.close()
        
        return chartList
    
    
    def __parseLine(self, line):
        '''Parse line to remove superfluous characters and aid indexing'''
        
        line = line.strip('\t')
        line = line.strip('\n')
        line = line.split()
    
        return line
    
    
    def __getBPM(self):
        '''Returns the BPM currently at the top of the stack'''
        return int(self.syncTrack[0][3])/1000
    
    
    def __getSync(self):
        '''Return list form of sync track portion of chart'''
        
        identifier = '[SyncTrack]'
        startIndex = self.chart.index([identifier])+4
        sync = self.chart[startIndex:]

        endIndex = sync.index(['}'])
        return sync[:endIndex] 
        
    
    def __getNotes(self, difficulty):
        '''Creates two FIFO linked lists, one with each individual note, and one with the 
        amount of time each note lasts. Popping from these two lists is the '''
        
        noteFIFO = FIFO.FIFO()
        timeFIFO = FIFO.FIFO()
        
        startIndex = self.chart.index([difficulty])+2
        notes = self.chart[startIndex:]

        endIndex = notes.index(['}'])
        notes = notes[:endIndex]
        self.firstNote = int(notes[0][0])
        
        
        for note in notes:
            noteFIFO.add(note[3])
            
        for i in range(len(notes)-1):
            time = int(notes[i+1][0]) - int(notes[i][0])
            timeFIFO.add(time)        
        
        self.notes = noteFIFO
        self.noteTime = timeFIFO