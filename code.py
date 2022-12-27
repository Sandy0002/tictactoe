from tkinter import *

obj=Tk()

ls=[]
def cross1():
    # c1()
    c=Canvas(highlightthickness=0,width=150,height=150,bg="black")#invert all colors after settings
    cl1=c.create_line(30,25,105,130,fill="white")
    cl2=c.create_line(30,130,105,25,fill="white")
    c.place(x=100,y=75)
     
def cross2():
    # c2()
    c=Canvas(highlightthickness=0,width=205,height= 175,bg="black")
    cl1=c.create_line(85,25,155,130,fill="white")
    cl2=c.create_line(85,130,155,25,fill="white")
    c.place(x=325,y=75)

def cross3():
    # c3()
    c=Canvas(highlightthickness=0,width=165,height= 165,bg="black")
    cl1=c.create_line(85,25,155,130,fill="white")
    cl2=c.create_line(85,130,155,25,fill="white")
    c.place(x=605,y=75)

def cross4():
    # c4()
    c=Canvas(highlightthickness=0,width=170,height= 170,bg="black")
    cl1=c.create_line(30,25,105,130,fill="white")
    cl2=c.create_line(30,130,105,25,fill="white")
    c.place(x=100,y=255)

def cross7():
    # c7()
    c=Canvas(highlightthickness=0,width=155,height= 155,bg="black")
    cl1=c.create_line(30,25,105,130,fill="white")
    cl2=c.create_line(30,130,105,25,fill="white")
    c.place(x=100,y=435)

def cross5():
    # c5()
    c=Canvas(highlightthickness=0,width=205,height= 165,bg="black")
    cl1=c.create_line(85,25,155,130,fill="white")
    cl2=c.create_line(85,130,155,25,fill="white")
    c.place(x=325,y=255)
    
def cross8():
    # c8()
    c=Canvas(highlightthickness=0,width=205,height= 165,bg="black")
    cl1=c.create_line(85,25,155,130,fill="white")
    cl2=c.create_line(85,130,155,25,fill="white")
    c.place(x=325,y=435)
    
def cross6():
    # c6()
    c=Canvas(highlightthickness=0,width=165,height= 165,bg="black")
    cl1=c.create_line(85,25,155,130,fill="white")
    cl2=c.create_line(85,130,155,25,fill="white")
    c.place(x=605,y=255)
    
def cross9():
    # c9()
    c=Canvas(highlightthickness=0,width=165,height= 165,bg="black")
    cl1=c.create_line(85,25,155,130,fill="white")
    cl2=c.create_line(85,130,155,25,fill="white")
    c.place(x=605,y=435)

def zero1():
    # z1()
    z=Canvas(width=150,height=150,bg="black",highlightthickness=0)
    z.create_oval(10,25,105,115,fill="black",outline="white")
    z.place(x=100,y=75)
def zero2():
    # z2()
    z=Canvas(highlightthickness=0,width=150,height= 150,bg="black")
    z.create_oval(10,25,105,115,fill="black",outline="white")
    z.place(x=390,y=75)
def zero3():
    # z3()
    z=Canvas(highlightthickness=0,width=150,height= 150,bg="black")
    z.create_oval(10,25,105,115,fill="black",outline="white")
    z.place(x=650,y=75)
def zero4():
    # z4()
    z=Canvas(highlightthickness=0,width=150,height= 150,bg="black")
    z.create_oval(10,25,105,115,fill="black",outline="white")
    z.place(x=100,y=275)
def zero7():
    # z7()
    z=Canvas(highlightthickness=0,width=150,height= 150,bg="black")
    z.create_oval(10,25,105,115,fill="black",outline="white")
    z.place(x=100,y=435)
def zero5():
    # z5()
    z=Canvas(highlightthickness=0,width=150,height= 150,bg="black")
    z.create_oval(10,25,105,115,fill="black",outline="white")
    z.place(x=390,y=275)

def zero8():
    # z8()
    z=Canvas(highlightthickness=0,width=150,height= 150,bg="black")
    z.create_oval(10,25,105,115,fill="black",outline="white")
    z.place(x=390,y=435)
def zero6():
    # z6()
    z=Canvas(highlightthickness=0,width=150,height= 150,bg="black")
    z.create_oval(10,25,105,115,fill="black",outline="white")
    z.place(x=650,y=275)
def zero9():
    # z9()
    z=Canvas(highlightthickness=0,width=150,height= 150,bg="black")
    z.create_oval(10,25,105,115,fill="black",outline="white")
    z.place(x=650,y=435)

def board():
    obj.maxsize(900,900)
    cv=Canvas(width=900,height=900,bg="black")
    
    # border lines
    cv.create_line(300,50,300,600,fill="white")
    cv.create_line(600,50,600,600,fill="white")
    cv.create_line(75,250,800,250,fill="white")
    cv.create_line(75,425,800,425,fill="white")

    cv.pack()
    # buttons
    bc1=Button(text="c1",command=cross1,fg="black",font="calibiri 11 bold")
    bc1.place(x=125,y=120)
    bc2=Button(text="c2",command=cross2,fg="black",font="calibiri 11 bold")
    bc2.place(x=425,y=120)
    bc3=Button(text="c3",command=cross3,fg="black",font="calibiri 11 bold")
    bc3.place(x=675,y=120)
    bc4=Button(text="c4",command=cross4,fg="black",font="calibiri 11 bold")
    bc4.place(x=125,y=335)
    bc7=Button(text="c7",command=cross7,fg="black",font="calibiri 11 bold")
    bc7.place(x=125,y=530)
    bc5=Button(text="c5",command=cross5,fg="black",font="calibiri 11 bold")
    bc5.place(x=425,y=335)
    bc8=Button(text="c8",command=cross8,fg="black",font="calibiri 11 bold")
    bc8.place(x=425,y=530)
    bc6=Button(text="c6",command=cross6,fg="black",font="calibiri 11 bold")
    bc6.place(x=675,y=335)
    bc9=Button(text="c9",command=cross9,fg="black",font="calibiri 11 bold")
    bc9.place(x=675,y=530)

    bz1=Button(text="z1",command=zero1,fg="black",font="calibiri 11 bold")
    bz1.place(x=175,y=120)
    bz2=Button(text="z2",command=zero2,fg="black",font="calibiri 11 bold")
    bz2.place(x=475,y=120)
    bz3=Button(text="z3",command=zero3,fg="black",font="calibiri 11 bold")
    bz3.place(x=725,y=120)
    bz4=Button(text="z4",command=zero4,fg="black",font="calibiri 11 bold")
    bz4.place(x=175,y=335)
    bz7=Button(text="z7",command=zero7,fg="black",font="calibiri 11 bold")
    bz7.place(x=175,y=530)
    bz5=Button(text="z5",command=zero5,fg="black",font="calibiri 11 bold")
    bz5.place(x=475,y=335)

    bz8=Button(text="z8",command=zero8,fg="black",font="calibiri 11 bold")
    bz8.place(x=475,y=530)
    bz6=Button(text="z6",command=zero6,fg="black",font="calibiri 11 bold")
    bz6.place(x=725,y=335)
    bz9=Button(text="z9",command=zero9,fg="black",font="calibiri 11 bold")
    bz9.place(x=725,y=530)

    obj.mainloop()
board()
