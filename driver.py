'''
Created on Jun 13, 2020

@author: wrileyherring
'''
#import packages
from book import Book
from patron import Patron

def main():
    
    #assign books and patrons
    book1 = Book("Of Mice and Men", "Steinbeck")
    book2 = Book("The Great Gatsby", "Fitzgerald")
    book3 = Book("1984","Orwell")
    book4 = Book("One Flew Over the Cuckoo's Nest","Kesey")
    patron1 = Patron("Ivan")
    patron2 =Patron("Jimmy")
    patron3 = Patron("Bob")
    
    #Run borrowing checks
    book1.borrow(patron1)
    patron1.addBook(book1)
    
    book1.borrow(patron2)
    
    book1.borrow(patron3)
    
    book2.borrow(patron1)
    patron1.addBook(book2)
    
    book3.borrow(patron1)
    patron1.addBook(book3)
    patron1.addBook(book4)
    
    book4.borrow(patron2)
    patron2.addBook(book4)
    
    #Check Print Status
    print("Book1 : " + str(book1))
    print("Patron1: " + str(patron1))
    

if __name__ == '__main__':
    main()
