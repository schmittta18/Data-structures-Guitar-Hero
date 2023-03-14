#FIFO Queue
#
# CS3021 LL Project
#
# winter 2019
# last updated: 04 Jan 2019
#

import LinkedList

class FIFO(object):
    ''' Implement, you will need to call appropriate LinkedList functionality.
        FIFO has-a Linked List.
        Generate appropriate docstrings.
        Do not write code to duplicate any LL behaviors in this file
        Do not change LinkedList. ''' 

    def __init__(self):
        self.theQueue = LinkedList.LinkedList()
        

    def add(self, dataItem):
        '''Adds the dataItem to the next index in the FIFO queue'''
        self.theQueue.append(dataItem)
         

    def remove(self):
        '''Removes the first item from the queue if the list is not empty'''
        if self.empty():
            answer = None
        else:
            answer = self.theQueue.read(0)
            self.theQueue.deleteAtIndex(0)
        return answer

    def empty(self):
        '''Uses linkedList empty functionality to check whether or not
        the FIFO queue is empty'''
        return self.theQueue.empty()

    
    def __str__(self):
        '''Prints the items in the FIFO when called'''
        if self.empty():
            answer = ''
        else:
            answer = str(self.theQueue)
        return answer
    
         
