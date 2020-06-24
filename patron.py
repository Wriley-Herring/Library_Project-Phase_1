'''

@author: wrileyherring
'''

class Patron(object):
    '''
    Patron object
    '''

    #assign class variables for patron object
    def __init__(self, name):
       
        self.name = name
        self.checkedOutBooks = []
    
    #addBook method allows tracking of which books a patron has checked out
    def addBook(self,book):
        
        #check if the patron has check out more than three books
        if len(self.checkedOutBooks) < 3:
            self.checkedOutBooks.append(book.title)
        
        #print a statement if the owner has check out more than 3 books
        else:
            print("\nCan't borrow more books--MAX REACHED!")
    
    #print method to determine how many books the patron has checked out       
    def __str__(self):
        
        return "{} has {} books".format(self.name,len(self.checkedOutBooks))
