####ScoreSheet
##This uses our dictionary class to store the high scores for each song
import myDict



songList = ["Guns N_ Roses - Welcome To The Jungle", 
            "Weezer - My Name Is Jonas", 
            "Pearl Jam - Even Flow",
            "Heart - Barracuda",
            "Metallica - One"]
difficultyList = ["Easy","Medium", "Hard", "Expert"]


class LeaderBoard:
    def __init__(self):
        ##Make a dictionary with song/difficulty keys and score file values
        self.scoreDict = myDict.myDictionary()
        self.songList = ["Guns N_ Roses - Welcome To The Jungle", 
                    "Weezer - My Name Is Jonas", 
                    "Pearl Jam - Even Flow",
                    "Heart - Barracuda",
                    "Metallica - One"]
        self.difficultyList = ["Easy","Medium", "Hard", "Expert"]     
        
        for song in self.songList:
            for difficulty in self.difficultyList:
                self.scoreDict.insert((song,difficulty),song+'_'+difficulty+'.txt')
                path = song + '_'+difficulty+'.txt'
                createFile = open(path,'a')
                createFile.close()
        self.pairs = self.scoreDict.items()
        print(self.pairs)
                
                
    def readLeaderBoard(self,resultTuple):
        
        ##returns a list of  "username      score" strings
        
        ### example path would be WelcometoTheJungle_Easy.txt
        scorePath = self.scoreDict.get(resultTuple)
        scoreFile = open(scorePath,'r')
        scoreList = scoreFile.read().splitlines()
        scoreFile.close()
        
        ### once we have the list, we need to parse out the top 5 scores for display purposes
        #highScores = myDict.myDictionary()
        #for item in scoreList:
            #tokens = item.split()
            ##put all of our players personal bests in to the dictionary
            #highScores.insert(tokens[0],tokens[1])
        #numberList = highScores.items()
        #numberList.sort(reverse = True)
        
            
            
        
        
        
        return scoreList
        
    def writeLeaderBoard(self,resultTuple,userName,score):
        scorePath = self.scoreDict.get(resultTuple)
        scoreFile = open(scorePath,'a')
        scoreFile.write(userName + '     '+ str(score))
        scoreFile.write('\n')
        scoreFile.close()
        
    
        
    
        
        
        
        
#####test code#######
#myBoard = LeaderBoard()
#myBoard.writeLeaderBoard(("Guns N_ Roses - Welcome To The Jungle",'Easy'),'Loren',650)
#myBoard.readLeaderBoard(("Guns N_ Roses - Welcome To The Jungle",'Easy'))
#myBoard.writeLeaderBoard(("Guns N_ Roses - Welcome To The Jungle",'Easy'),'Tom',600)
#myBoard.readLeaderBoard(("Guns N_ Roses - Welcome To The Jungle",'Easy'))






