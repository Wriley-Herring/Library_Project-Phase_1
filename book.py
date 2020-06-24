'''
Created on Jun 13, 2020

@author: wrileyherring
'''

class Book(object):
    '''
    Book Object
    '''
    
    #assign class vairiables
    def __init__(self, title,author):

        self.title = title
        self.author = author
        self.bookQueue = []
        self.owner = 'none'
    
    #borrow method allows books to be assigned to patrons
    def borrow(self,patron):
        
        #add patron to book queue
        self.bookQueue.append(patron)
        #assign current owner of book
        self.owner = self.bookQueue[0]
            
    #create print method to tell current status of book (Owner and Queue
    def __str__(self):
        
        return '{}, {} in care of: {}\n \nWaiting: \n1. {}\n2. {}'.format(self.title,self.author,str(self.owner),self.bookQueue[1],self.bookQueue[2])