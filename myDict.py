#Dictionary
#

import LinkedList

####TUPLE ORDERING
KEY = 0
VALUE = 1

class myDictionary(object):
    
    
    def __init__(self):
        '''Constructor, creates a list of linked lists .
        Each bin will be assigned to a modulo of the hash function and the number of bins.'''
        self.numBins = 20
        i=0
        self.theDict =[]
        while i <self.numBins:
            self.theDict.append(LinkedList.LinkedList())
            i+=1
            
            

        
    
    def insert(self, key,value):
        #First, compute the hash value for the key
        hashValue = hash(key)%(self.numBins)
        location = self.theDict[hashValue].indexOfKey(key)
        
        #Before we add it, must make sure the key isn't already in the dictionary. If its not, add as a (K,V), tuple.
        #If it is, delete the old entry and replace it with the new one
        if location != None:
            self.theDict[hashValue].deleteAtIndex(location)
            
    
        self.theDict[hashValue].append((key,value))
            
    def items(self):
        '''Returns a python list of key value pairs, ie a list of tuples'''
        itemList=[]
        
        #For each bin in our list of linked lists
        for container in self.theDict:
            #If there is data in the bin
            if not container.empty():
                #Walk through the list and return the data
                i=0
                while container.read(i) != None:
                    data = container.read(i)
                    itemList.append(data)
                    i+=1    
                    
        return itemList
    def get(self,key):
        '''Returns value if key in dictionary, or None if not in dictionary'''
        hashValue = hash(key)%(self.numBins)
        location = self.theDict[hashValue].indexOfKey(key)
        if location != None:
            returnValue = self.theDict[hashValue].read(location)[VALUE]
            
        else:
            print("key not in dictionary")
            returnValue = None
            
        return returnValue
    
    
    def remove(self,key):
        hashValue = hash(key)%(self.numBins)
        location = self.theDict[hashValue].indexOfKey(key)
        if location != None:
            returnValue = self.theDict[hashValue].read(location)
            self.theDict[hashValue].deleteAtIndex(location)
            
        else:
            print("key not in dictionary")
            returnValue = None
            
        return returnValue        
        
        
        
        
    def __len__(self):
        '''Overrides the internal python length function and returns 
        the overall number of keyValue pairs'''
        length = 0 
        for container in self.theDict:
            #If there is data in the bin
            if not container.empty():
                #Walk through the list and add each pair
                i=0
                while container.read(i) != None:
                    length+=1
                    i+=1    
    
        return length    
    def keys(self):
        ''' Returns a list of the keys in the dictionary'''
        keyList=[]
    
        #For each bin in our list of linked lists
        for container in self.theDict:
            #If there is data in the bin
            if not container.empty():
                #Walk through the list and add the keys to our keyList
                i=0
                while container.read(i) != None:
                    data = container.read(i)
                    keyList.append(data[KEY])
                    i+=1    
    
        return keyList   
    
    def values(self):
        '''Returns a list of the values in the dictionary'''
        valueList=[]
    
        #For each bin in our list of linked lists
        for container in self.theDict:
            #If there is data in the bin
            if not container.empty():
                #Walk through the list and add the keys to our keyList
                i=0
                while container.read(i) != None:
                    data = container.read(i)
                    valueList.append(data[VALUE])
                    i+=1    
    
        return valueList  
    
    def update(self,aDict):
        dictItems = list(aDict.items())
        
        for pair in dictItems:
            self.insert(pair[KEY],pair[VALUE])
    def __hash__(self):
        #Prevent hashing of the dictionary
        return None
        
        
        


