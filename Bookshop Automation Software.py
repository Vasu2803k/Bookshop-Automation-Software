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

from datetime import datetime,date
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import ImageTk,Image, ImageSequence
import time
import mysql
import mysql.connector as connector
from mysql.connector import Error


# create a database or connect to one 
def create_connection(host_name,user_name,password,auth_plugin_name,database_name):
    connection_temp=None
    try:
        connection_temp=connector.connect(host=host_name,user=user_name,
                     passwd=password,auth_plugin=auth_plugin_name,database=database_name)
        print("connection succeeded")
    except Error as err:
        print(f"Error: {err}")
    return connection_temp


def root_access():
    global rootaccess
    
    global Bookshop_img_access
    rootaccess=Tk()
    rootaccess.configure(bg="orange")
    rootaccess.geometry('800x680')
    rootaccess.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
    # Create Image Widget
    Bookshop_img_access=ImageTk.PhotoImage((Image.open("D:\Project_1\Images_Icons\Bookshop_img2.jpeg")).resize((320,300)))
    #Bookshop_img_access=Bookshop_img_access.resize((300,300))
    # text label-Shop name
    text_label_access=Label(rootaccess,text="VS Book Store",font=('Helvatical bold',50),relief=SUNKEN,bg='ivory3')
    text_label_access.grid(row=0,column=0,columnspan=3,sticky=W+E,padx=20)
    # Image label
    Bookshop_img_label_access=Label(rootaccess,image=Bookshop_img_access,anchor=CENTER, relief=SUNKEN,bd=10).grid(row=1,column=1,padx=10,pady=60) 

    # title
    rootaccess.title("BOOKSHOP AUTOMATION SYSTEM")
    # frame1
    Bookshop_frame1_access=LabelFrame(rootaccess,text="Bookshop Automation Software :)",relief=SUNKEN)
    Bookshop_frame1_access.grid(row=1,column=0,padx=10)
    # frame2
    Bookshop_frame2_access=LabelFrame(rootaccess, text="Bookshop Automation Software :)",relief=SUNKEN)
    Bookshop_frame2_access.grid(row=1,column=2,padx=8)
    # Label
    Bookshop_label1_access=Label(Bookshop_frame1_access, text="Bookshops are the places of\n magical discoveries and\n the rediscovery of past pleasures", padx=10, pady=20, fg="darkred", bg="lightgreen").pack()
    Bookshop_label2_access=Label(Bookshop_frame2_access, text="That's the thing about books.\nThey let you travel without\n moving your feet", padx=20, pady=20, fg="darkred", bg="lightgreen").pack()
    # two buttons
    
    VS_button=Button(rootaccess,text="VS Member",relief=SUNKEN,bg="lightgreen",command=VS_Member, anchor=CENTER,padx=28,pady=9,font=(("Times New Roman",15)),borderwidth=5)
    VS_button.place(x=230,y=480)

    customer_button=Button(rootaccess,text="Customer",relief=SUNKEN,bg="lightgreen",command=customer,anchor=CENTER,padx=36,pady=9,font=(("Times New Roman",15)),borderwidth=5)
    customer_button.place(x=405,y=480)

    Status_bar=Label(rootaccess,text="WELCOME TO THE NEW VERSION OF BOOKSTORE",anchor=CENTER,padx=50,font=(("Helvetica",20)),bg="orange",fg="darkblue")
    Status_bar.place(x=10,y=630)

    Logout_button=Button(rootaccess,text="LOGOUT",relief=SUNKEN,bg="red",command=exit_program, anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",15)),borderwidth=5)
    Logout_button.place(x=335,y=550)
    
    

def exit_program():

    #yes_no messagebox
    global rootaccess
    yes_no=messagebox.askyesno("Warning! ","Do you really want to exit? ")
    
    if(yes_no):
        exit()
        rootaccess.quit()
    else:
        return
    

def customer_entry():
    global name_entry
    global contact_entry
    global address_entry
    global cursor
    global connection
    name=name_entry.get()
    date_time=date.today()
    sql_query="INSERT INTO customer_details(full_name,contact_number,address,time_date) values(%s,%s,%s,%s);"
    cursor.execute(sql_query,(name,contact_entry.get(),address_entry.get(),date_time))
    print(cursor.fetchall())
    
def enter_button():
    global name_entry
    global contact_entry
    global address_entry

    res = (any((ord(ele)>=65 and ord(ele)<=90) or (ord(ele)>=97 and ord(ele)<=122) for ele in contact_entry.get()))

    if(name_entry.get()=="" or name_entry.get()==" " or len(name_entry.get())<7):
        messagebox.showwarning(" ALERT!","Input your name and proceed (Atleast 7 letters):) ")
        name_entry.delete(0, END)
    
    elif(len(contact_entry.get())!=10):
        messagebox.showerror(" ALERT!", "Entered more or less numbers! Contact number should be of 10 numbers. Press 'ok' to enter again")
        
        contact_entry.delete(0,END)
    
    elif(res==True):
        messagebox.showwarning(" ALERT!", "Entered alphabet/s. Press 'ok' to enter again")
        contact_entry.delete(0,END)  
        
    elif(len(address_entry.get())<10):
        messagebox.showerror(" ALERT!", "Entered less characters! Address should be of atleast 10 characters. Press 'ok' to enter again")
        address_entry.delete(0, END)
    else:
        books()
        customer_entry()



def customer_window():

    global rootaccess
    rootaccess.destroy()

    global root
    global Bookshop_img
    global name_entry
    global contact_entry
    global address_entry

    # main window
    root=Tk()
    
    # changing the colour of main window
    root.configure(bg="orange")

    # Geometry or dimensions of root Window
    root.geometry('800x680')
    # Displaying Icon
    root.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
    # Create Image Widget
    Bookshop_img=ImageTk.PhotoImage((Image.open("D:\Project_1\Images_Icons\Bookshop_img.png")).resize((320,300)))
    
     # title
    root.title("BOOKSHOP AUTOMATION SYSTEM")
   
    # text label-Shop name
    text_label=Label(root,text="VS Book Store",font=('Helvatical bold',50),relief=SUNKEN,bg='ivory3',anchor=CENTER,padx=50)
    text_label.grid(row=0,column=0,sticky=W+E,columnspan=7,padx=12)
    
    Bookshop_frame1=LabelFrame(root,text="Bookshop Automation Software :)",relief=SUNKEN)
    Bookshop_frame1.grid(row=1,column=0,padx=5)

    Bookshop_label1=Label(Bookshop_frame1, text="Explore the world's knowledge", padx=20, pady=20, fg="darkred",bg="lightgreen").pack()
    Bookshop_frame2=LabelFrame(root,text="Bookshop Automation Software :)",relief=SUNKEN)

    Bookshop_frame2.grid(row=1,column=3,padx=5)
    Bookshop_label2=Label(Bookshop_frame2, text="Explore today, discover tomorrow", padx=10, pady=20, fg="darkred",bg="lightgreen").pack()
    # Image label
    Bookshop_img_label=Label(root,image=Bookshop_img,anchor=CENTER, relief=SUNKEN,bd=10).grid(row=1,column=1,pady=25) 

    name_label=Label(root,text="Full name ",relief=SUNKEN,bg='azure',padx=20)
    name_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)
    contact_label=Label(root,text="Contact ",relief=SUNKEN,bg='azure',padx=25)
    contact_label.grid(row=3,column=0,padx=5,pady=10,sticky=W)
    address_label=Label(root,text="Address ",relief=SUNKEN,bg='azure',padx=25)
    address_label.grid(row=4,column=0,padx=5,pady=10,sticky=W)
    
    # Entry Widgets
    name_entry=Entry(root,width=90,borderwidth=2)
    name_entry.grid(row=2,column=0,columnspan=4,padx=125)
    contact_entry=Entry(root,width=90,borderwidth=2)
    contact_entry.grid(row=3,column=0,columnspan=4,padx=125)
    address_entry=Entry(root,width=90,borderwidth=2)
    address_entry.grid(row=4,column=0,columnspan=4,padx=125)
    enter_button1=Button(root, text="ENTER",bd=10, padx=40, pady=10, bg="green",command=enter_button)
    enter_button1.place(x=350,y=600)

def reading_gif():
    global loaded_img
    global gif_display
    
    load_gif=Label(gif_display,bg="ivory3")
    load_gif.pack(padx=20,pady=20)
    img=Image.open('D:/Project_1/Images_Icons/reading_gif.gif')
    
    for img in ImageSequence.Iterator(img):
        try:
            img=img.resize((775,350))
            loaded_img=ImageTk.PhotoImage(img)
            load_gif.configure(image=loaded_img)
            gif_display.update()
            time.sleep(0.001)
        except TypeError:
            pass
        except TclError:
            pass
    else:
        gif_display.destroy()

def add_to_cart(isbn_no,title,author,price):
    global name_entry
    global cursor
    global connection
    books_quantity=simpledialog.askinteger("Input:)","Enter the number of books on your selection of purchase")
    cust_name=name_entry.get()
    sql_query="INSERT INTO cart(customer_name,isbn_no,title,author,no_of_books,sell_price) VALUES(%s,%s,%s,%s,%s,%s);"

    cursor.execute(sql_query,(cust_name,isbn_no,title,author,books_quantity,price))
    
    print(cursor.fetchall())
def cart_win():
    global checkout_frame
    cart_window=Tk()
    cart_window.title("Cart")
    cart_window.configure(bg="orange")

    checkout_frame=Frame(root1,padx=5,pady=5,bg="coral")
    checkout_frame.place(x=0,y=280,height=350,width=280)

    # Geometry or dimensions of root Window
    cart_window.geometry('500x500')
    # Displaying Icon
    cart_window.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
def search_author():
    global author_or_book_entry
    
    global entry_number
    global books_frame
    global gif_display
    
    gif_display=Toplevel()
    gif_display.title("Reading gif:)")
    # changing the colour of main window
    gif_display.configure(bg="orange")

    # Geometry or dimensions of root Window
    gif_display.geometry('800x400')
    # Displaying Icon
    gif_display.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
    reading_gif()
    clear_func1()

    ISBN_label=Label(books_frame,text="ISBN",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=47,anchor=CENTER,bg="violet")
    ISBN_label.place(x=5,y=5)
    title_author_label=Label(books_frame,text="Title | Author",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=50,bg="violet")
    title_author_label.place(x=145,y=5)
    quantity_label=Label(books_frame,text="N_Books",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=8,bg="violet")
    quantity_label.place(x=360,y=5)
    Rack_label=Label(books_frame,text="Rack No",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=12,bg="violet")
    Rack_label.place(x=455,y=5)
    price_label=Label(books_frame,text="Price",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=32,bg="violet")
    price_label.place(x=562,y=5)
    buy_label=Label(books_frame,text="Add to cart",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=5,bg="violet")
    buy_label.place(x=675,y=5)

    query="SELECT author_name FROM inventory;"
    cursor.execute(query)
    author_list=cursor.fetchall()

    global books_details1
    result_title=""
    for book1 in author_list:
        if (author_or_book_entry.get().lower() in book1[0].lower() ):
            result_title=book1[0]
            sql_query="SELECT * FROM inventory WHERE author_name=(%s)"
            cursor.execute(sql_query,(result_title,))
            books_details1=cursor.fetchall()
            print(books_details1)
            break
    else:
        messagebox.showerror("Error", "No books found using this keyword, modify the text or Use other keywords.")
        author_or_book_entry.delete(0,END)
        clear_func1()

    
    if(author_or_book_entry.get()):
        author_or_book_entry.delete(0,END)
        size=0
        for book in books_details1:
            ISBN_label1=Label(books_frame,text=book[0],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,anchor=CENTER,bg="coral")
            ISBN_label1.place(x=12,y=60+size)
            title_author_label1=Label(books_frame,text=f"{book[1]}\n{book[2]}",font=("Helvetica",9),bg="coral")
            title_author_label1.place(x=165,y=60+size)
            quantity_label1=Label(books_frame,text=book[4],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=4,bg="coral")
            quantity_label1.place(x=385,y=60+size)
            Rack_label1=Label(books_frame,text=book[5],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=12,bg="coral")
            Rack_label1.place(x=470,y=60+size)
            price_label1=Label(books_frame,text=book[6],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=15,bg="coral")
            price_label1.place(x=580,y=60+size)
            
        
            buy_button1=Button(books_frame,text=" BUY ",font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=5,bg="green",command=lambda: add_to_cart(book[0],book[1],book[2],book[6]))
            buy_button1.place(x=692,y=60+size)
        
            size+=55
    
   
def search_book():
    
    global author_or_book_entry
    global entry_number
    global books_frame
    global gif_display
    global books_details
    #global author_or_book_entry
    
    gif_display=Toplevel()
    gif_display.title("Reading gif:)")
    # changing the colour of main window
    gif_display.configure(bg="orange")
    # Geometry or dimensions of root Window
    gif_display.geometry('800x400')
    # Displaying Icon
    gif_display.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')

    reading_gif()
    clear_func1()
    
    ISBN_label=Label(books_frame,text="ISBN",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=47,anchor=CENTER,bg="violet")
    ISBN_label.place(x=5,y=5)
    title_author_label=Label(books_frame,text="Title | Author",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=50,bg="violet")
    title_author_label.place(x=145,y=5)
    quantity_label=Label(books_frame,text="N_Books",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=8,bg="violet")
    quantity_label.place(x=360,y=5)
    Rack_label=Label(books_frame,text="Rack No",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=12,bg="violet")
    Rack_label.place(x=455,y=5)
    price_label=Label(books_frame,text="Price",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=32,bg="violet")
    price_label.place(x=562,y=5)
    buy_label=Label(books_frame,text="Add to cart",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=5,bg="violet")
    buy_label.place(x=675,y=5)
    query="SELECT title FROM inventory"

    cursor.execute(query)
    book_list=cursor.fetchall()
    print(book_list)
    
    books_details=[]
    result_title=""
    for book1 in book_list:
        if author_or_book_entry.get().lower() in book1[0].lower():
            result_title=book1[0]
            sql_query="SELECT * FROM inventory WHERE title=(%s)"
            cursor.execute(sql_query,(result_title,))
            books_details=cursor.fetchall()
            break
    else:
        messagebox.showerror("Error", "No books found using this keyword, modify the text or Use other keywords.")
        author_or_book_entry.delete(0,END)
        clear_func1()
    if(author_or_book_entry.get()):
        size=0
        for book in books_details:
            ISBN_label1=Label(books_frame,text=book[0],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,anchor=CENTER,bg="coral")
            ISBN_label1.place(x=12,y=60+size)
            title_author_label1=Label(books_frame,text=f"{book[1]}\n{book[2]}",font=("Helvetica",9),bg="coral")
            title_author_label1.place(x=165,y=60+size)
            quantity_label1=Label(books_frame,text=book[4],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=4,bg="coral")
            quantity_label1.place(x=385,y=60+size)
            Rack_label1=Label(books_frame,text=book[5],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=12,bg="coral")
            Rack_label1.place(x=470,y=60+size)
            price_label1=Label(books_frame,text=book[6],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=15,bg="coral")
            price_label1.place(x=580,y=60+size)
            
        
            buy_button1=Button(books_frame,text=" BUY ",font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=5,bg="green",command=lambda: add_to_cart(book[0],book[1],book[2],book[6]))
            buy_button1.place(x=692,y=60+size)
        
            size+=55
            
def request_field():
    global customer_name_entry
    global contact_no_entry
    global book_title_entry
    global author_name_entry
    global cursor
    global connection
    customer_name=customer_name_entry.get().title()
    contact_no=contact_no_entry.get()
    book_title=book_title_entry.get().title()
    author_name=author_name_entry.get().title()
    customer_name_entry.delete(0,END)
    contact_no_entry.delete(0,END)
    book_title_entry.delete(0,END)
    author_name_entry.delete(0,END)
    date_time=datetime.now()
    now1=date_time.strftime('%Y-%M-%D %H:%M:%S')
    
    sql_query="INSERT INTO request_field(date_time, customer_name, contact_number,book_title, book_author) values(%s,%s,%s,%s,%s)"
    cursor.execute(sql_query,(now1,
                              customer_name,contact_no,book_title,author_name))
    print(cursor.fetchall())
    return


def Request_func():
    global customer_name_entry
    global contact_no_entry
    global book_title_entry
    global author_name_entry
    
    
    
    request_win=Tk()
    request_win.configure(bg="orange")
    request_win.geometry('600x500')
    request_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
    
    text_label_access=Label(request_win,text="VS Book Store",font=('Helvatical bold',30),relief=SUNKEN,bg='ivory3',padx=120)
    text_label_access.grid(row=0,column=0,columnspan=3,sticky=W+E,padx=40)
    
    request_win.title("Request Window | BOOKSHOP AUTOMATION SYSTEM")
    
    customer_name=Label(request_win,text="Name",relief=SUNKEN,padx=14,pady=5)
    customer_name.place(x=5,y=150)
    contact_no=Label(request_win,text="Contact",relief=SUNKEN,padx=9,pady=5)
    contact_no.place(x=5,y=190)
    book_title=Label(request_win,text="Title",relief=SUNKEN,padx=18,pady=5)
    book_title.place(x=5,y=230)
    author_name=Label(request_win,text="Author",relief=SUNKEN,padx=11,pady=5)
    author_name.place(x=5,y=270)
    
    customer_name_entry=Entry(request_win,width=80,borderwidth=5)
    customer_name_entry.place(x=80,y=150)
    contact_no_entry=Entry(request_win,width=80,borderwidth=5)
    contact_no_entry.place(x=80,y=190)
    book_title_entry=Entry(request_win,width=80,borderwidth=5)
    book_title_entry.place(x=80,y=230)
    author_name_entry=Entry(request_win,width=80,borderwidth=5)
    author_name_entry.place(x=80,y=270)
    
    
    insert_button=Button(request_win,text="Submit",relief=SUNKEN,padx=15,pady=8,bd=5,bg="green",command=request_field)
    insert_button.place(x=250,y=370)

def clear_func1():
    global books_frame
    for widget in books_frame.winfo_children():
        widget.destroy()

def books():
    global author_or_book_entry
    global checkout_frame
    global books_frame
    global root1
    

    root1=Toplevel()
    root1.geometry('800x680')
    root1.title("BOOKSHOP AUTOMATION SYSTEM")
    # colour
    root1.configure(bg="orange")
    root1.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')

    text_label=Label(root1,text="VS Book Store",font=('Helvatical bold',50),relief=SUNKEN,bg='ivory3',padx=70)
    text_label.grid(row=0,column=0,columnspan=4,sticky=W+E,padx=30)

    author_book_label=Label(root1, text="Enter title or author name ",relief=SUNKEN,font=('Helvatical bold',17),anchor=CENTER,borderwidth=12)
    author_book_label.grid(row=1,column=0,padx=150,sticky=W+E,pady=10)

    author_or_book_entry=Entry(root1,width=90, borderwidth=2)
    author_or_book_entry.grid(row=2,column=0,padx=100)

    clear_label=Button(root1,text="Clear Results",padx=9,pady=10,font=("Helvetica",14),bg="lightgreen",relief=SUNKEN,borderwidth=5,command=clear_func1)
    clear_label.place(x=330,y=630)

    author_button=Button(root1, text="Search by AUTHOR NAME",relief=SUNKEN,bg="green",padx=10,pady=5,borderwidth=10,command=search_author)
    author_button.place(x=60,y=200)
    bookname_button=Button(root1, text="Search by BOOK NAME",relief=SUNKEN,bg="green",padx=17,pady=5,borderwidth=10,command=search_book)
    bookname_button.place(x=295,y=200)

    books_frame=Frame(root1,padx=5,pady=5,bg="coral")
    books_frame.place(x=0,y=270,height=360,width=800)

    books_label=Label(root1,text="Books",padx=30,pady=10,font=("Helvetica",14),bg="brown",relief=SUNKEN,borderwidth=5)
    books_label.place(x=80,y=630)

    
    request_button=Button(root1,text="Request for book",bg="green",relief=SUNKEN,padx=25,pady=5,borderwidth=10,command=Request_func)
    request_button.place(x=530,y=200)

    cart_label=Button(root1,text=" Show Cart ",padx=12,pady=10,font=("Helvetica",14),bg="green",relief=SUNKEN,borderwidth=5,command=cart_win)
    cart_label.place(x=580,y=630)
           
    #checkout_button=Button(root1, text="Proceed to checkout",relief=SUNKEN,bg="green",padx=10,pady=5,borderwidth=5,command=search_author)
    #checkout_button.place(x=80,y=630)


    
def customer():
    customer_window()



def VS_Member():
    
    
    VS_root=Toplevel()
    # changing the colour of main window
    VS_root.configure(bg="orange")


    # Geometry or dimensions of root Window
    VS_root.geometry('800x680')

    # Displaying Icon
    VS_root.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    VS_root.title("BOOKSHOP AUTOMATION SYSTEM")

    sales_clerk_button=Button(VS_root,text="Sales Clerk",padx=8,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="lightgreen",command=lambda: VS_access("Sales Clerk"))
    sales_clerk_button.place(x=350,y=150)
    employee_button=Button(VS_root,text="Employee",padx=15,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="lightgreen",command=lambda: VS_access("Employee"))
    employee_button.place(x=350,y=230)
    manager_button=Button(VS_root,text="Manager",padx=21,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="lightgreen",command=lambda: VS_access("Manager"))
    manager_button.place(x=350,y=310)
    Owner_button=Button(VS_root,text="Owner",padx=32,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="lightgreen",command=lambda: VS_access("Owner"))
    Owner_button.place(x=350,y=390)
    
    main_window_button=Button(VS_root,text="Back to previous window/Page",padx=2,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="green",command=VS_root.destroy)
    main_window_button.place(x=280,y=630)



def Checkout():
    global sales_win
    global print_button
    sql_query="SELECT ISBN,title,quantity,sell_price FROM checkout_list;"
    #cursor.execute(sql_query)
    #items_list=cursor.fetchall()
    checkout_label=LabelFrame(sales_win,text="Checkout Label:) ")
    checkout_label.place(x=50,y=300,width=400,height=200)
    heading_label=Label(checkout_label,text= "| ISBN     | Title      | Quantity    | sell_price |",borderwidth=5)
    heading_label.pack(padx=5,pady=5)


    print_button.configure(state=ACTIVE)
    

def sales_window():
    
    global sales_win
    global print_button
    sales_win=Toplevel()
    # changing the colour of main window
    sales_win.configure(bg="orange")
    # Geometry or dimensions of root Window
    sales_win.geometry('800x680')
    # Displaying Icon
    sales_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    sales_win.title("BOOKSHOP AUTOMATION SYSTEM")
    
    items_list_button=Button(sales_win,text="Checkout List", relief=SUNKEN,padx=20,pady=10,font=("Helvetica",14),bg="lightgreen",command=Checkout)
    items_list_button.place(x=50,y=50)
    print_button=Button(sales_win,text="Print Reciept", relief=SUNKEN,padx=20,pady=10,font=("Helvetica",14),bg="lightgreen",command=Checkout,state=DISABLED)
    print_button.place(x=50,y=150)
    
    
def sales_clerk():
    
    sales_win=Toplevel()
    # changing the colour of main window
    sales_win.configure(bg="orange")


    # Geometry or dimensions of root Window
    sales_win.geometry('800x680')
    # Displaying Icon
    sales_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    sales_win.title("Sales Clerk | BOOKSHOP AUTOMATION SYSTEM")
    return

def employee_window():
    
    employee_win=Toplevel()
    # changing the colour of main window
    employee_win.configure(bg="orange")


    # Geometry or dimensions of root Window
    employee_window.geometry('800x680')
    # Displaying Icon
    employee_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    employee_win.title("Employee | BOOKSHOP AUTOMATION SYSTEM")
    return
def manager_window():
    
    manager_win=Toplevel()
    # changing the colour of main window
    manager_win.configure(bg="orange")


    # Geometry or dimensions of root Window
    manager_win.geometry('800x680')
    # Displaying Icon
    manager_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    manager_win.title("Manager | BOOKSHOP AUTOMATION SYSTEM")
    return
def owner_window():
    
    owner_win=Toplevel()
    # changing the colour of main window
    owner_win.configure(bg="orange")


    # Geometry or dimensions of root Window
    owner_win.geometry('800x680')
    # Displaying Icon
    owner_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    owner_win.title("Owner | BOOKSHOP AUTOMATION SYSTEM")
    return

# checks whether data found or not
def check_vs_member(employee_type):
    global user_name_entry
    global password_entry
    
    sql_query="SELECT username, user_password,employee_type FROM vs_members;"
    cursor.execute(sql_query)
    users_list=cursor.fetchall()
    for user,passwd,emp_type in users_list:
        if(emp_type.lower()==employee_type.lower() and user.lower()==user_name_entry.get().lower() and passwd==password_entry.get()):
            messagebox.showinfo("Access Granted","Validation successful, Access granted!")
            if(emp_type.lower()=="Sales Clerk".lower()):
                sales_window()
            elif(emp_type.lower()=="Employee".lower()):
                employee_window()
            elif(emp_type.lower()=="Manager".lower()):
                manager_window()
            elif(emp_type.lower()=="Owner".lower()):
                owner_window()
            break
            
    else:
        messagebox.askretrycancel("Access Denied","Sorry!,username or password is incorrect")


def clear():
    global VS_access_window
    global password_entry
    global user_name_entry
    password_entry.delete(0,END)
    user_name_entry.delete(0,END)


def VS_access(employee_type):
    
    global VS_access_window
    global password_entry
    global user_name_entry
    VS_access_window=Toplevel()
    # changing the colour of main window
    VS_access_window.configure(bg="orange")


    # Geometry or dimensions of root Window
    VS_access_window.geometry('800x680')
    # Displaying Icon
    VS_access_window.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    VS_access_window.title("BOOKSHOP AUTOMATION SYSTEM")

   
    
    user_name=Label(VS_access_window,text="Username",padx=15,pady=10,relief=SUNKEN)
    user_name.place(x=100,y=400)

    user_name_entry=Entry(VS_access_window,width=90,borderwidth=10)
    user_name_entry.place(x=200,y=400)

    password_label=Label(VS_access_window,text="Password",padx=15,pady=10,relief=SUNKEN)
    password_label.place(x=100,y=450)

    password_entry=Entry(VS_access_window,width=90,borderwidth=10)
    password_entry.place(x=200,y=450)
    
    # clear button
    clear_button1=Button(VS_access_window, text="CLEAR",bd=10, padx=50, pady=10, bg="lightgreen",command=clear)
    clear_button1.place(x=180,y=600)
    # enter button
    
    enter_button1=Button(VS_access_window, text="ENTER",bd=10, padx=50, pady=10, bg="lightgreen",command=lambda: check_vs_member(employee_type))
    enter_button1.place(x=350,y=500)
    exit_button1=Button(VS_access_window ,text="EXIT",bd=10, padx=50, pady=10, bg="lightgreen",command=VS_access_window.destroy)
    exit_button1.place(x=520,y=600)
    
    play_gif()



count=0
def play_gif():
    global loaded_img
    global VS_access_window
    global count
    load_gif=Label(VS_access_window,bg="orange")
    load_gif.grid(row=2,column=0,padx=150)
    img=Image.open('D:/Project_1/Images_Icons/Hiding_eyes3.gif')
    
    
    for img in ImageSequence.Iterator(img):
        try:
            img=img.resize((500,320))
            loaded_img=ImageTk.PhotoImage(img)
            load_gif.configure(image=loaded_img)
            VS_access_window.update()
        #count+=1
        #if(count==40):
            #break
            time.sleep(0.1)
        except TypeError:
            pass
        except TclError:
            pass
    try:
        VS_access_window.after(1500,play_gif())

    except TclError:
        pass
    
    #if(count!=40):
        #load_gif.after(0,play_gif)
        
    #else:
        #load_gif.destroy()  

        


connection=create_connection('localhost','root','V@$u#1528','mysql_native_password','Bookshop_database')
cursor=connection.cursor() 
#cursor.execute("CREATE TABLE vs_members( emp_id int,username varchar(40), password varchar(15), PRIMARY KEY (emp_id));" )

# Do the related stuff
#cursor.execute("ALTER TABLE vs_members add Employee_Type varchar(40);")


#Added

'''
doj=date.today()
sql_query2="insert into vs_members values(103,'Dileep103',22,'Adilabad,Telangana',%s,'Dileep#103','Employee')"
    
cursor.execute(sql_query2,(doj,))
'''

root_access()

#commit changes
connection.commit()
'''
def close_connection():
    #close the connnection
    if connection and cursor:
        cursor.close()
        connection.close()
close_connection()
'''
rootaccess.mainloop()


