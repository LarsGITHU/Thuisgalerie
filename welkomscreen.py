from tkinter import *
from PIL import ImageTk, Image 
root= Tk()
root.geometry("700x250")
FirstPage = Frame(root)
root.title("Rijksmuseum App")


photo = PhotoImage(file= 'rm-logo.gif')
label = Label(root, image = photo)
label.image = photo
label.pack(side=TOP, padx=10)



welkom_label = Label(FirstPage, text="Welkom in onze programma\nBen je een bezoeker of een galeriehouder?")
welkom_label.pack(side=TOP, pady=10, padx=10)


bezoekers_button = Button(FirstPage, text="Bezoeker")
bezoekers_button.pack(side=LEFT, pady=10, padx=10)

ghouder_button = Button(FirstPage, text="Galleriehouder")
ghouder_button.pack(side=RIGHT, pady=10, padx=10)

def clicked():
    pass
FirstPage.pack()
root.mainloop()