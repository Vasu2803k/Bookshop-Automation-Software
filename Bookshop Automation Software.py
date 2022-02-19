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
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import ImageTk,Image


# main window
root=Tk()
# changing the colour of main window
root.configure(bg="lightpink")


def main_window():
    

    global Bookshop_img
    # Geometry or dimensions of root Window
    root.geometry('800x680')
    # Displaying Icon
    root.iconbitmap('D:\SDE\Py\Bookshop_icon_2.ico')
    
    # Create Image Widget
    Bookshop_img=ImageTk.PhotoImage(Image.open("D:/SDE/Py/Images/Bookshop_img.png"))
    # text label-Shop name
    text_label=Label(root,text="VS Software",font=('Helvatical bold',50),relief=SUNKEN,bg='ivory3')
    text_label.grid(row=0,column=0,columnspan=3,sticky=W+E,padx=20)
    # Image label
    Bookshop_img_label=Label(root,image=Bookshop_img,anchor=CENTER, relief=SUNKEN,bd=10).grid(row=1,column=1,padx=10,pady=60) 

    # title
    root.title("BOOKSHOP AUTOMATION SYSTEM")
    # frame1
    Bookshop_frame1=LabelFrame(root,text="Bookshop Automation Software :)",relief=SUNKEN)
    Bookshop_frame1.grid(row=1,column=0,padx=18)
    # frame2
    Bookshop_frame2=LabelFrame(root, text="Bookshop Automation Software :)",relief=SUNKEN)
    Bookshop_frame2.grid(row=1,column=2,padx=8)
    
    # Label
    Bookshop_label1=Label(Bookshop_frame1, text="Explore the world's knowledge.", padx=20, pady=20, fg="red", bg="lightblue").pack()
    Bookshop_label2=Label(Bookshop_frame2, text="Explore today, discover tomorrow", padx=20, pady=20, fg="red", bg="lightblue").pack()
    # open button in main window
    Open_button=Button(root,text="OPEN",padx=5,pady=5,relief=SUNKEN,bg="green", anchor=CENTER, command=open_availability)
    Open_button.grid(row=2,column=1)


# Availabilty_func
def open_availability():

    check_availability1=Button(root, text="Check for availabilty",bd=10, padx=80, pady=20, bg="Orange",command=check_availability,anchor=CENTER)
    check_availability1.grid(row=3,column=1,pady=15)
    
    
def check_availability():
    root.destroy()
    global root2
    root2=Tk()
    global input_name
    global curr_name
    
    global Bookshop_img
    
    # title
    root2.title("BOOKSHOP AUTOMATION SYSTEM")
    # colour
    root2.configure(bg="lightpink")
    # Create Image Widget
    Bookshop_img=ImageTk.PhotoImage(Image.open("D:/SDE/Py/Images/Bookshop_img.png"))
    # text label-Shop name
    text_label=Label(root2,text="VS Software",font=('Helvatical bold',50),relief=SUNKEN,bg='ivory3')
    text_label.grid(row=0,column=0,columnspan=3,sticky=W+E,padx=20)
    # Image label
    Bookshop_img_label=Label(root2,image=Bookshop_img,anchor=CENTER, relief=SUNKEN,bd=10).grid(row=1,column=1,padx=10,pady=50) 

    # frame1
    Bookshop_frame1=LabelFrame(root2,text="Bookshop Automation Software :)",relief=SUNKEN)
    Bookshop_frame1.grid(row=1,column=0,padx=18)
    # frame2
    Bookshop_frame2=LabelFrame(root2, text="Bookshop Automation Software :)",relief=SUNKEN)
    Bookshop_frame2.grid(row=1,column=2,padx=8)
    
    # Label
    Bookshop_label1=Label(Bookshop_frame1, text="Explore the world's knowledge.", padx=20, pady=20, fg="red", bg="lightblue").pack()
    Bookshop_label2=Label(Bookshop_frame2, text="Explore today, discover tomorrow", padx=20, pady=20, fg="red", bg="lightblue").pack()
    # Text widget (Author name)
    text_label=Label(root2, text="Enter Author name or title of the book :)", padx=20, pady=15, bg="ivory3",font=("Times new roman",14,BOLD))
    text_label.grid(row=2,column=0,columnspan=5,sticky=W+E,padx=50)

    # Entry Widget
    input_name=Entry(root2,width=40, borderwidth=10)
    input_name.grid(row=3,column=0,columnspan=5,sticky=W+E,padx=30)
    # clear, enter, exit buttons
    # clear button
    clear_button1=Button(root2, text="CLEAR",bd=10, padx=50, pady=20, bg="Orange",command=clear_button)
    # enter button
    enter_button1=Button(root2, text="ENTER",bd=10, padx=50, pady=20, bg="Orange",command=enter_button)
    clear_button1.grid(row=4,column=0,pady=10)
    enter_button1.grid(row=4,column=1,pady=10)
    exit_button1=Button(root2, text="EXIT",bd=10, padx=50, pady=20, bg="Orange",command=exit_button)
    exit_button1.grid(row=4,column=2,pady=10)


    #curr_name=input_name.get()
    
def database_window():

    
    
    global curr_name
    global database_img
    root4=Toplevel()
    # Geometry or dimensions of root Window
    root4.geometry('800x680')
    # Displaying Icon
    root4.iconbitmap('D:\SDE\Py\Bookshop_icon_2.ico')
    # title
    root4.title("BOOKSHOP AUTOMATION SYSTEM")
    # colour
    root4.configure(bg="ivory3")
    
    
    # Create Image Widget
    database_img=ImageTk.PhotoImage(Image.open('D:\SDE\Py\Images\database_img.png'))
    # text label-Shop name
    text_label=Label(root4,text="VS Software",font=('Helvatical bold',50),relief=SUNKEN,bg='lightblue')
    text_label.grid(row=0,column=0,columnspan=5,sticky=W+E,padx=10)

    # Image label
    database_image_label=Label(root4,image=database_img,relief=SUNKEN,bd=10).grid(row=1,column=1,padx=50,pady=20) 


    
    input_frame=LabelFrame(root4, text="Entered Input",padx=40,pady=20,bg="ivory3",relief=SUNKEN)
    input_frame.grid(row=1,column=0,padx=20)

    #input frame
    input_show=Label(input_frame, text=curr_name.title(), padx=121,pady=15,relief=SUNKEN)
    input_show.grid(row=0,column=0)

    load_gif=Label(root4, text=" Loading, Please Wait :)", padx=50, pady=10 ,bg="yellow",relief=SUNKEN,bd=10)
    load_gif.grid(row=2,column=0,padx=10)

    # back button
    back1=Button(root4, text=" BACK TO EXPLORE ", bg="orange", padx=50, pady=10, bd=10,relief=SUNKEN, command=root4.destroy)
    back1.grid(row=2,column=1)
    # check in database


def enter_button():
    global input_name
    global curr_name
    
    curr_name=input_name.get()
    if(curr_name=='' or curr_name==' '):
        messagebox.showwarning(" ALERT!","Input the thing you are looking for :) ")
    else:
        input_name.delete(0, END)
        database_window()
    
    
def clear_button():
    global input_name
    input_name.delete(0,END)

    
def exit_button():
    
    root3=Toplevel()
    root3.title("BOOKSHOP AUTOMATION SYSTEM")
    # Geometry or dimensions of root Window
    root3.geometry('300x300')
    # Displaying Icon
    root3.iconbitmap('D:\SDE\Py\Bookshop_icon_2.ico')
    # changing the colour of window
    root3.configure(bg="lightpink")

    close_label=Label(root3, text="Thanks!, visit again:) ",padx=50,pady=50,relief=SUNKEN,bg="ivory3",font=("Times new roman",14,BOLD))
    close_label.pack()
    
    clear1=Button(root3, text=" CLEAR ", bg="red", padx=60, pady=25, bd=10,relief=SUNKEN, command=root2.destroy)
    clear1.pack(pady=5)

    # back button
    back1=Button(root3, text=" BACK TO EXPLORE ", bg="orange", padx=60, pady=25, bd=10,relief=SUNKEN, command=root3.destroy)
    back1.pack(pady=5)
    


 
def user():
    
    main_window()
    
    
def next_user():
    main_window()

user()
next_user()
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