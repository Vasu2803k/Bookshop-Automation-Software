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


from tkinter import *
from tkinter import font
root=Tk()

def main_window():
    root.title("BOOKSHOP AUTOMATION SYSTEM")
    software_name=Label(root, text="Welcome to the new version of Bookshop :)", padx=20, pady=40, fg="red", bg="yellow")
    software_name.grid(row=0,column=0,columnspan=2)

#software_name.pack() // cannot be used both grid and pack at once.
def open():
    
    open_label=Label(root, text="Check for availabilty", padx=100, pady=20, bg="Orange")
    open_label.grid(row=2,column=0,columnspan=2)
    input_name=Entry(root, text="Enter Author name or title of the book", width=40, borderwidth=10)
    input_name.grid(row=3,columnspan=2)

def clear_button():
    root2.destroy()
    

def close():
    root.destroy()
    global root2
    root2=Tk()
    root2.title("BOOKSHOP AUTOMATION SYSTEM")
    
    close_label=Label(root2, text="Thanks!, visit again:) ",bg="red", padx=50,pady=50)
    close_label.pack()
    button_clear=Button(root2, text="Clear! ", bg="Blue", padx=50, pady=25, bd=10, command=clear_button)
    button_clear.pack()
    
    
    
def button():   
    
    open_button=Button(root, text="open",bd=10, padx=50, pady=25, command=open, bg="green")
    close_button=Button(root, text="close",bd=10, padx=50, pady=25, command=close, bg="red")
    open_button.grid(row=1,column=0)
    close_button.grid(row=1,column=1)




def user():
    
    main_window()
    button()
def next_user():
    global root2
    root2.destroy()
    user()
start=True

user()
root.mainloop()


'''
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
'''     
user interface contains many options to be selected by the user


def availability_of_book():
    check_availability=input("check for availability of boook ").lower()
    if(check_availability=="yes"):
        print("Enter the key words i.e., Book Title or name of the author")

#learn sql-Database Management System.
'''