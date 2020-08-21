from tkinter import *

# tkinter initialized 
root = Tk()
# Created func() 
def getvals():
    print(f"{namevalue.get()}, {phonevalue.get()}, {gendervalue.get()}, {emergencyvalue.get()}, { paymentvalue.get()}, {foodservicevalue.get()}")
    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get()}, {phonevalue.get()}, {gendervalue.get()}, {emergencyvalue.get()}, { paymentvalue.get()}, {foodservicevalue.get()}\n")         
# Used geometry() Method To Limit The Initial Size
root.geometry("455x555")
# Label Created Using Label() Class
Label(root, relief = SUNKEN, pady = 10, text = "          TEST          ",fg = "white", bg = "skyblue").grid(row = 0, column = 2)
Label(root, relief = SUNKEN,text = "Welcome to VinayTravels", bg = "lightgreen",fg = "white", pady = 10,font = "Arial 13 bold").grid(row = 0, column = 3)
Label(root, relief = SUNKEN, pady = 10, text = "           GUI            ",fg = "white", bg = "lightgreen").grid(row = 0, column = 4)
Label(root, relief = SUNKEN, pady = 10, text = "          USING          ",fg = "white", bg = "grey").grid(row = 1, column = 2)
Label(root, text = "\"A Faster Way to transport\"", bg = "skyblue", fg = "white", padx = 5,relief = SUNKEN, font = "Helvetica 10").grid(row = 1, column = 3)
Label(root, relief = SUNKEN, pady = 10, text = "          TKINTER          ",fg = "white", bg = "skyblue").grid(row = 1, column = 4)
# Created Label For Form Option
name = Label(root, text = "Name")
phone = Label(root, text = "Phone-Number")
gender = Label(root, text = "Gender")
emergency = Label(root, text = "Emergency-Contact")
paymentmode = Label(root, text = "Payment Mode")
# Above Labels Packed Using .grid() method
name.grid(row = 2 , column = 2)
phone.grid(row = 3, column = 2)
gender.grid(row = 4, column = 2)
emergency.grid(row = 5, column = 2)
paymentmode.grid(row = 6, column = 2)
# Cleated a TextArea Using Stringvar() class 
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
# Created IntVar() Because A CheckBox Can Only Be 1 Or 0
foodservicevalue = IntVar() 
# Created Entry Variables Using Entry Class 
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue )
genderentry = Entry(root, textvariable =gendervalue )
emergencyentry = Entry(root, textvariable = emergencyvalue)
paymententry = Entry(root, textvariable = paymentvalue)
# Packed All The Entry Variabels Using .grid() func.
nameentry.grid(row = 2 , column = 3)
phoneentry.grid(row = 3 , column = 3)
genderentry.grid(row = 4 , column = 3)
emergencyentry.grid(row = 5 , column = 3)
paymententry.grid(row = 6 , column = 3)
# Creating Check Box Using Checkbutton Class
foodser =Checkbutton(text = "want to prebook your meal", variable = foodservicevalue)
# Packed Chekbutton Using .grid() func.
foodser.grid(row = 7, column = 3)
# Creating A Button And Assigning It A Command
Button(text = "Submit It To Vinay Travels", command = getvals).grid(row = 8, column = 3)
# Programme Completed
root.mainloop()
