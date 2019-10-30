from tkinter import *
from PIL import ImageTk, Image 

def toonBezoekersFrame():
    FirstPage.pack_forget()
    bezoekersFrame.pack()
    inloggennaam_entry.grid(row=1, column=1, pady=5, padx=10)
    email_entry.grid(row=2, column=1, pady=5, padx=10)
    inloggennaam_label.grid(row=1, column=0, pady=5, padx=10)
    email_label.grid(row=2, column=0, pady=5, padx=10)
    terug_button1.grid(row=3, column=2)
    root.geometry("300x100")

def terugBezoekersNaarFirstpage():
    bezoekersFrame.pack_forget()
    root.geometry("700x250")
    welkom_label.pack(side=TOP, pady=10, padx=10)
    bezoekers_button.pack(side=LEFT, pady=10, padx=10)
    ghouder_button.pack(side=RIGHT, pady=10, padx=10)
    FirstPage.pack()




    
root= Tk()
root.geometry("700x250")
root.title("Rijksmuseum App")







FirstPage = Frame(master=root)
photo = PhotoImage(file= 'rm-logo.gif')
label = Label(master=FirstPage, image = photo)
label.image = photo
label.pack(side=TOP, padx=10)

bezoekersFrame = Frame(master=root)
bezoekersFrame.pack(fill="both", expand=True)
inloggennaam_entry = Entry(master=bezoekersFrame)
email_entry = Entry(master=bezoekersFrame)
inloggennaam_label = Label(master=bezoekersFrame, text="Naam")
email_label = Label(master=bezoekersFrame, text="Email")
terug_button1 = Button(master=bezoekersFrame, text="Terug", command=terugBezoekersNaarFirstpage)



welkom_label = Label(master=FirstPage, text="Welkom in onze programma\nBen je een bezoeker of een galeriehouder?")
welkom_label.pack(side=TOP, pady=10, padx=10)
bezoekers_button = Button(master=FirstPage, text="Bezoeker", command=toonBezoekersFrame)
bezoekers_button.pack(side=LEFT, pady=10, padx=10)
ghouder_button = Button(master=FirstPage, text="Galleriehouder")
ghouder_button.pack(side=RIGHT, pady=10, padx=10)
FirstPage.pack()



root.mainloop()