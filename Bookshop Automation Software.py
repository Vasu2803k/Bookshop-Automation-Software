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
def enter_button():
    global input_name
    global curr_name
    global root3
    curr_name=input_name.get()
    
    input_name.delete(0, END)
    
    author_name=Label(root3, text="Author name: "+ curr_name.title(), padx=40, pady=40 ,bg="lightblue")
    author_name.grid(row=4,column=0,columnspan=2)
    # check in database 
    
def clear_button():
    global input_name
    input_name.delete(0,END)
def check_availability():
    root.destroy()
    global root3
    global input_name
    global curr_name
    root3=Tk()

    root3.title("BOOKSHOP AUTOMATION SYSTEM")
    input_name=Entry(root3,width=40, borderwidth=10)
    
    check_label=Label(root3, text="Enter Author name or title of the book :)", padx=100, pady=20, bg="yellow")
    check_label.grid(row=0,column=0,columnspan=2)
    input_name.grid(row=1,column=0,columnspan=2)
    
    clear_button1=Button(root3, text="clear",bd=10, padx=80, pady=20, bg="Orange",command=clear_button)
    enter_button1=Button(root3, text="enter",bd=10, padx=80, pady=20, bg="Orange",command=enter_button)
    clear_button1.grid(row=2,column=0)
    enter_button1.grid(row=2,column=1)

    curr_name=input_name.get()
    
    

def open():

    check_availability1=Button(root, text="Check for availabilty",bd=10, padx=100, pady=20, bg="Orange",command=check_availability)
    check_availability1.grid(row=2,column=0,columnspan=2)
    
    
    
#def clear():
#  root2.destroy()
    

def close():
    root.destroy()
    global root2
    root2=Tk()
    root2.title("BOOKSHOP AUTOMATION SYSTEM")
    
    close_label=Label(root2, text="Thanks!, visit again:) ",bg="red", padx=50,pady=50)
    close_label.pack()
    clear1=Button(root2, text="Clear! ", bg="Blue", padx=50, pady=25, bd=10, command=root.quit)
    clear1.pack()
    
    
    
def button():   
    
    open1=Button(root, text="open",bd=10, padx=50, pady=25, command=open, bg="green")
    close1=Button(root, text="close",bd=10, padx=50, pady=25, command=close, bg="red")
    open1.grid(row=1,column=0)
    close1.grid(row=1,column=1)




def user():
    
    main_window()
    button()
def next_user():
    global root2
    root2.destroy()
    user()

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