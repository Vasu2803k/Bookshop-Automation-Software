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
def create_connection(host_name,user_name,password,database_name):
    connection_temp=None
    try:
        connection_temp=connector.connect(host=host_name,user=user_name,
                     passwd=password,database=database_name)
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
    rootaccess.title("Main Window | BOOKSHOP AUTOMATION SYSTEM")
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

    Logout_button=Button(rootaccess,text="Logout",relief=SUNKEN,bg="red",command=exit_program, anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",15)),borderwidth=5)
    Logout_button.place(x=335,y=550)
    
    



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
    VS_access_window.title("VS_access | BOOKSHOP AUTOMATION SYSTEM")

    enter_details=Label(VS_access_window,text="Enter user name and password",padx=25,pady=10,relief=SUNKEN,bg="violet")
    enter_details.place(x=315,y=350)
    
    user_name=Label(VS_access_window,text="Username",padx=15,pady=10,relief=SUNKEN)
    user_name.place(x=100,y=400)

    user_name_entry=Entry(VS_access_window,width=90,borderwidth=10)
    user_name_entry.place(x=200,y=400)

    password_label=Label(VS_access_window,text="Password",padx=15,pady=10,relief=SUNKEN)
    password_label.place(x=100,y=450)

    password_entry=Entry(VS_access_window,show="*",width=90,borderwidth=10)
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



# checks whether data found or not
def check_vs_member(employee_type):
    global user_name_entry
    global password_entry
    global VS_access_window
    sql_query="SELECT username, user_password,employee_type FROM vs_members;"
    cursor.execute(sql_query)
    users_list=cursor.fetchall()
    for user,passwd,emp_type in users_list:
        if(emp_type.lower()==employee_type.lower() and user.lower()==user_name_entry.get().lower() and passwd==password_entry.get()):
            messagebox.showinfo("Access Granted","Validation successful, Access granted!")
            if(emp_type.lower()=="Sales Clerk".lower()):
                VS_access_window.destroy()
                sales_window()
            elif(emp_type.lower()=="Employee".lower()):
                VS_access_window.destroy()
                employee_window()
            elif(emp_type.lower()=="Manager".lower()):
                VS_access_window.destroy()
                manager_window()
            elif(emp_type.lower()=="Owner".lower()):
                VS_access_window.destroy()
                owner_window()
            break
    
    else:
        prompt_reply=messagebox.askretrycancel("Access Denied","Sorry!,Click Retry to enter again or cancel to exit")
        if(prompt_reply==True):
            password_entry.delete(0,END)
            user_name_entry.delete(0,END)
            
        else:
            VS_access_window.destroy()
        

def backy(present_win,previous_win):
    #global rootaccess
    #global root
    present_win.withdraw()
    previous_win.wm_deiconify()

def clear():
    global VS_access_window
    global password_entry
    global user_name_entry
    password_entry.delete(0,END)
    user_name_entry.delete(0,END)


def VS_Member():
    global VS_root
    global rootaccess

    rootaccess.withdraw()

    VS_root=Toplevel()
    # changing the colour of main window
    VS_root.configure(bg="orange")


    # Geometry or dimensions of root Window
    VS_root.geometry('800x680')

    # Displaying Icon
    VS_root.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    VS_root.title("VS_Member | BOOKSHOP AUTOMATION SYSTEM")

    sales_clerk_button=Button(VS_root,text="Sales Clerk",padx=8,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="lightgreen",command=lambda: VS_access("Sales Clerk"))
    sales_clerk_button.place(x=350,y=150)
    employee_button=Button(VS_root,text="Employee",padx=15,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="lightgreen",command=lambda: VS_access("Employee"))
    employee_button.place(x=350,y=230)
    manager_button=Button(VS_root,text="Manager",padx=21,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="lightgreen",command=lambda: VS_access("Manager"))
    manager_button.place(x=350,y=310)
    Owner_button=Button(VS_root,text="Owner",padx=32,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="lightgreen",command=lambda: VS_access("Owner"))
    Owner_button.place(x=350,y=390)
    
    main_window_button=Button(VS_root,text="Back to previous window/Page",padx=2,pady=8,relief=SUNKEN,font=("Helvetica",14),bg="green",command=lambda: backy(VS_root,rootaccess))
    main_window_button.place(x=280,y=630)



def customer_window():

    global rootaccess
    rootaccess.withdraw()
    '''
    if(rootaccess):
        rootaccess.destroy()
    else:
        pass
        '''
    global root
    global Bookshop_img
    global name_entry
    global contact_entry
    global address_entry
    # main window
    
    root=Toplevel()
    
    # changing the colour of main window
    root.configure(bg="orange")

    # Geometry or dimensions of root Window
    root.geometry('800x680')
    # Displaying Icon
    root.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
    # Create Image Widget
    Bookshop_img=ImageTk.PhotoImage((Image.open("D:\Project_1\Images_Icons\Bookshop_img.png")).resize((320,300)))
    
     # title
    root.title("Customer_Window | BOOKSHOP AUTOMATION SYSTEM")
   
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
    customer_label=Label(root,text="Customer Details",relief=SUNKEN,bg='violet',padx=30,pady=5,borderwidth=5)
    customer_label.place(x=5,y=420)
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
    enter_button1.place(x=250,y=600)
    exit_button1=Button(root, text="BACK",bd=10, padx=40, pady=10, bg="green",command=lambda: backy(root,rootaccess))
    exit_button1.place(x=450,y=600)
    
    


def customer_entry():
    global name_entry
    global contact_entry
    global address_entry
    name=name_entry.get()
    date_time=date.today()
    sql_query="INSERT INTO customer_details(full_name,contact_number,address,time_date) values(%s,%s,%s,%s);"
    cursor.execute(sql_query,(name,contact_entry.get(),address_entry.get(),date_time))
    print("customer details inserted")
    
    
def enter_button():
    global name_entry
    global contact_entry
    global address_entry

    res = (any((ord(ele)>=65 and ord(ele)<=90) or (ord(ele)>=97 and ord(ele)<=122) for ele in contact_entry.get()))

    if(len(name_entry.get())<7):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Name should be of 7 characters ")
        if(prompt_reply==True):
            
            name_entry.delete(0, END) 
        else:
            root.destroy()
        
    elif(len(contact_entry.get())!=10):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Contact Number should be of 10 characters ")
        if(prompt_reply==True):
            contact_entry.delete(0,END) 
        else:
            root.destroy()
    elif(res==True):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Only Numbers/Digits")
        if(prompt_reply==True):
            contact_entry.delete(0,END) 
        else:
            root.destroy()
    
    elif(len(address_entry.get())<10):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Address should be more than 10 characters")
        if(prompt_reply==True):
            address_entry.delete(0, END) 
        else:
            root.destroy()
    
        
    else:
        customer_entry()

        books()
        
def customer():
    customer_window()

def books():
    global author_or_book_entry
    #global checkout_frame
    global books_frame
    global root1
    global root
    root.withdraw()
    #root.destroy()
    root1=Toplevel()
    root1.geometry('800x680')
    root1.title("Books Window | BOOKSHOP AUTOMATION SYSTEM")
    # colour
    root1.configure(bg="orange")
    root1.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')

    text_label=Label(root1,text="VS Book Store",font=('Helvatical bold',50),relief=SUNKEN,bg='ivory3',padx=70)
    text_label.grid(row=0,column=0,columnspan=4,sticky=W+E,padx=30)

    author_book_label=Label(root1, text="Enter title or author name ",relief=SUNKEN,font=('Helvatical bold',17),anchor=CENTER,borderwidth=12)
    author_book_label.grid(row=1,column=0,padx=150,sticky=W+E,pady=10)

    author_or_book_entry=Entry(root1,width=90, borderwidth=2)
    author_or_book_entry.grid(row=2,column=0,padx=100)

    

    author_button=Button(root1, text="Search by AUTHOR NAME",relief=SUNKEN,bg="green",padx=10,pady=5,borderwidth=10,command=search_author)
    author_button.place(x=60,y=180)
    bookname_button=Button(root1, text="Search by BOOK NAME",relief=SUNKEN,bg="green",padx=17,pady=4,borderwidth=10,command=search_book)
    bookname_button.place(x=295,y=180)

    books_label=Label(root1,text="Books List",padx=40,font=("Helvetica",14),bg="violet",relief=SUNKEN,borderwidth=5)
    books_label.place(x=0,y=235)

    books_frame=Frame(root1,padx=5,pady=5,bg="coral")
    books_frame.place(x=0,y=270,height=360,width=800)

    
    #v.configure(command=books_frame.yview)


    clear_label=Button(root1,text="Clear Results",padx=9,pady=10,font=("Helvetica",14),bg="lightgreen",relief=SUNKEN,borderwidth=5,command=clear_func1)
    clear_label.place(x=80,y=630)

    Logout_button=Button(root1,text=" Back ",relief=SUNKEN,bg="red",command=lambda: backy(root1,root), anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",14)),borderwidth=5)
    Logout_button.place(x=330,y=630)
    
    

    
    request_button=Button(root1,text="Request for book",bg="green",relief=SUNKEN,padx=25,pady=5,borderwidth=10,command=Request_func)
    request_button.place(x=530,y=180)

    cart_label=Button(root1,text=" Show Cart ",padx=12,pady=10,font=("Helvetica",14),bg="green",relief=SUNKEN,borderwidth=5,command=cart_win)
    cart_label.place(x=580,y=630)
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
           
    #checkout_button=Button(root1, text="Proceed to checkout",relief=SUNKEN,bg="green",padx=10,pady=5,borderwidth=5,command=search_author)
    #checkout_button.place(x=80,y=630)


def search_author():
    global author_or_book_entry
    global books_frame
    global books_details1

    reading_gif()
    clear_func1()
    
    query="SELECT author_name FROM inventory;"
    cursor.execute(query)
    author_list=cursor.fetchall()

    list_len=len(author_list)
    result_title=""
    is_found=False
    books_details1=[]
    if(author_or_book_entry.get()):
        for book1 in author_list:
            if (author_or_book_entry.get().lower() in book1[0].lower() and (book1!=author_list[list_len-1])):
                is_found=True
                result_title=book1[0]
                sql_query="SELECT * FROM inventory WHERE author_name=(%s)"
                cursor.execute(sql_query,(result_title,))
                book_details=cursor.fetchall()

                books_details1+=book_details
            elif(author_or_book_entry.get().lower() in book1[0].lower() and (book1==author_list[list_len-1])):
                is_found=True
                result_title=book1[0]
                sql_query="SELECT * FROM inventory WHERE author_name=(%s)"
                cursor.execute(sql_query,(result_title,))
                book_details=cursor.fetchall()
                books_details1+=book_details
                break
            elif(book1==author_list[list_len-1]):
                break

    
        else:
            not_found_label1=Label(books_frame,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
            not_found_label1.place(x=250,y=100)
    else:
        not_found_label1=Label(books_frame,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
        not_found_label1.place(x=250,y=100)
    

    if(is_found):
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
            button_dict=Button(books_frame,text=" BUY ",font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=5,bg="green",command=add_to_cart)
            button_dict.place(x=692,y=60+size)
        
            size+=55
    
    v=Scrollbar(books_frame,orient=VERTICAL)
    v.pack(side=RIGHT, fill=Y)
    
def search_book():
    
    global author_or_book_entry
    
    global books_frame
    global gif_display
    global books_details
    
    
    reading_gif()
    clear_func1()
    
    query="SELECT title FROM inventory"

    cursor.execute(query)
    book_list=cursor.fetchall()
    list_len=len(book_list)
    print(book_list)
    
    books_details=[]
    result_title=""
    is_found=False
    if(author_or_book_entry.get()):
        for book1 in book_list:
            if (author_or_book_entry.get().lower() in book1[0].lower() and (book1!=book_list[list_len-1])):
                is_found=True
                result_title=book1[0]
                sql_query="SELECT * FROM inventory WHERE title=(%s)"
                cursor.execute(sql_query,(result_title,))
                book_details=cursor.fetchall()
                books_details+=book_details
                print(books_details)
            elif(author_or_book_entry.get().lower() in book1[0].lower() and (book1==book_list[list_len-1])):
                is_found=True
                result_title=book1[0]
                sql_query="SELECT * FROM inventory WHERE author_name=(%s)"
                cursor.execute(sql_query,(result_title,))
                book_details=cursor.fetchall()
                books_details+=book_details
                break
            elif(book1==book_list[list_len-1]):
                break
        else:
            not_found_label1=Label(books_frame,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
            not_found_label1.place(x=250,y=100)
    else:
        not_found_label1=Label(books_frame,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
        not_found_label1.place(x=250,y=100)
        
    if(is_found):  
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
            
            buy_button1=Button(books_frame,text=" BUY ",font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=5,bg="green",command=add_to_cart)
            buy_button1.place(x=692,y=60+size)

        
            size+=55
    else:
        not_found_label1=Label(books_frame,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
        not_found_label1.place(x=250,y=100)
    
    v=Scrollbar(books_frame,orient=VERTICAL)
    v.pack(side=RIGHT, fill=Y)
def add_to_cart():
    global root
    cust_name=name_entry.get()
    
    # take isbn as input from customer

    isbn=simpledialog.askstring("Input","Enter ISBN Number including hyphens(-)")
    is_isbn=True
    while(is_isbn):
        if(isbn=="" or isbn==None or len(isbn)!=17):
            prompt_reply=messagebox.askretrycancel("Retry"," Wrong Input \nClick Retry to enter again or cancel to exit")
            
            if(prompt_reply==True):
                is_isbn=True
                isbn=simpledialog.askstring("Input","Enter ISBN Number including hyphens(-)")
            else:
                is_isbn=False
                messagebox.showinfo("clear prompt", "Click ok to quit prompt")
        else:
            is_isbn=False       
            
            sql_query1="SELECT ISBN,title,author_name,rack_number, sell_price from inventory where ISBN=(%s);"
            cursor.execute(sql_query1,(isbn,))
            cart_list=cursor.fetchall()
            print(cart_list)
            date_time=datetime.now()
            now1=date_time.strftime('%Y-%M-%D %H:%M:%S')
            books_quantity=simpledialog.askinteger("Input","Enter the number of books on your selection of purchase!")
            sql_query2="INSERT INTO cart(time_date,customer_name,isbn_no,title,author,no_of_books,sell_price,rack_number) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
            
            for item in cart_list:
                cursor.execute(sql_query2,(now1,cust_name,item[0],item[1],item[2],books_quantity,item[4],item[3]))
                messagebox.showinfo("Info","Added item(s) to cart")
                print("added to cart")
def request_field_insert():
    global customer_name_entry
    global contact_no_entry
    global book_title_entry
    global author_name_entry
    global request_win
    global author_or_book_entry
    global root1
    customer_name=customer_name_entry.get().title()
    contact_no=contact_no_entry.get()
    book_title=book_title_entry.get().title()
    author_name=author_name_entry.get().title()
   
    date_time=datetime.now()
    now1=date_time.strftime('%Y-%M-%D %H:%M:%S')
    
    sql_query="INSERT INTO request_field(date_time, customer_name, contact_number,book_title, book_author) values(%s,%s,%s,%s,%s)"
    cursor.execute(sql_query,(now1,
                              customer_name,contact_no,book_title,author_name))
    reply=messagebox.askyesno("Info!","Thanks for helping us:) Would you like to request for another book? if yes click on 'YES' or else 'NO'")
    if(reply==True):
        customer_name_entry.delete(0,END)
        contact_no_entry.delete(0,END)
        book_title_entry.delete(0,END)
        author_name_entry.delete(0,END)
    else:
        reply=messagebox.askretrycancel('Search for book',"if you want to search for another book, \nClick on'Retry' or else click cancel to Exit.")
        if(reply==True):
            request_win.destroy()
            author_or_book_entry.delete(0,END)
        else:
            request_win.destroy()
            root1.destroy()

def request_field():
    global customer_name_entry
    global contact_no_entry
    global book_title_entry
    global author_name_entry
    global request_win
    global author_or_book_entry
    global root1

    res = (any((ord(ele)>=65 and ord(ele)<=90) or (ord(ele)>=97 and ord(ele)<=122) for ele in contact_no_entry.get()))

    if(len(customer_name_entry.get())<7):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Name should be of 7 characters ")
        if(prompt_reply==True):
            
            customer_name_entry.delete(0,END)
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                request_win.destroy()
            else:
                customer_name_entry.delete(0,END)
        
    elif(len(contact_no_entry.get())!=10):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Contact Number should be of 10 characters ")
        if(prompt_reply==True):
            contact_no_entry.delete(0,END) 
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                request_win.destroy()
            else:
                contact_no_entry.delete(0,END)
    elif(res==True):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Only Numbers/Digits")
        if(prompt_reply==True):
            contact_no_entry.delete(0,END) 
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                request_win.destroy()
            else:
                contact_no_entry.delete(0,END)
    
    elif(len(book_title_entry.get())<5):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Address should be more than 5 characters")
        if(prompt_reply==True):
            book_title_entry.delete(0, END) 
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                request_win.destroy()
            else:
                book_title_entry.delete(0, END)
    elif(len(author_name_entry.get())<5):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Address should be more than 5 characters")
        if(prompt_reply==True):
            (author_name_entry.delete(0, END) )
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                request_win.destroy()
            else:
                author_name_entry.delete(0, END) 
            
    else:
        request_field_insert()

def Request_func():
    global customer_name_entry
    global contact_no_entry
    global book_title_entry
    global author_name_entry
    global root1
    root1.withdraw()
    global request_win
    '''
    if(root):
        root.destroy()
    else:
        pass
    
    '''
    request_win=Toplevel()
    request_win.configure(bg="orange")
    request_win.geometry('600x500')
    request_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
    request_field_label=Label(request_win,text="Enter details fro procurement",bg='violet',padx=20,relief=SUNKEN,borderwidth=5)
    request_field_label.place(x=5,y=120)

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
    Logout_button=Button(request_win,text=" Back ",relief=SUNKEN,bg="red",command=lambda: backy(request_win,root1), anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",14)),borderwidth=5)
    Logout_button.place(x=227,y=440)
def cart_win():
    global cart_window
    global root1
    root1.withdraw()
    cart_window=Toplevel()
    cart_window.title("Cart")
    cart_window.configure(bg="orange")

    #checkout_frame=Frame(root1,padx=5,pady=5,bg="coral")
    #checkout_frame.place(x=0,y=280,height=350,width=280)

    # Geometry or dimensions of root Window
    cart_window.geometry('800x680')
    # Displaying Icon
    cart_window.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
    books_frame1=Frame(cart_window,padx=5,pady=5,bg="coral")
    books_frame1.place(x=50,y=290,height=350,width=700)
    
    cart_label=ISBN_label=Label(cart_window,text="CART",font=("Helvetica",12),relief=SUNKEN,borderwidth=5,padx=47,anchor=CENTER,bg="lightgreen")
    cart_label.place(x=320,y=257)

    ISBN_label=Label(books_frame1,text="ISBN",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=47,anchor=CENTER,bg="violet")
    ISBN_label.place(x=5,y=5)
    title_author_label=Label(books_frame1,text="Title | Author",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=50,bg="violet")
    title_author_label.place(x=145,y=5)
    quantity_label=Label(books_frame1,text="N_Books",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=8,bg="violet")
    quantity_label.place(x=360,y=5)
    Rack_label=Label(books_frame1,text="Rack No",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=12,bg="violet")
    Rack_label.place(x=580,y=5)
    price_label=Label(books_frame1,text="Price",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=32,bg="violet")
    price_label.place(x=460,y=5)
    #buy_label=Label(books_frame1,text="Add to cart",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=5,bg="violet")
    #buy_label.place(x=675,y=5)

    query="SELECT isbn_no,title,author,no_of_books,sell_price,rack_number FROM cart;"
    cursor.execute(query)
    cart_list=cursor.fetchall()
    size=0
    if(len(cart_list)!=0):
        for item in cart_list:
            ISBN_label1=Label(books_frame1,text=item[0],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,anchor=CENTER,bg="coral")
            ISBN_label1.place(x=12,y=60+size)
            title_author_label1=Label(books_frame1,text=f"{item[1]}\n{item[2]}",font=("Helvetica",9),bg="coral")
            title_author_label1.place(x=165,y=60+size)
            quantity_label1=Label(books_frame1,text=item[3],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=4,bg="coral")
            quantity_label1.place(x=385,y=60+size)
            price_label1=Label(books_frame1,text=item[4],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=15,bg="coral")
            price_label1.place(x=475,y=60+size)
            Rack_label1=Label(books_frame1,text=item[5],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=12,bg="coral")
            Rack_label1.place(x=600,y=60+size) 
                
                    #buy_button1=Button(books_frame1,text=" BUY ",font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=5,bg="green",command=lambda: add_to_cart(book[0],book[1],book[2],book[6]))
                    #buy_button1.place(x=692,y=60+size)
            size+=55
    else:
        not_found_label1=Label(books_frame1,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
        not_found_label1.place(x=200,y=150)

    back_button=Button(cart_window,text=" Back ",font=("Helvetica",9),relief=SUNKEN,borderwidth=5,padx=50,bg="green",command=lambda: backy(cart_window,root1))
    back_button.place(x=200,y=647)
    proceed_button=Button(cart_window,text=" PROCEED TO BUY ",font=("Helvetica",9),relief=SUNKEN,borderwidth=5,padx=5,bg="green",command=Checkout)
    proceed_button.place(x=500,y=647)
   
    cart_image()
    

def clear_func1():
    global books_frame
    
    for widget in books_frame.winfo_children():
        widget.destroy()
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




def Checkout():
    VS_access("Sales Clerk")

def insert_statistics():
    global total_amount
    global name_entry
    global contact_entry
    global address_entry
    date_time=date.today()

    
    sql_query="SELECT customer_name,no_of_books from cart;"

    cursor.execute(sql_query)
    stats_list=cursor.fetchall()
    print(stats_list)
    if(len(stats_list)>0):
        print("stats updating")
        for stats in stats_list:
            sql_query1="INSERT INTO sales_statistics values(%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql_query1,(date_time,stats[0],contact_entry.get(),address_entry.get(),stats[1],total_amount))

    
    print("stats updated")
    update_inventory()

def update_inventory():
    query="SELECT isbn_no,no_of_books FROM cart;"
    cursor.execute(query)
    inv_list=cursor.fetchall()
    if(len(inv_list)!=0):
        print("updating inventory")
        for item in inv_list:
            sql_query="UPDATE INVENTORY SET quantity=quantity-(%s) where isbn=(%s);"
            cursor.execute(sql_query,(item[1],item[0]))
            print("updating.....")
        else:
            messagebox.showinfo("Info","Updated")

    print("Updated after purchase")
    # delete those with 0 quantity
    sql_query2="DELETE FROM INVENTORY where quantity=0;"
    cursor.execute(sql_query2)
    
def payment():
    global total_amount
    global print_button

    print_button.configure(state=ACTIVE)

    print_button.configure(state=ACTIVE)
    sql_query="SELECT no_of_books,sell_price FROM cart;"

    cursor.execute(sql_query)
    payment_list=cursor.fetchall()
    total_amount=0
    for amount in payment_list:
        total_amount+=amount[0]*amount[1]
    
    is_paid=False
    while(not is_paid):
        prompt_reply=messagebox.askyesnocancel("Pay?","Click 'YES' if paid or 'NO' if unpaid or 'Cancel' if unsure")
        if(prompt_reply==True):
            is_paid=True
            insert_statistics()
        elif(prompt_reply==False):
            messagebox.showwarning("Pay?","Ask customer to Pay to proceed further")
            is_paid=False

        elif(prompt_reply==None):
            messagebox.showwarning("Pay?","Are you sure? Click OK to exit")
            is_paid=False


def checkout_win():
    global sales_win
    global print_button

    cart_frame=Frame(sales_win,padx=10,pady=10,bg="Ivory3")
    cart_frame.place(x=50,y=150,height=400,width=700)
    
    ISBN_label=Label(cart_frame,text="ISBN",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=47,anchor=CENTER,bg="violet")
    ISBN_label.place(x=5,y=5)
    title_author_label=Label(cart_frame,text="Title | Author",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=65,bg="violet")
    title_author_label.place(x=143,y=5)
    quantity_label=Label(cart_frame,text="N_Books",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=8,bg="violet")
    quantity_label.place(x=360,y=5)
    Rack_label=Label(cart_frame,text="Rack No",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=12,bg="violet")
    Rack_label.place(x=580,y=5)
    price_label=Label(cart_frame,text="Price",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=32,bg="violet")
    price_label.place(x=460,y=5)
    #buy_label=Label(books_frame1,text="Add to cart",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=5,bg="violet")
    #buy_label.place(x=675,y=5)

    query="SELECT isbn_no,title,author,no_of_books,sell_price,rack_number FROM cart;"
    cursor.execute(query)
    cart_list=cursor.fetchall()
    size=0
    if(len(cart_list)!=0):
        proceed_but=Button(sales_win,text="Confirm",font=("Helvetica",12),relief=SUNKEN,borderwidth=5,padx=5,bg='green',command=payment)
        proceed_but.place(x=380,y=575)

        for item in cart_list:
            ISBN_label1=Label(cart_frame,text=item[0],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,anchor=CENTER,bg="Ivory3")
            ISBN_label1.place(x=12,y=60+size)
            title_author_label1=Label(cart_frame,text=f"{item[1]}\n{item[2]}",font=("Helvetica",9),bg="Ivory3")
            title_author_label1.place(x=152,y=60+size)
            quantity_label1=Label(cart_frame,text=item[3],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=4,bg="Ivory3")
            quantity_label1.place(x=385,y=60+size)
            price_label1=Label(cart_frame,text=item[4],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=15,bg="Ivory3")
            price_label1.place(x=475,y=60+size)
            Rack_label1=Label(cart_frame,text=item[5],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=12,bg="Ivory3")
            Rack_label1.place(x=600,y=60+size)
            #buy_button1=Button(books_frame1,text=" BUY ",font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=5,bg="green",command=lambda: add_to_cart(book[0],book[1],book[2],book[6]))
            #buy_button1.place(x=692,y=60+size)
            size+=55
    else:
        not_found_label1=Label(cart_frame,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
        not_found_label1.place(x=200,y=150)
    
def message():
    global Invoice_win
    global sales_win
    global gif_display
    global cart_window
    global root
    global root1
    messagebox.showinfo("Info","Purchase Completed:)")
    #clear_cart()
    Invoice_win.destroy()
    sales_win.destroy()
    cart_window.destroy()
    root1.destroy()
    root.destroy()
    
    


def Invoice():
    global Invoice_win
    global total_amount
    Invoice_win=Toplevel()
    Invoice_win.configure(bg="ivory3")
    # Geometry or dimensions of root Window
    Invoice_win.geometry('800x680')
    # Displaying Icon
    Invoice_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    Invoice_win.title("Invoice | BOOKSHOP AUTOMATION SYSTEM")

    invoice_frame=Frame(Invoice_win,bg="white",borderwidth=2,relief=SUNKEN)
    invoice_frame.place(x=150,y=5,height=650,width=450)
    invoice_frame.configure(bg="white")
    #store_text=Text(invoice_frame,)
    
    invoice_no=0
    store_text=f'''
                VS BOOKSTORE
            New Version of Bookshop

 -------------------------------------------------------------------

        Invoice Number     :   {invoice_no}

 -------------------------------------------------------------------
        '''
    
    reciept_label=Label(invoice_frame,text=store_text,bg="white")
    reciept_label.pack()
    sql_query="SELECT customer_name,title,isbn_no,no_of_books,sell_price from cart ;"
    cursor.execute(sql_query)
    reciept_list=cursor.fetchall()

    customer_label=Label(invoice_frame,text=f"Name: {reciept_list[0][0]}\t\t\t",bg="white")
    customer_label.pack()

    design_text="----------------------------------------------------------------"
    design_label=Label(invoice_frame,text=design_text,bg="white")
    design_label.pack()
    heading_label=Label(invoice_frame,text="\n book_name\t\t  ISBN\t\tQty\tPrice\n",bg="white")
    heading_label.pack()
    design_label=Label(invoice_frame,text=design_text,bg="white")
    design_label.pack()
    
    
    for item in reciept_list:
        customer_name=item[0]
        book_name=item[1]
        ISBN=item[2]
        Qty=item[3]
        Price=item[4]
        
        books_label=Label(invoice_frame,text=f" {book_name} {ISBN}  {Qty}   {Price}\n",bg="white")
        books_label.pack()
        design_label=Label(invoice_frame,text=design_text,bg="white")
        design_label.pack()

    total_label=Label(invoice_frame,text=f"\t\t\t\tTotal Amount:\t{total_amount}",bg="white")
    total_label.pack()
    paid_label=Label(invoice_frame,text="Paid:)",bg="white",font=("Times New Roman",12,'bold'))
    paid_label.pack()
    thanks_label=Label(invoice_frame,text="Thanks, Visit again:)",bg="white",font=("Times New Roman",12,'bold'))
    thanks_label.place(x=150,y=520)
    print_button=Button(Invoice_win,text="Confirm", relief=SUNKEN,borderwidth=7,pady=5,padx=5,font=("Helvetica",14),bg="green",command=message)
    print_button.place(x=650,y=600)

def sales_window():
    
    global sales_win
    global print_button
    global VS_root
    VS_root.withdraw
    sales_win=Toplevel()
    # changing the colour of main window
    sales_win.configure(bg="orange")
    # Geometry or dimensions of root Window
    sales_win.geometry('800x680')
    # Displaying Icon
    sales_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    sales_win.title(" Sales Clerk | BOOKSHOP AUTOMATION SYSTEM")
    
    items_list_button=Button(sales_win,text="Checkout List", relief=SUNKEN,padx=20,pady=10,font=("Helvetica",14),bg="lightgreen",command=checkout_win)
    items_list_button.place(x=180,y=50)

    print_button=Button(sales_win,text="Print Reciept", relief=SUNKEN,padx=20,pady=10,font=("Helvetica",14),bg="lightgreen",command=Invoice,state=DISABLED)
    print_button.place(x=500,y=50)

    Logout_button=Button(sales_win,text=" Back ",relief=SUNKEN,bg="red",command=lambda: backy(sales_win,VS_root), anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",15)),borderwidth=5)
    Logout_button.place(x=350,y=620)
def insert_stock():
    global stockist_name_emp
    global contact_no_stockist_emp
    global book_title_emp
    global author_name_emp
    global isbn_emp
    global published_year_emp
    global quantity_emp
    global rack_number_emp
    global price_emp

    sql_query="INSERT INTO inventory values(%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(sql_query,(isbn_emp.get(),book_title_emp.get(),author_name_emp.get(),published_year_emp.get(),quantity_emp.get(),rack_number_emp.get(),price_emp.get()))

    sql_query1="INSERT INTO stockist_details values(%s,%s,%s,%s,%s);"
    cursor.execute(sql_query1,(stockist_name_emp.get(),contact_no_stockist_emp.get(),book_title_emp.get(),author_name_emp.get(),quantity_emp.get()))
    messagebox.showinfo("Info","Updated:)")

def update_details_check():
    global employee_win
    global stockist_name_emp
    global contact_no_stockist_emp
    global book_title_emp
    global author_name_emp
    global isbn_emp
    global published_year_emp
    global quantity_emp
    global rack_number_emp
    res = (any((ord(ele)>=65 and ord(ele)<=90) or (ord(ele)>=97 and ord(ele)<=122) for ele in contact_no_stockist_emp.get()))
    if(len(stockist_name_emp.get())<7):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Name should be of 7 characters ")
        if(prompt_reply==True):
            stockist_name_emp.delete(0,END)
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                stockist_name_emp.delete(0,END)
            
    elif(len(contact_no_stockist_emp.get())!=10):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Contact Number should be of 10 characters ")
        if(prompt_reply==True):
            contact_no_stockist_emp.delete(0,END) 
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                contact_no_stockist_emp.delete(0,END)
    elif(res==True):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Only Numbers/Digits")
        if(prompt_reply==True):
            contact_no_stockist_emp.delete(0,END) 
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                contact_no_stockist_emp.delete(0,END)
        
    elif(len(book_title_emp.get())<5):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Address should be more than 5 characters")
        if(prompt_reply==True):
            book_title_emp.delete(0, END) 
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                book_title_emp.delete(0, END)
    elif(len(author_name_emp.get())<5):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Address should be more than 5 characters")
        if(prompt_reply==True):
            (author_name_emp.delete(0, END) )
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                author_name_emp.delete(0, END) 
    elif(not(len(isbn_emp.get())==17 )):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: isbn should be of 17 characters with hyphens ")
        if(prompt_reply==True):
            isbn_emp.delete(0,END)
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                isbn_emp.delete(0,END)
    
    elif(not(len(published_year_emp.get())==4)):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: published year should be of 4 characters ")
        if(prompt_reply==True):
            published_year_emp.delete(0,END)
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                published_year_emp.delete(0,END)
    elif((not(len(quantity_emp.get())>0 )) and not((ord(quantity_emp.get())<=48 and ord(quantity_emp.get())>=57))):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint:Only integers")
        if(prompt_reply==True):
            quantity_emp.delete(0,END)
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                quantity_emp.delete(0,END)
    elif((not(len(rack_number_emp.get())>0 )) and not ((ord(rack_number_emp.get())<=48 and ord(rack_number_emp.get())>=57))):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: rack number should be of atleast 1 character ")
        if(prompt_reply==True):
            rack_number_emp.delete(0,END)
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                rack_number_emp.delete(0,END)
    elif((not(len(price_emp.get())>0 )) or not ((ord(price_emp.get())<=48 and ord(price_emp.get())>=57))):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: price should be of atleast 1 character")
        if(prompt_reply==True):
            price_emp.delete(0,END)
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                employee_win.destroy()
            else:
                price_emp.delete(0,END)
            
            
    else:
        insert_stock()  

def employee_work():
    global employee_win
    global stockist_name_emp
    global contact_no_stockist_emp
    global book_title_emp
    global author_name_emp
    global isbn_emp
    global published_year_emp
    global quantity_emp
    global rack_number_emp
    global price_emp
    stockist_name=Label(employee_win,text=" Stockist Name",relief=SUNKEN,padx=4,pady=5)
    stockist_name.place(x=5,y=150)
    contact_no_stockist=Label(employee_win,text="Contact",relief=SUNKEN,padx=23,pady=5)
    contact_no_stockist.place(x=5,y=190)
    book_title=Label(employee_win,text="Book Title",relief=SUNKEN,padx=18,pady=5)
    book_title.place(x=5,y=230)
    author_name=Label(employee_win,text="Author",relief=SUNKEN,padx=25,pady=5)
    author_name.place(x=5,y=270)
    isbn=Label(employee_win,text="ISBN",relief=SUNKEN,padx=31,pady=5)
    isbn.place(x=5,y=310)
    published_year=Label(employee_win,text="Published year",relief=SUNKEN,padx=5,pady=5)
    published_year.place(x=5,y=350)
    quantity=Label(employee_win,text="quantity",relief=SUNKEN,padx=22,pady=5)
    quantity.place(x=5,y=390)
    rack_number=Label(employee_win,text="rack number",relief=SUNKEN,padx=10,pady=5)
    rack_number.place(x=5,y=430)
    price=Label(employee_win,text="price",relief=SUNKEN,padx=32,pady=5)
    price.place(x=5,y=470)
   

    
    stockist_name_emp=Entry(employee_win,width=80,borderwidth=5)
    stockist_name_emp.place(x=110,y=150)
    contact_no_stockist_emp=Entry(employee_win,width=80,borderwidth=5)
    contact_no_stockist_emp.place(x=110,y=190)
    book_title_emp=Entry(employee_win,width=80,borderwidth=5)
    book_title_emp.place(x=110,y=230)
    author_name_emp=Entry(employee_win,width=80,borderwidth=5)
    author_name_emp.place(x=110,y=270)
    isbn_emp=Entry(employee_win,width=80,borderwidth=5)
    isbn_emp.place(x=110,y=310)
    published_year_emp=Entry(employee_win,width=80,borderwidth=5)
    published_year_emp.place(x=110,y=350)
    quantity_emp=Entry(employee_win,width=80,borderwidth=5)
    quantity_emp.place(x=110,y=390)
    rack_number_emp=Entry(employee_win,width=80,borderwidth=5)
    rack_number_emp.place(x=110,y=430)
    price_emp=Entry(employee_win,width=80,borderwidth=5)
    price_emp.place(x=110,y=470)

    
    insert_button=Button(employee_win,text="Submit",relief=SUNKEN,padx=15,pady=8,bd=5,bg="green",command=update_details_check)
    insert_button.place(x=270,y=520)
    

def employee_window():
    global employee_win
    global VS_root
    VS_root.withdraw()
    employee_win=Toplevel()
    # changing the colour of main window
    employee_win.configure(bg="orange")

    # Geometry or dimensions of root Window
    employee_win.geometry('650x750')
    # Displaying Icon
    employee_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    employee_win.title("Employee | BOOKSHOP AUTOMATION SYSTEM")
    update_label=Button(employee_win,text="Update Stock",relief=SUNKEN,padx=40,pady=5,borderwidth=2,bg="Violet",command=employee_work)
    update_label.place(x=230,y=90)
    Logout_button=Button(employee_win,text=" Back ",relief=SUNKEN,bg="red",command=lambda: backy(employee_win,VS_root), anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",15)),borderwidth=5)
    Logout_button.place(x=250,y=680)

    return
    
def manager_view():
    global manager_win
    global VS_root
    
    request_field_frame=Frame(manager_win,padx=10,pady=10,bg='Ivory3')
    request_field_frame.place(x=30,y=80,height=400,width=730)
    
    
    customer_name_label=Label(request_field_frame,text="customer name",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=25,anchor=CENTER,bg="violet")
    customer_name_label.place(x=20,y=5)
    title_label=Label(request_field_frame,text="Title ",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=60,bg="violet")
    title_label.place(x=190,y=5)
    author_label=Label(request_field_frame,text="Author",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=60,bg="violet")
    author_label.place(x=370,y=5)
    contact_label=Label(request_field_frame,text="Contact Number",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=15,bg="violet")
    contact_label.place(x=545,y=5)
    #price_label=Label(request_field_frame,text="Price",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=32,bg="violet")
    #price_label.place(x=460,y=5)
    #buy_label=Label(books_frame1,text="Add to cart",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=5,bg="violet")
    #buy_label.place(x=675,y=5)

    query="SELECT customer_name,book_title,book_author,contact_number FROM request_field;"
    cursor.execute(query)
    request_list=cursor.fetchall()
    size=0
    if(request_list):
        for item in request_list:
            customer_name_label1=Label(request_field_frame,text=item[0],font=("Helvetica",9,"bold"),anchor=CENTER,bg="ivory3")
            customer_name_label1.place(x=30,y=60+size)
            title_label1=Label(request_field_frame,text=f"{item[1]}",font=("Helvetica",9,"bold"),padx=2,bg="ivory3")
            title_label1.place(x=200,y=60+size)
            author_label1=Label(request_field_frame,text=item[2],font=("Helvetica",9,"bold"),padx=4,bg="ivory3")
            author_label1.place(x=385,y=60+size)
            contact_label=Label(request_field_frame,text=item[3],font=("Helvetica",9,"bold"),padx=15,bg="ivory3")
            contact_label.place(x=555,y=60+size)
            #Rack_label1=Label(request_field_frame,text=item[5],font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=12,bg="coral")
            #Rack_label1.place(x=600,y=60+size) 
            
                #buy_button1=Button(books_frame1,text=" BUY ",font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=5,bg="green",command=lambda: add_to_cart(book[0],book[1],book[2],book[6]))
                #buy_button1.place(x=692,y=60+size)
            size+=55
    else:
        not_found_label1=Label(request_field_frame,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
        not_found_label1.place(x=250,y=100)
    Logout_button=Button(manager_win,text=" Back ",relief=SUNKEN,bg="red",command=lambda: backy(manager_win,VS_root), anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",15)),borderwidth=5)
    Logout_button.place(x=350,y=620)
    
def manager_window():
    global manager_win
    global VS_root
    VS_root.withdraw()
    manager_win=Toplevel()
    # changing the colour of main window
    manager_win.configure(bg="orange")


    # Geometry or dimensions of root Window
    manager_win.geometry('800x680')
    # Displaying Icon
    manager_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    manager_win.title("Manager | BOOKSHOP AUTOMATION SYSTEM")

    request_field_button=Button(manager_win,text="View Request Field",relief=SUNKEN,bg="green",padx=5,pady=5,borderwidth=5,command=manager_view)
    request_field_button.place(x=350,y=20)


def statistics1():
    global owner_win
    sql_query="SELECT date_time,full_name,quantity,amount from sales_statistics;"
    cursor.execute(sql_query)
    stats_list1=cursor.fetchall()

    revenue=0
    for stat in stats_list1:
        revenue+=stat[3]
    
    print(stats_list1)
    now=(date.today())
    books_qty=0
    for stats in stats_list1:
        sql_query1="SELECT DATEDIFF(%s,%s)+1;"
        cursor.execute(sql_query1,(now,stats[0]))
        res=cursor.fetchone()
        print(res)
        books_qty+=stats[2]
        if(res[0]<15):
            inv_level=2*books_qty
            inventory_label=Label(owner_win,text="Inventory Level Required is:" +f"{inv_level}",relief=SUNKEN,padx=5,pady=7,bg="ivory3")
            inventory_label.place(x=310,y=110)
            break
    
    threshold_frame=Frame(owner_win,padx=10,pady=10,bg="Ivory3")
    threshold_frame.place(x=50,y=170,height=400,width=700)
    
    ISBN_label=Label(threshold_frame,text="ISBN",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=47,anchor=CENTER,bg="violet")
    ISBN_label.place(x=5,y=5)
    title_label=Label(threshold_frame,text="Title",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=80,bg="violet")
    title_label.place(x=145,y=5)
    quantity_label=Label(threshold_frame,text="N_Books",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=8,bg="violet")
    quantity_label.place(x=500,y=5)
    author_label=Label(threshold_frame,text="Author",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=60,bg="violet")
    author_label.place(x=335,y=5)
    price_label=Label(threshold_frame,text="Price",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=32,bg="violet")
    price_label.place(x=580,y=5)
    #buy_label=Label(books_frame1,text="Add to cart",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=5,bg="violet")
    #buy_label.place(x=675,y=5)

    query="SELECT ISBN,title,author_name,quantity,sell_price FROM inventory where quantity<(%s);"
    cursor.execute(query,(inv_level,))
    threshold_list=cursor.fetchall()
    size=0
    if(len(threshold_list)!=0):
        for item in threshold_list:
            ISBN_label1=Label(threshold_frame,text=item[0],font=("Helvetica",9),borderwidth=3,anchor=CENTER,bg="Ivory3")
            ISBN_label1.place(x=12,y=60+size)
            title_label1=Label(threshold_frame,text=f"{item[1]}",font=("Helvetica",9),borderwidth=3,bg="Ivory3")
            title_label1.place(x=152,y=60+size)
            quantity_label1=Label(threshold_frame,text=item[3],font=("Helvetica",9),borderwidth=3,padx=4,bg="Ivory3")
            quantity_label1.place(x=520,y=60+size)
            price_label1=Label(threshold_frame,text=item[4],font=("Helvetica",9),borderwidth=3,padx=15,bg="Ivory3")
            price_label1.place(x=600,y=60+size)
            author_label1=Label(threshold_frame,text=item[2],font=("Helvetica",9),borderwidth=3,bg="Ivory3")
            author_label1.place(x=345,y=60+size)
            #buy_button1=Button(books_frame1,text=" BUY ",font=("Helvetica",9),relief=SUNKEN,borderwidth=3,padx=5,bg="green",command=lambda: add_to_cart(book[0],book[1],book[2],book[6]))
            #buy_button1.place(x=692,y=60+size)
            size+=55
    else:
        not_found_label1=Label(threshold_frame,text="No books below threshold",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
        not_found_label1.place(x=200,y=250)
         
            

    revenue_label=Label(owner_win,text="Revenue: "+f"{revenue}",font=("Helvetica",14),relief=SUNKEN,borderwidth=3,padx=25,bg="violet")
    revenue_label.place(x=600,y=630)
    #not_found_label1=Label(request_field_frame,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
    #not_found_label1.place(x=250,y=100)
    
def owner_work():
    global owner_win
    
    statistics1()
def owner_window():
    global owner_win
    global VS_root
    VS_root.withdraw()
    owner_win=Toplevel()
    # changing the colour of main window
    owner_win.configure(bg="orange")


    # Geometry or dimensions of root Window
    owner_win.geometry('800x680')
    # Displaying Icon
    owner_win.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
     # title
    owner_win.title("Owner | BOOKSHOP AUTOMATION SYSTEM")

    view_label=Button(owner_win,text="View Inventory Level & Below Threshold",relief=SUNKEN,padx=20,pady=7,borderwidth=5,bg="Violet",command=owner_work)
    view_label.place(x=270,y=20)
    Logout_button=Button(owner_win,text=" Back ",relief=SUNKEN,bg="red",command=lambda: backy(owner_win,VS_root), anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",15)),borderwidth=5)
    Logout_button.place(x=350,y=620)
    
   
def reading_gif():
    global loaded_img
    global gif_display
    
    gif_display=Toplevel()
    gif_display.title("Reading gif:)")
    # changing the colour of main window
    gif_display.configure(bg="orange")

    # Geometry or dimensions of root Window
    gif_display.geometry('800x400')
    # Displaying Icon
    gif_display.iconbitmap('D:\Project_1\Images_Icons\Bookshop_icon_2.ico')
    
    load_gif=Label(gif_display,bg="ivory3")
    load_gif.pack(padx=20,pady=20)
    img=Image.open('D:/Project_1/Images_Icons/Searching_books.gif')
    
    for img in ImageSequence.Iterator(img):
        try:
            img=img.resize((775,350))
            loaded_img=ImageTk.PhotoImage(img)
            load_gif.configure(image=loaded_img)
            gif_display.update()
            time.sleep(0.1)
        except TypeError:
            pass
        except TclError:
            pass
        except AttributeError:
            pass
    else:
        gif_display.destroy()

def cart_image():
    global cart_window
    global loaded_img

    load_gif=Label(cart_window,bg="orange")
    load_gif.grid(row=2,column=0,padx=80)
    img=Image.open('D:/Project_1/Images_Icons/giphy.gif')
    
    for img in ImageSequence.Iterator(img):
        try:
            img=img.resize((650,250))
            loaded_img=ImageTk.PhotoImage(img)
            load_gif.configure(image=loaded_img)
            cart_window.update()
            time.sleep(0.0001)
        except TypeError:
            pass
        except TclError:
            pass
        except AttributeError:
            pass
    try:
        cart_window.after(1500,cart_image())
    except TclError:
        pass
    except AttributeError:
        pass
    
#count=0
def play_gif():
    global loaded_img
    global VS_access_window
    #global count
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
        except AttributeError:
            pass
    try:
        VS_access_window.after(1500,play_gif())

    except TclError:
        pass
    except AttributeError:
        pass
    #if(count!=40):
        #load_gif.after(0,play_gif)
        
    #else:
        #load_gif.destroy()  

        

def exit_program():

    #yes_no messagebox
    global rootaccess
    
    yes_no=messagebox.askyesno("Warning! ","Do you really want to exit? ")
    if(yes_no==True):
        
        rootaccess.destroy()
    else:
        pass
    
def clear_cart():

    sql_query="DELETE FROM CART;"
    cursor.execute(sql_query)


connection=create_connection('localhost','root','*Vasu@1528k','Bookshop_database')
cursor=connection.cursor() 
#cursor.execute("CREATE TABLE vs_members( emp_id int,username varchar(40), password varchar(15), PRIMARY KEY (emp_id));" )

# Do the related stuff
#cursor.execute("ALTER TABLE vs_members add Employee_Type varchar(40);")


#Added

'''
def close_connection():
    #close the connnection
    if (connection):
        connection.close()

'''


#root_access()
# clear the cart before other customer use after purchase of current customer
#clear_cart()




if __name__=="__main__":
    root_access()
    clear_cart()
    rootaccess.mainloop()
    #commit changes
    connection.commit()

