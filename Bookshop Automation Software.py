'''
The Bookshop Automation Software (BAS) is to automate all operations in a bookshop.
Generally it includes the Order Processing, Stock Management and Accounts Management. Also
BAS will provide the ability to search any book using the book title or the name of the author
that are available in the shop and in case where the book is not available in the stock, it will ask
the customer to enter full details of the book for procurement of the book in future and
increment a request field for the book.
BAS will help the manager to periodically view the request field of the books so as to arrive at a
rough estimate regarding the current demand for different books. Also it maintains the price of
various books.
'''
print("BOOKSHOP AUTOMATION SYSTEM")
def open_Bookshop():
    print("Welcome to the new version of Bookshop :)")
    print("> Open or close")
    is_type=False
    while not is_type:
        try:
            open_close=(input("> selcect open or close: ").lower())
            if(open_close=="open"):
                print("> Let's get started")
                break
            elif(open_close=="close"):
                print("> Thanks-Visit Again")
                exit()
        except Exception:
            print("> Wrong!-Type/Input correctly")  
            is_type=False
        else:
            print("> only choose 'open' or 'close'")
            is_type=False
        
open_Bookshop() 
books_database=[]      
'''     
user interface contains many options to be selected by the user

'''
def availability_of_book():
    check_availability=input("check for availability of boook ").lower()
    if(check_availability=="yes"):
        print("Enter the key words i.e., Book Title or name of the author")

#learn sql-Database Management System.