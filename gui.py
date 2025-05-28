from tkinter import Tk,Menu, Button, Canvas, messagebox, PhotoImage,NW 

class GUI():
    def __init__(self):
        #set up root of 
        root = Tk()
        root.wm_title('maze')
        #root.iconphoto(True, PhotoImage(file = "wall0.gif") )

        #set up menubar
        menubar = Menu(root)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help ",command=lambda : messagebox.showinfo("Help", "This is the help message."))
        helpmenu.add_command(label="About...")
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)

        #set up canvas
        canvas = Canvas(root, width=100, height=100)
        canvas.grid(row=1,column=0,columnspan =3,rowspan = 3)

        #set up canvas
        l_button = Button(root,text="left")
        l_button.grid(row=4,column=0)
        r_button = Button(root,text="right")
        r_button.grid(row=4,column=2)

        #start gui
        root.mainloop()

if __name__ == "__main__":    
    gui = GUI()
    
