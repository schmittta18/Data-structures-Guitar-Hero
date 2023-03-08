#Chart class
'''
Implements all functionality related to music files
Last updated: 1645 Feb 7 2023
'''

import os 
        
class Chart(object):
    
    def __init__(self, songChoice, difficultyChoice):
        '''
        I think we may be better off just storing the paths to the sound files in the 
        chart class and doing all the mixer initialization in main. I'll keep it as
        is for now for testing purposes. 
        '''
        
        
        #Song Folder
        self.songPath = self.__loadSong(songChoice)
        
        #Sound Files
        self.guitar = os.path.join(self.songPath, 'guitar.ogg')
        
        #Some songs don't have rhythm files...
        self.rhythm = os.path.join(self.songPath, 'rhythm.ogg')
        self.song = os.path.join(self.songPath, 'song.ogg')
        
        #Album Art
        self.album = os.path.join(self.songPath, 'album.png')
    
        #Note Chart
        self.difficulty = self.__loadDifficulty(difficultyChoice)
        self.chart = self.__loadChart(os.path.join(self.songPath, 'notes.chart'))
        
        #Chart Breakdown
        self.syncTrack = self.__getSync()
        self.syncTime = int(self.syncTrack[0][0])
        
        self.notes = self.__getNotes(self.difficulty)
        self.bpm = self.__getBPM()
        self.noteTime = int(self.notes[1][0]) - int(self.notes[0][0])
        
    
####################################################
# instance methods

    
    def pop(self):
        '''Return the next note of the song'''
        
        #will eventually need to implement held notes
        note = self.notes.pop(0)
        return int(note[3])
    
    def getMusic(self):
        return [self.guitar, self.rhythm, self.song]
    
    def getResolution(self):
        return self.resolution
    
    def getSyncTime(self):
        return self.syncTime
    
    def getBPM(self):
        return self.bpm
    
    def getFirstNote(self):
        return int(self.notes[0][0])

    def getTime(self):
        '''Return time next note occurs, also unncessary if stored in the class'''
        self.noteTime = int(self.notes[1][0]) - int(self.notes[0][0])
        return self.noteTime
    
    def chord(self):
        '''Return whether or not two notes are part of a chord'''
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
        
        songList = ["Guns N' Roses - Welcome To The Jungle", 
                    "Weezer - My Name Is Jonas", 
                    "Pearl Jam - Even Flow",
                    "Heart - Barracuda",
                    "Metallica - One"]
       
        return "Guitar Hero III Tracks New\Quickplay\\" + songList[songNumber]
    
    
    def __loadDifficulty(self, level):
        
        options = ['[ExpertSingle]', '[HardSingle]', '[MediumSingle]', '[EasySingle]' ]
        return options[level]    
    
    
    def __loadChart(self, chart):

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
        '''Return list form of notes portion of chart'''
        
        startIndex = self.chart.index([difficulty])+2
        notes = self.chart[startIndex:]

        endIndex = notes.index(['}'])
        return notes[:endIndex]

    

####################################################
# test