from tkinter import *


class Window(Frame):
    
    def __init__(self, master):
      
        Frame.__init__(self)        
        
        self.master = master 
        
        self.init_window()

    def init_window(self):
      
        self.master.title("Rijksmuseumgalerie")

        self.pack(fill=BOTH, expand=1)

        bezoekerButton = Button(self, text="Bezoekers") # command=clicked)
        bezoekerButton.pack(pady=10, padx=10, side=RIGHT)
        #grbezoekerButton.place(y=200)
        #bezoekerButton.grid(row=0, column=0, pady=5, padx=5)

        ghouderButton = Button(self, text="Galerie houder") #, command=clicked)
        ghouderButton.pack(pady=10, padx=10, side=LEFT)
        #ghouderButton.place(y=200)
        #ghouderButton.grid(row=1, column=5, pady=5, padx=5)

class PageOne(Frame):
    
    def __init__(self, master):
        
        Frame.__init__(self):

    loginframe = Frame(master=root)
    loginframe.pack(fill="both", expand=True)

    #def client_exit(self):
    #   exit()

    #def clicked(self):


root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()






"""
    def __init__(self, naam, email, code):
        self.naam = naam
        self.email = email
        self.code = code
"""