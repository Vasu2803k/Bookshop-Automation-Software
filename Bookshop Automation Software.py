print("BOOKSHOP AUTOMATION SYSTEM")
def open_Bookshop():
    print("Welcome to the new version of Bookshop :)")
    print(">Open or close")
    is_type=False
    while not is_type:
        try:
            open_close=(input(">Type 'Yes' to open and 'No' to close: ").lower())
            if(open_close=="yes"):
                print(">Let's get started")
                break
            elif(open_close=="no"):
                print(">Thanks-Visit Again")
                exit()
        except Exception:
            print(">Wrong!-Type/Input correctly")  
            is_type=False
        else:
            print(">only choose 'Yes' or 'No'")
            is_type=False
        
open_Bookshop()            
