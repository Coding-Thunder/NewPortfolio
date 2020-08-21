from tkinter import *
import tkinter.messagebox as tmsg
root  = Tk()


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "𝔼𝕣𝕣𝕠𝕣(𝔼𝕟𝕥𝕖𝕣-𝕍𝕒𝕝𝕚𝕕-𝕀𝕟𝕡𝕦𝕥)"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)



def backspace():
    global scvalue
    a = int(len(scvalue.get())) - 1
    scvalue.set(a)
    screen.update()


root.geometry("644x900")
root.wm_iconbitmap("calculator.ico")
root.title("ℂ𝔸 𝕃ℂ 𝕌𝕃 𝔸 𝕋𝕆 ℝ")
title = "🅲🅰 🅻🅲 🆄🅻 🅰🆃 🅾🆁"
subtitle = "Ⓑ Ⓔ Ⓣ Ⓐ"
Label(root,  text = title, font = "lucida 40 bold").pack()
Label(root, text = subtitle,font = "lucida 20 bold").pack()
scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvariable = scvalue, font = "lucida 40 bold")
screen.pack(fill = X, ipadx = 8, padx = 10 , pady = 10)
a = Button(root, text = "C", padx = 28, pady = 18, font = "lucida 10 bold")
a.pack(side = TOP, padx = 18, pady = 12)
a.bind("<Button-1>", click)
f = Frame(root, bg = "grey" )
b = Button(f,text = "9", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
b = Button(f,text = "8", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
b = Button(f,text = "7", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>",click)
b = Button(f,text = "6", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg = "grey" )
b = Button(f,text = "5", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
b = Button(f,text = "4", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>",click)
b = Button(f,text = "3", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
b = Button(f,text = "2", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg = "grey" )

b = Button(f,text = "1", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>",click)
b = Button(f,text = "0", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
b = Button(f,text = "+", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
b = Button(f,text = "-", padx = 28, pady = 18, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "grey" )
b = Button(f,text = "*", padx = 28, pady = 22, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
b = Button(f,text = "/", padx = 28, pady = 22, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
b = Button(f,text = "%", padx = 28, pady = 22, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>",click)
b = Button(f,text = "=", padx = 28, pady = 22, font = "lucida 25 bold" )
b.pack(side  = LEFT, padx = 18, pady = 12)
b.bind("<Button-1>", click)
f.pack()
tmsg.showinfo("𝔹𝔼 𝕋𝔸 - 𝕋𝔼 𝕊𝕋 𝕀ℕ 𝔾 - ℙℍ 𝔸𝕊 𝔼", "We Do Not Gaurantee A Error Free Software Because This SoftWare is Still Under Development, This Is Not The Final Version")
root.mainloop()
