from tkinter import *
from PIL import ImageTk
from tkinter import messagebox as tmsg
class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login-System")
        self.root.geometry("1350x700+0+0")
        # Inserting background image
        self.bg_img = ImageTk.PhotoImage(file = "bg.jpg")
        self.logo_icon = PhotoImage(file = "logo.png")
        Label(self.root, image = self.bg_img).pack()
        Label(self.root, text = "Login System", font = ("times new roman",40,"bold"), bg = "yellow",fg = "red", bd = 10,relief = GROOVE).place(x = 0, y = 0,relwidth = 1)
        log_frame = Frame(self.root,bg= "white")
        log_frame.place(x= 550, y = 150)
        self.uname = StringVar()
        self.pass_ = StringVar()

        Label(log_frame,image = self.logo_icon, bd = 0).grid(row = 0, columnspan = 2,pady = 20)
        Label(log_frame, text = "Username",compound = LEFT,font = ("times new roman",20,"bold")).grid(row = 1, column = 0, padx = 20, pady = 10)
        txtuser = Entry(log_frame, bd = 5,textvariable = self.uname, relief = GROOVE, font = ("",15)).grid(row = 1, column = 1, padx = 20)
        txtpass = Entry(log_frame, bd = 5,textvariable = self.pass_, relief = GROOVE, font = ("",15)).grid(row = 2, column = 1, padx = 20)
        Label(log_frame, text = "Password",compound = LEFT,font = ("times new roman",20,"bold")).grid(row = 2, column = 0, padx = 20, pady = 10)
        Button(log_frame, text = "Log in",command = self.login, width = 15, font = ("times new roman",20,"bold"), bg = "yellow", fg = "red").grid(row = 3, column = 1, pady = 20)
    
    def login(self):
        if self.uname.get()=="" or self.pass_.get() == "":
            tmsg.showerror("Error","All fields are requried")
        elif self.uname.get()=="vinay" and self.pass_.get() == "vinay@1234":
            tmsg.showinfo("Successfull",f"welcome{self.uname.get()}")
        else:
            tmsg.showerror("Error","Invalid Username or password")


root = Tk()
obj = Login_System(root)
root.mainloop()