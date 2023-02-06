from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

cspaces = 150
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Venky950",
    database="lmanage"
)


def vehicleentry():
    tkWindow_2 = Tk()
    tkWindow_2.geometry('1200x800+600+600')
    tkWindow_2.title('VECILE ENTRY')
    img = Image.open('car.jpg')
    img = img.resize((1400, 1400))
    bg = ImageTk.PhotoImage(img)
    label = Label(tkWindow_2, image=bg)
    label.place(x=0, y=0)
    # vechile no
    VnoLabel = Label(tkWindow_2, text="Vechile no (XXXX-XX-XXXX)",font=('times new roman',14),background='gray27',fg='white').place(x=300,y=100)
    vno = StringVar()
    Vnoentry = Entry(tkWindow_2, textvariable=vno, show='').place(x=580,y=100,width=200,height=20)

    # vechile name
    VnameLabel = Label(tkWindow_2, text="Vechile name",font=('times new roman',14),background='gray27',fg='white').place(x=420,y=150)
    vname = StringVar()
    vnameentry = Entry(tkWindow_2, textvariable=vname, show='').place(x=580,y=150,width=200,height=20)

    # owner name
    onameLabel = Label(tkWindow_2,text="Owner name",font=('times new roman',14),background='gray27',fg='white').place(x=420,y=200)
    oname = StringVar()
    onameEntry = Entry(tkWindow_2, textvariable=oname, show='').place(x=580,y=200,width=200,height=20)

    # date
    dateLabel = Label(tkWindow_2, text="Date(DD-MM-YYYY)",font=('times new roman',14),background='gray27',fg='white').place(x=380,y=250)
    datel = StringVar()
    dateEntry = Entry(tkWindow_2, textvariable=datel, show='').place(x=580,y=250,width=200,height=20)

    timeLabel = Label(tkWindow_2, text="Time(HH:MM:SS)",font=('times new roman', 14),background='gray27',fg='white').place(x=380,y=300)
    timel = StringVar()
    timeLabel = Entry(tkWindow_2, textvariable=timel, show='').place(x=580,y=300,width=200,height=20)

    # Submit button
    loginButton = Button(tkWindow_2, text="Submit",font=('times new roman', 14),background='green',fg='white',command=tkWindow_2.destroy).place(x=620,y=350,width=150,height=20)

    tkWindow_2.mainloop()

    global cspaces
    cspaces=cspaces - 1
    print("Done!")

    Vehicle_Number = vno.get()
    vehicle_Name = vname.get()
    Owner_Name = oname.get()
    Date = datel.get()
    Time = timel.get()
    data = (Vehicle_Number,vehicle_Name,Owner_Name,Date,Time)

    print("DATA = ", data)

    sql = "insert into vehicles(Vehicle_Number,vehicle_Name,Owner_Name,Date,Time) values(%s,%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print(".............")
    print("Data entered successfully")
    ViewLeftOverSpaces(cspaces)
    main()


def RemoveEntry():
    tkWindow = Tk()
    tkWindow.geometry('1200x800+600+600')
    tkWindow.title('REMOVE ENTRY')
    img = Image.open('car.jpg')
    img = img.resize((1200, 1200))
    bg = ImageTk.PhotoImage(img)
    label = Label(tkWindow, image=bg)
    label.place(x=0, y=0)

    carLabel = Label(tkWindow, text="Vehicle Number",font=('times new roman',18),background='grey27',fg='white').place(x=420,y=400)
    carcode = StringVar()
    carEntry = Entry(tkWindow,textvariable=carcode).place(x=640,y=400,width=200,height=28)

    # Submit button
    loginButton = Button(tkWindow, text="Submit",font=('times new roman',14),bg='green',fg='white',command=tkWindow.destroy).place(x=580,y=455,width=150,height=20)

    global cspaces
    cspaces=cspaces + 1
    tkWindow.mainloop()

    ac = carcode.get()
    sql = "delete from vehicles where Vehicle_Number = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    main()


def ViewParkedVehicles():
    tkWindow = Tk()
    tkWindow.geometry('1200x800+600+600')
    tkWindow.title('VIEW PARKED VEHICLES')
    img = Image.open('car.jpg')
    img = img.resize((1500, 1200))
    bg = ImageTk.PhotoImage(img)
    label = Label(tkWindow, image=bg)
    label.place(x=0, y=0)
    dvalues = Label(tkWindow, text="Vehicle_Number\tvehicle_Name\tOwner_Name\tDate\t\tTime",font=('times new roman',23), background='gray14',fg='white').place(x=18,y=10)

    sql = "select * from vehicles"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    cnt = 50
    for i in myresult:
        Vehicle_Number=Label(tkWindow,text=i[0],font=('arial bold',18),background='gray27',fg='white').place(x=50,y=cnt)
        vehicle_Name=Label(tkWindow, text=i[1],font=('arial bold',18),background='gray27',fg='white').place(x=300,y=cnt)
        Owner_Name=Label(tkWindow, text=i[2],font=('arial bold',18),background='gray27',fg='white').place(x=550,y=cnt)
        Date=Label(tkWindow, text=i[3],font=('arial bold',18),background='gray27',fg='white').place(x=750,y=cnt)
        Time=Label(tkWindow, text=i[4],font=('arial bold',18),background='gray27',fg='white').place(x=1020,y=cnt)
        cnt += 2

    tkWindow.mainloop()
    main()


def ViewLeftOverSpaces():
    tkWindow = Tk()
    tkWindow.geometry('1200x800+600+600')
    tkWindow.title('VIEW PARKED VEHICLES')
    tkWindow.configure(bg='gray27')
    img = Image.open('car.jpg')
    img = img.resize((1500,1200))
    bg = ImageTk.PhotoImage(img)
    label = Label(tkWindow, image=bg)
    label.place(x=0, y=0)

    available = Label(tkWindow, text="AVAILABLE SPACES:",font=('arial bold',18), background='gray27', fg='white').place(x=300,y=300)
    aventry = Label(tkWindow,text=cspaces,font=('arial bold',18),background='gray27',fg='white').place(x=560,y=300)
    tkWindow.mainloop()
    main()


def bill():
    tkWindow = Tk()
    tkWindow.geometry('1200x800+600+600')
    tkWindow.title('BILL')
    tkWindow.configure(bg='gray27')
    img = Image.open('car.jpg')
    img = img.resize((1500, 1200))
    bg = ImageTk.PhotoImage(img)
    label = Label(tkWindow, image=bg)
    label.place(x=0, y=0)

    carLabel = Label(tkWindow, text="Vehicle Number",font=('times new roman',18),background='grey27',fg='white').place(x=420,y=400)
    ccode = StringVar()
    carEntry = Entry(tkWindow,textvariable=ccode).place(x=640,y=400,width=200,height=28)

    loginButton = Button(tkWindow,text="ENTER",font=('roboto',13),background='green',fg='white',command=lambda: [tkWindow.destroy(),billnumbers()]).place(x=500,y=600)

    tkWindow.mainloop()
    global cspaces
    cspaces = cspaces + 1
    ac = ccode.get()
    sql = "delete from vehicles where Vehicle_Number = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    main()

class billnumbers(Tk):
    def __init__(self):
        super().__init__()

        self.title("BILL")
        self.geometry("400x200")
        self.configure(bg='gray27')

        self.A = IntVar()

        self.A.trace_add("write", self.calculate_bill)

        self.create_widgets()

    def create_widgets(self):
        self.A_label = Label(self, text="ENTER THE NO.OF HOURS: ",font=('Helvetica',12),bg='gray27',fg='white')

        self.A_entry = Entry(self, textvariable=self.A)

        self.bill_label = Label(self, text="BILL: ",font=('Helvetica',12),bg='gray27',fg='white')
        self.result_label = Label(self, text=self.A.get())

        self.A_label.grid(row=5, column=0, padx=10, pady=10)
        self.A_entry.grid(row=5, column=1, padx=10, pady=10)
        self.bill_label.grid(row=7, column=0, padx=10, pady=10)
        self.result_label.grid(row=7, column=1, padx=10, pady=10)

    def calculate_bill(self, *args):
        try:
            num_a = self.A.get()
        except:
            num_a = 0

        self.result_label['text'] = num_a * 60

billnumbers()
mainloop()

def exit():
    for i in range(10):
        if i == 5:
            quit()


def main():
    # window
    tkWindow = Tk()
    tkWindow.geometry('1200x800+600+600')
    tkWindow.title('OPTIONS')
    img = Image.open('car.jpg')
    img = img.resize((1200, 1200))

    bg = ImageTk.PhotoImage(img)
    label = Label(tkWindow, image=bg)
    label.place(x=0, y=0)

    loginButton_1 = Button(tkWindow, text="VECHILE ENTRY",font=('roboto',13),background='gray27',fg='white',command=lambda: [tkWindow.destroy(),vehicleentry()]).place(x=500,y=100)
    loginButton_2 = Button(tkWindow, text="REMOVE ENTRY",font=('roboto',13),background='gray27',fg='white', command=lambda: [tkWindow.destroy(),RemoveEntry()]).place(x = 500,y = 200)
    loginButton_3 = Button(tkWindow, text="VIEW PARKED VECHILE",font=('roboto',13),background='gray27',fg='white', command=lambda: [tkWindow.destroy(),ViewParkedVehicles()]).place(x = 500,y = 300)

    loginButton_4=Button( tkWindow,text="VIEW LEFT OVER SPACES",font=('roboto',13),background='gray27',fg='white', command=lambda: [ tkWindow.destroy(),ViewLeftOverSpaces()]).place(x =500,y = 400)
    loginButton_5 = Button(tkWindow, text="BILL", font=('roboto', 13), background='gray27', fg='white',command=lambda: [tkWindow.destroy(), bill()]).place(x=500, y=500)
    loginButton_6 = Button(tkWindow, text="EXIT",font=('roboto',13),background='gray27',fg='white', command=lambda: [tkWindow.destroy(),exit()]).place(x=500, y=600)

    tkWindow.mainloop()


def password():
    import random
    ps = random.randint(0000,10000)

    # user = input("Enter Username: ")
    print("Your password is:", ps)

    user, verify = tk()

    # verify = input("Enter password:")

    if verify == str(ps):
        main()
    else:
        verify != str(ps)
        print("wrong password")
        password()


def tk():
    # window
    tkWindow = Tk()
    tkWindow.geometry('1200x800+600+600')
    tkWindow.title('LOGIN')
    img = Image.open('car.jpg')
    img = img.resize((1300,1500))

    bg = ImageTk.PhotoImage(img)
    label = Label(tkWindow,image=bg)
    label.place(x=0, y=0)

    # username label and text entry box
    titlelabel = Label(tkWindow,text="CAR PARKING MANAGEMENT SYSTEM",font=('Eras Medium ITC',28),fg='white',background='BLACK').place(x=300,y=150)
    usernameLabel = Label(tkWindow,text="Username",font=('calibri',18),fg='white',background='gray27').place(x=390,y=360)
    username = StringVar()
    usernameEntry = Entry(tkWindow,textvariable=username,width=20).place(x=520, y=361,width=250,height=25)

    # password label and password entry box
    passwordLabel = Label(tkWindow,text="Password",font=('calibri',18),fg='white',background='gray27').place(x=390,y=410)
    password = StringVar()
    passwordEntry = Entry(tkWindow,textvariable=password, show='*').place(x=520, y=401,width=250,height=25)

    # validateLogin = partial(validateLogin, username, password)

    # login button
    loginButton = Button(tkWindow, text="LOGIN",font=('Arial',12),fg='White',command=tkWindow.destroy,bg='green').place(x=590, y=451,width=150,height=25)

    tkWindow.mainloop()

    return username.get(), password.get()


password()
