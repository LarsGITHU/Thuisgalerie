from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo

def toonBezoekersFrame():
    FirstPage.pack_forget()
    bezoekersFrame.pack()
    inloggennaam_entry.grid(row=1, column=1, pady=5, padx=10)
    email_entry.grid(row=2, column=1, pady=5, padx=10)
    inloggennaam_label.grid(row=1, column=0, pady=5, padx=10)
    email_label.grid(row=2, column=0, pady=5, padx=10)
    terug_button1.grid(row=3, column=2)
    inloggen_button.grid(row=3, column=3)
    root.geometry("400x100")

def terugBezoekersNaarFirstpage():
    bezoekersFrame.pack_forget()
    root.geometry("700x250")
    welkom_label.pack(side=TOP, pady=10, padx=10)
    bezoekers_button.pack(side=LEFT, pady=10, padx=10)
    ghouder_button.pack(side=RIGHT, pady=10, padx=10)
    FirstPage.pack()

def kunststukkenLijstFrame():
    pass

def leenbareKunststukkenFrame():
    pass


def gallerieBezoekersFrame():
    pass

def gallerieBezoekersCode():
    pass

def bezochteKunstwerkFrame():
    pass

def uitgeleendeKunststukkenFrame():
    pass



def bezoekersInfo():
 
    bezoekersInfo_dict = {}
    bez_naam = str(inloggennaam_entry.get())
   
    bez_email = str(email_entry.get())
    try:
        if (bez_naam or bez_email) == "":
            bericht = "Voer uw naam en emailadres in A.U.B."
            showinfo(title='Not a Valid Input', message=bericht)

        elif bez_naam.isalpha() == False:
            bericht = "Voer uw naam in"
            showinfo(title='Not a Valid Input', message=bericht)

        else:
            bezoekersInfo_dict[bez_naam] = bez_email
            kustStukkenLijstFrame()
            return bezoekersInfo_dict
    except:
        pass

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

inloggen_button = Button(master=bezoekersFrame, text="Inloggen", command=bezoekersInfo)


welkom_label = Label(master=FirstPage, text="Welkom in onze programma\nBen je een bezoeker of een galeriehouder?")
welkom_label.pack(side=TOP, pady=10, padx=10)

bezoekers_button = Button(master=FirstPage, text="Bezoeker", command=toonBezoekersFrame)
bezoekers_button.pack(side=LEFT, pady=10, padx=10)

ghouder_button = Button(master=FirstPage, text="Galleriehouder")
ghouder_button.pack(side=RIGHT, pady=10, padx=10)

FirstPage.pack()



root.mainloop()