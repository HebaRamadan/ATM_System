'''
 *  Author       : Heba Ramadan Taha
'''
import tkinter

counter = 0
Block_Account      = 0
Get_Balance         = 0
Amount_Balance   = 0
Sub_Balance         = 0
Password_Flag       = 0
Name    =0
New_Password = 0
RechargeValue  = 0
Recharge_Flag   = 0

def CreateWindow():
    global MyWindow 
    MyWindow = tkinter.Tk()
    MyWindow.geometry("450x400")
    MyWindow.title("ATM System")
    MyWindow.resizable(width = "False" , height = "False")
    MyWindow.configure(background="olive")
    i=0
    while i<10:
        MyWindow.columnconfigure(i , minsize=20)
        MyWindow.rowconfigure     (i , minsize=20)
        i+=1
    
        
def IDWidget():
    global Label_1
    global Entry_1
    global Button_1
    
    counter = 0
    
    Label_1     =   tkinter.Label(MyWindow , text = "Please Enter ID :" , bg = "olive" ,  fg = "black")
    Label_1.grid(   row = 2 , column = 1    )
    
    Entry_1     =   tkinter.Entry(MyWindow , width = 30)
    Entry_1.grid(   row = 3 , column = 2   )
    
    Button_1   =   tkinter.Button(MyWindow , text = "Enter"  , bg = "darkolivegreen" ,  fg = "black" , width = 7 , command = CheckID)
    Button_1.grid( row = 5 , column = 2   )


def HomeWidget():
        
    Label_1.configure(text = 'Welcome In My ATM '   ,fg = 'black')
    Label_1.grid( row = 0 , column = 0 )
    Entry_1.destroy()

    global Var_1
    global Withdraw
    global Balance
    global Password_Chan
    global Fawry
    global End
    
    Var_1           = tkinter.IntVar()
    
    Withdraw      = tkinter.Radiobutton(MyWindow , text ='Cash Withdraw     ' , bg = "olive"  , value = 1 , variable = Var_1 )
    Withdraw.grid( row = 2 , column = 0)
    
    Balance        = tkinter.Radiobutton(MyWindow , text ='Balance Inquiry     ' , bg = "olive" , value = 2 , variable = Var_1  )
    Balance.grid( row = 2   , column = 2 )
    
    Password_Chan= tkinter.Radiobutton(MyWindow , text ='Password Change' , bg = "olive" , value = 3 , variable = Var_1  )
    Password_Chan.grid( row = 3 , column = 0 )    
    
    Fawry           = tkinter.Radiobutton(MyWindow , text ='Fawry Service        ' , bg = "olive" , value = 4 , variable = Var_1  )
    Fawry.grid( row = 3 , column = 2 )
          
    End               = tkinter.Radiobutton(MyWindow , text ='Exit System          ' , bg = "olive" , value = 5 , variable = Var_1  )
    End.grid( row = 4 , column = 0 )
    
    
    Button_1.configure(text = 'Enter'   , command = CheckRadioButton)
    Button_1.grid( row = 6 , column = 2 )
    
    

    MyWindow.mainloop()
       
    
def PasswordWidget():
    Button_1.destroy()
    Label_1.destroy()
    Entry_1.destroy()
    IDWidget()
    Label_1.config(text = "Please Enter Password" )
    Button_1.config(command = CheckPassword )
    Entry_1.configure(show = '*')   

def CheckID():
    global ID
    ID = ""
    ID =  Entry_1.get()
    File = open("DataBase.txt" , "r")
    flag   = 0
    block = 0
    
    if ID != "":
        ID = " "+ID+" "
        while True :
            DataOfCustomer = File.readline()
            if  DataOfCustomer == "":
                break
            else:
                if DataOfCustomer.find(ID) >= 0:
                    if DataOfCustomer.find(" valid ") >= 0:
                        flag = 1
                        break
                    else:
                        block = 1
                        flag    = 6
                else :
                    pass
    
    if block == 1:
        Label_1.config(text = "This account is locked, please go to the branch.",  fg = "red")
        Button_1.config(text = "Back" , command = Back )
        Button_1.grid( row = 5 , column = 1   )
        Entry_1.destroy()
        
    else:
        pass
        
    if flag == 1 :
        PasswordWidget()
        Entry_1.delete(0 , "end")
        Entry_1.configure(show = '*')
    elif flag == 0:
        Label_1.config(text = "*Incorrect ID" , fg = "red")
        Entry_1.config(fg = "red")
        Button_1.config(text = "Back" , command = Back )

    File.close()

   
def CheckPassword():
    global counter
    global Block_Account
    Password =""
    Password =  Entry_1.get()
    
    flag = 0
    
    File = open("DataBase.txt" , "r")
    
    if Password != "":
        Password = " "+Password+" " 
        while True:
            DataOfCustomer = File.readline()
            if DataOfCustomer.find(ID) >= 0:
                if DataOfCustomer.find(Password) >= 0:
                    flag = 1
                    break
                else :
                    print("InCorrect")
                    counter += 1
                    break
            else:
                pass
    
    if flag == 1:
        #print("Correct")
        Entry_1.destroy()
        HomeWidget()
        
    else :
        if counter > 2 :
            Label_1.config(text = "This account is locked, please go to the branch.",  fg = "red")
            Entry_1.destroy()
            Button_1.config(text = "Back" , command = Back )
            Button_1.grid( row = 5 , column = 1   )
            Block_Account = 1
            ReWritInDataBase()
            counter = 0
        else :
            Label_1.config(text = "")    
            Label_1.config(text = "*Incorrect Password" , fg = "red")
            Entry_1.config(fg = "red")
            Button_1.config(text = "Back" , command = PasswordWidget)
        
    File.close()   
      
      
def Back():
    Label_1.config(text = " " )
    Button_1.destroy()
    Entry_1.destroy()
    IDWidget()
  

def ReWritInDataBase():
    global Block_Account
    global Get_Balance
    global Amount_Balance
    global AmountOfWithdraw
    global RechargeValue
    global Sub_Balance
    global Name
    global New_Password
    global Password_Flag
    global Recharge_Flag
    
    File = open("DataBase.txt" , "r")
    List = File.readlines()
    File.close()
    
    File = open("DataBase.txt" , "w")
    i = 0
    for String in List :
        if String.find(ID) >=0:
            print("Done")
            break
        else :
            i += 1
    if Block_Account == 1:
        List[i] = List[i].replace("valid" , "Nvalid")
        Block_Account = 0
        
    if Get_Balance ==  1:
        string =  List[i]
        Amount_Balance = string[string.find("Balance:")+8:string.find(".")]
        Name                = string[string.find("Name:")+5:string.find(",")]
        print(Amount_Balance)
        print(Name)
    
    if Sub_Balance == 1:
        new_balance =  int(Amount_Balance) - int(AmountOfWithdraw)
        string  =  List[i]
        string  =  string[string.find("Balance:")+8:string.find(".")]
        List[i] =  List[i].replace(string , str(new_balance))
        print(Amount_Balance)
        print(AmountOfWithdraw)
        print(str(new_balance))
        
        
    if Password_Flag == 1:
        string  =  List[i]
        string  =  string[string.find("Password: ")+10:string.find(" ,")]
        List[i] =  List[i].replace(string , str(New_Password))
        print(string)
        print(New_Password)
        
        
        
    if Recharge_Flag == 1 :
        new_balance =  int(Amount_Balance) - int(RechargeValue)
        string  =  List[i]
        string  =  string[string.find("Balance:")+8:string.find(".")]
        List[i] =  List[i].replace(string , str(new_balance))
        print(Amount_Balance)
        print(RechargeValue)
        print(str(new_balance))
     
    else :
        pass
        
    for x in List :
        print("Done")
        File.write(x)
        
    Block_Account  = 0
    Get_Balance    = 0
    Sub_Balance    = 0
    Password_Flag = 0
      
  
def CheckRadioButton():
    global  Get_Balance
    Withdraw.destroy()
    Balance.destroy()
    Password_Chan.destroy()
    Fawry.destroy()
    End.destroy()

    if (Var_1.get() == 1): 
        Get_Balance = 1
        ReWritInDataBase()
        CashWithdrawWidget()
        
    if (Var_1.get() == 2):
        Get_Balance = 1
        ReWritInDataBase()
        BalanceWidget()


    if (Var_1.get() == 3):
       ChangePasswordWidget()

    if (Var_1.get() == 4):
        FawryServiceWidget()
        
    if (Var_1.get() == 5):
        Label_1.configure(text = " ")
        Label_1.grid(   row = 0 , column = 0    )
        Button_1.destroy()
        IDWidget()       
    
        
 
def CashWithdrawWidget():
        global Button_2
        Label_1.destroy()
        Entry_1.destroy()
        Button_1.destroy()
        IDWidget()
        Label_1.configure(text = "Enter Cash withdraw amount :")
        Label_1.grid(   row = 2 , column = 0    )
        Entry_1.grid(   row = 3 , column = 1   )
        Button_1.configure(command = CashWithdraw)
        Button_1.grid( row = 5 , column = 1   )
        Button_2   =   tkinter.Button(MyWindow , text = "Back"  , bg = "darkolivegreen" ,  fg = "black" , width = 7 , command = Clr_Button )
        Button_2.grid( row = 5 , column = 2   )
  
 
def Clr_Button():
    Button_2.destroy()
    HomeWidget()
 
 
def CashWithdraw():
    global Sub_Balance
    global Amount_Balance
    global AmountOfWithdraw
    AmountOfWithdraw = Entry_1.get()
    print(AmountOfWithdraw)
    print(Amount_Balance)
    
    if  int(AmountOfWithdraw) > int(Amount_Balance) :
        Button_2.destroy()
        Label_1.config(text = "")    
        Label_1.config(text = "*Balance Not Cover This amount" , fg = "red")
        Entry_1.config(fg = "red")
        Button_1.config(text = "Back" , command = HomeWidget)
        Button_1.grid( row = 5 , column = 1   )
    elif (int(AmountOfWithdraw )% 100 != 0) or (int(AmountOfWithdraw )> 5000):
        Button_2.destroy()
        Label_1.config(text = "")    
        Label_1.config(text = "*NOT Valid Operation" , fg = "red")
        Entry_1.config(fg = "red")
        Button_1.config(text = "Back" , command = HomeWidget)
        Button_1.grid( row = 5 , column = 1   )
    else :
        Sub_Balance  = 1
        ReWritInDataBase()
        Button_2.destroy()
        Label_1.config(text = "")    
        Label_1.config(text = "Thank you ,Successful operation" , fg = "black")
        Entry_1.destroy()
        Button_1.config(text = "Back" , command = HomeWidget)
        Button_1.grid( row = 5 , column = 1   )
    
    
    
def BalanceWidget():
    global Label_2
    global Label_3
    Button_1.destroy()
    IDWidget()
    Label_1.config(text = "")  
    Label_1.configure(text = "Information About Acount :")
    Label_1.grid(   row = 0 , column = 0    )
    Entry_1.destroy()
    Button_1.configure(text = 'OK',command = CLR)
    Button_1.grid( row = 5 , column = 1   )
    
    Label_2     =   tkinter.Label(MyWindow , text = "1- Balance Inquiry: "+Amount_Balance , bg = "olive" ,  fg = "black")
    Label_2.grid(   row = 2 , column = 1    )
    Label_3     =   tkinter.Label(MyWindow , text = "2- Name : "+Name , bg = "olive" ,  fg = "black")
    Label_3.grid(   row = 3 , column = 1    )


    
def CLR():
    Label_2.destroy()
    Label_3.destroy()
    HomeWidget()
   
   
        
def ChangePasswordWidget():
        global Button_2
        global Label_2
        global Label_3
        global Entry_2

        Label_1.destroy()
        Button_1.destroy()
        IDWidget()
        Label_1.configure(text = "Change Password :")
        Label_1.grid(   row = 0 , column = 0    )
        
        Label_2     =   tkinter.Label(MyWindow , text = "Enter New Password    : " , bg = "olive" ,  fg = "black")
        Label_2.grid(   row = 2 , column = 1   )
        Entry_1.grid(   row = 2 , column = 2   )
        
        Label_3     =   tkinter.Label(MyWindow , text = "Confirm Password : " , bg = "olive" ,  fg = "black")
        Label_3.grid(   row = 3 , column = 1    )
        Entry_2     =   tkinter.Entry(MyWindow , width = 30 , fg = "black")
        Entry_2.grid(   row = 3 , column = 2   )
        
        Button_1.configure(command = ChangeCheck)
        Button_1.grid( row = 5 , column = 1   )
        Button_2   =   tkinter.Button(MyWindow , text = "Back"  , bg = "darkolivegreen" ,  fg = "black" , width = 7 , command = CLR_1)
        Button_2.grid( row = 5 , column = 2   )   



def CLR_1():
    Label_2.destroy()
    Label_3.destroy()
    Entry_1.destroy()
    Entry_2.destroy()
    Button_2.destroy()
    HomeWidget()        
    
    
def ChangeCheck():
    global Password_Flag
    global New_Password
    
    New_Password = Entry_1.get()
    y                    = Entry_2.get()
    
    flagP = 0
    if New_Password == y :
        counterP = 0
        for i in New_Password:
            if i >= '0' and i <= '9' :
                counterP +=1
            else:
                flagP = 1
    
    if  New_Password != y or counterP > 4  or  flagP == 1  or New_Password == "":
        Label_1.configure(text = "NOT Valid Password Try Again " , fg = 'red')
        Label_1.grid(   row = 1 , column = 1    )
        Entry_1.configure(fg = 'red')
        Entry_2.configure(fg = 'red')
        Button_1.destroy()
        Button_2.configure(text =  "Back",command = ChangePasswordWidget)
    
    else :
        Password_Flag = 1
        ReWritInDataBase()
        ConfirmMessage()
  
  
def ConfirmMessage():
    Label_2.destroy()
    Label_3.destroy()
    Entry_1.destroy()
    Entry_2.destroy()
    Button_2.destroy()
    
    Label_1.configure(text = " ")
    Label_1.grid(   row = 0 , column = 0   )
    Label_1.configure(text = "Successful operation , Password Changed")
    Label_1.grid(   row = 1 , column = 1    )
    Button_1.configure(text = "Back" , command = HomeWidget)
    Button_1.grid(   row = 5 , column = 2    )
        
 
def FawryServiceWidget():
    Label_1.configure(text = "  ")
    Label_1.grid(row = 0 , column = 0)
    Label_1.configure(text = "Fawry Service"   ,fg = 'black')
    Label_1.grid(row = 0 , column = 1)
    
    global Var_2
    global Orange
    global Etisalat
    global Vodafone
    global WE
    global Exit
    global Button_Back
    
    Var_2           = tkinter.IntVar()
    
    Orange        = tkinter.Radiobutton(MyWindow  , text='Orange Recharge    ' , bg = "olive"  , value = 1 , variable = Var_2 )
    Orange.grid( row = 2 , column = 0)
    
    Etisalat        = tkinter.Radiobutton(MyWindow , text='Etisalat Recharge    ' , bg = "olive" , value = 2 , variable = Var_2  )
    Etisalat.grid( row = 2   , column = 2 )
    
    Vodafone     = tkinter.Radiobutton(MyWindow  , text='Vodafone Recharge ' , bg = "olive" , value = 3 , variable = Var_2  )
    Vodafone.grid( row = 3 , column = 0 )    
    
    WE             = tkinter.Radiobutton(MyWindow  , text='WE Recharge          ' , bg = "olive" , value = 4 , variable = Var_2  )
    WE.grid( row = 3 , column = 2 )
    
    
    Button_1.configure(text = 'Enter'   , command = CheckFawryService)
    Button_1.grid( row = 6 , column = 1 )
             
    Button_Back   =   tkinter.Button(MyWindow , text = "Back"  , bg = "darkolivegreen" ,  fg = "black" , width = 7 , command = Clr_Wdgit)
    Button_Back.grid( row = 6 , column = 2   )
 

def Clr_Wdgit():
    Orange.destroy()
    Etisalat.destroy()
    Vodafone.destroy()
    WE.destroy()
    Button_Back.destroy()
    HomeWidget()
   
   
def CheckFawryService():
    Orange.destroy()
    Etisalat.destroy()
    Vodafone.destroy()
    Button_Back.destroy()
    Button_1.destroy()
    Label_1.destroy()
    WE.destroy()
    
    CreatChargeWedget()

  
def CreatChargeWedget():
    global Var_2
    global Label_2
    global Label_3
    global Button_Back
    global Entry_2
    global Get_Balance
    
    Get_Balance = 1
    ReWritInDataBase()
    IDWidget()
    Entry_2 = tkinter.Entry(MyWindow , width = 30)
    Label_2 = tkinter.Label( bg = "olive" ,  fg = "black")
    Label_3 = tkinter.Label( bg = "olive" ,  fg = "black")
    Label_1.configure(text = " ")
    Label_1.grid(   row =  0, column = 0    )
    if (Var_2.get() == 1): 
        Label_2.configure(text = "Orange Recharge")
        Label_2.grid( row = 0 , column = 1 )
        print(Var_2.get())
    
    
    if (Var_2.get() == 2):
        Label_2.configure(text = "Etisalat Recharge")
        Label_2.grid( row = 0 , column = 1 )

    if (Var_2.get() == 3):
        Label_2.configure(text = "Vodafone Recharge")
        Label_2.grid( row = 0 , column = 1 )

    if (Var_2.get() == 4):
        Label_2.configure(text = "WE Recharge ")
        Label_2.grid( row = 0 , column = 1 )

    Label_3.configure(text = "Enter Phone Number :        ")
    Label_3.grid( row = 2 , column = 0 )  
    Entry_2.grid( row = 2 , column = 1 )
    
    Label_1.configure(text = "Enter Amount Of Recharge :")
    Label_1.grid( row = 4 , column = 0 )
    Entry_1.grid( row = 4 , column = 1 )
    
    Button_1.configure(command = CheckRecharge)
    
    Button_1.grid(row = 6 , column = 1 )
    
    Button_Back   =   tkinter.Button(MyWindow , text = "Back"  , bg = "darkolivegreen" ,  fg = "black" , width = 7 , command = Clr_ButtonBack)
    Button_Back.grid( row = 6 , column = 2   )
    
       
def Clr_ButtonBack():
    Label_2.destroy()
    Label_3.destroy()
    Entry_1.destroy()
    Entry_2.destroy()
    Button_Back.destroy()
    FawryServiceWidget()
 
 
def CheckRecharge():
    global Amount_Balance
    global RechargeValue
    global Recharge_Flag

    RechargeValue = Entry_1.get()
    phonenumber  = Entry_2.get()
    phonenumber_flag = 0
    print(RechargeValue)
    print(Amount_Balance)
    
    if (Var_2.get() == 1): 
        i = 0
        for number in phonenumber :
            i = i+1
        if i == 11 and (phonenumber[0:3] == '012') :
            phonenumber_flag = 1
        
    if (Var_2.get() == 2):
        i = 0
        for number in phonenumber :
            i = i+1
        if i == 11 and (phonenumber[0:3] == '011') :
            phonenumber_flag = 1

    if (Var_2.get() == 3):
        i = 0
        for number in phonenumber :
            i = i+1
        if i == 11 and (phonenumber[0:3] == '010') :
            phonenumber_flag = 1

    if (Var_2.get() == 4):
        i = 0
        for number in phonenumber :
            i = i+1
        if i == 11 and (phonenumber[0:3] == '015') :
            phonenumber_flag = 1
    
    print(phonenumber_flag)
    if  (int(RechargeValue) > int(Amount_Balance)) or (phonenumber_flag == 0):
        Button_Back .destroy()
        Label_1.config(text = "")    
        Label_3.config(text = "*Error in operation :" , fg = "red")
        Entry_1.config(fg = "red")
        Entry_2.config(fg = "red")
        Button_1.config(text = "Back" , command = clrwedget) 
    else :
        Recharge_Flag = 1
        ReWritInDataBase()
        ConfirmMessageRecharge()
        
        
def clrwedget():
    Label_1.destroy()
    Label_2.destroy()
    Label_3.destroy()
    Entry_1.destroy()
    Entry_2.destroy()
    Button_1.destroy()
    CreatChargeWedget()
    
    
def ConfirmMessageRecharge():
    Entry_1.destroy()
    Entry_2.destroy()
    Label_2.destroy()
    Label_3.destroy()
    Button_Back.destroy() 
    Label_1.configure(text = " ")
    Label_1.grid(   row =  0, column = 0    )
    Label_1.configure(text = "Successful operation , Recharged Done ")
    Label_1.grid(   row = 1 , column = 1    )
    Button_1.configure(text = "Back" , command = HomeWidget)
    Button_1.grid(   row = 5 , column = 2    )


   