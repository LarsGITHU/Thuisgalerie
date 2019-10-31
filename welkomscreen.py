from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
import random
import json

bezoekersInfo_dict = {}
ghoudersInfo_dict = {}
uniqueCode = []


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

def terugRegOfLogNaarFirspage():
    regOfLog.pack_forget()
    root.geometry("700x250")
    welkom_label.pack(side=TOP, pady=10, padx=10)
    bezoekers_button.pack(side=LEFT, pady=10, padx=10)
    ghouder_button.pack(side=RIGHT, pady=10, padx=10)
    FirstPage.pack()

def terugRegFrameFirspage():
    regFrame.pack_forget()
    root.geometry("700x250")
    welkom_label.pack(side=TOP, pady=10, padx=10)
    bezoekers_button.pack(side=LEFT, pady=10, padx=10)
    ghouder_button.pack(side=RIGHT, pady=10, padx=10)
    FirstPage.pack()



def toonRegOfLogFrame():
    root.geometry("350x320")

    FirstPage.pack_forget()
    regOfLog.pack()
    
    reg_button.grid(row=0,column=0, padx=50, pady=50)
    log_button.grid(row=0,column=3, padx=50, pady=50)
    terug_button2.grid(row=1, column=3, pady= 100)
    



def terugRegNaarRegofLog():
    gh_inloggenFrame.pack_forget()
    regOfLog.pack()
    reg_button.grid(row=0,column=0, padx=50, pady=50)
    log_button.grid(row=0,column=3, padx=50, pady=50)
    terug_button2.grid(row=1, column=3, pady= 100)
    root.geometry("350x320")



def kunststukkenLijstFrame():
    pass



def gH_inlog_info():

    gHI_naam = str(gHouder_naam.get())
    gHI_email = str(gHouder_email.get())

    if ghouderI_naam == "" or ghouderI_email == "":
        print(ghoudersInfo_dict)
    
    """
    try:
        if ghouderI_naam == "" or ghouderI_email == "":
            bericht = "Voer uw naam en emailadres in A.U.B."
            showinfo(title='Not a Valid Input', message=bericht)

        else:

            ghouder_inloggen_info.append(ghouderI_naam, gehouderI_email)
            if ghouder_inloggen_info[0] in ghoudersInfo_dict.keys():
                if ghouderI_email == ghoudersInfo_dict ['ghouder email']:
                    kustStukkenLijstFrame()
                else:
                    bericht = "Voer de juiste data in A.U.B."
                    showinfo(title='Fout!', message=bericht)
            else:
                bericht = "Voer de juiste data in A.U.B."
                showinfo(title='Fout!', message=bericht)
            
        return GhouderInfo_dict

    except:
        pass
    """







def registratieFrame():
    regOfLog.pack_forget()
    regFrame.pack()

    gHouder_naam.grid(row=0,column=1, padx=5, pady=5)
    gHouder_email.grid(row=1,column=1, padx=5, pady=5)
    gHouder_postcode.grid(row=2,column=1, padx=5, pady=5)

    gHouder_naam_label.grid(row=0,column=0, padx=5, pady=5)
    gHouder_email_label.grid(row=1,column=0, padx=5, pady=5)
    gHouder_postcode_label.grid(row=2,column=0, padx=5, pady=5)

    
    inloggen_button3.grid(row=3, column=2, padx=2, pady=5)
    terug_button3.grid(row=4, column=2, padx=2, pady=5)
    root.geometry("350x190")
    
def toonGh_inloggenFrame():
    regOfLog.pack_forget()
    gh_inloggenFrame.pack()

    inloggennaamGhouder_entry.grid(row=1, column=1, pady=5, padx=10)
    emailGhouder_entry.grid(row=2, column=1, pady=5, padx=10)
    inloggennaamGhouder_label.grid(row=1, column=0, pady=5, padx=10)
    emailGhouder_label.grid(row=2, column=0, pady=5, padx=10)
    terug_button_gh.grid(row=3, column=2)
    inloggenGhouder_button.grid(row=3, column=3)
    root.geometry("400x120")


def gallerieBezoekersFrame():
    pass

def gallerieBezoekersCode():
    r = random.randint(1000,9999)
    while True:
        if r not in uniqueCode:
            uniqueCode.append(r)
            return r
        else:
           continue




def gekozenKunstwerkFrame():
    pass

def uitgeleendeKunststukkenFrame():
    pass



def bezoekersInfo():
    bez_naam = str(inloggennaam_entry.get())   
    bez_email = str(email_entry.get())
    try:
        if bez_naam == "" or bez_email == "":
            bericht = "Voer uw naam en emailadres in A.U.B."
            showinfo(title='Not a Valid Input', message=bericht)

        elif bez_naam.isalpha() == False:
            bericht = "Voer uw eerste naam in"
            showinfo(title='Not a Valid Input', message=bericht)

        else:
            bez_code = gallerieBezoekersCode()
            bezoekersInfo_dict[bez_naam] = [bez_email, bez_code]
            with open('bezoekers-data.txt', 'a') as f:
                for i, v in bezoekersInfo_dict.items():
                    f.write('{}  {}\n'.format(i, v))
            kustStukkenLijstFrame()

    except:
        pass


def gHouderInfo():
    ghouder_dict = {}

    gH_naam = str(gHouder_naam.get())
    gH_email = str(gHouder_email.get())
    gH_postcode = str(gHouder_postcode.get())
    fn_ln = gH_naam.split()
    

    
            
    try:
        if gH_naam == "" or gH_email == "" or gH_postcode == "":
            bericht = "Unvalid input. Probeer nog een keer!"
            showinfo(title='Not a Valid Input', message=bericht)         

        else:
            ghouder_dict['ghouder naam'] = [gH_naam]
            ghouder_dict['ghouder email'] = [gH_email]
            ghouder_dict['ghouder postcode'] = [gH_postcode]
            gh_firstname = fn_ln[0]
            ghoudersInfo_dict[gh_firstname] = ghouder_dict
            json_gh_data = json.dumps(ghoudersInfo_dict, indent=4)
            
            with open('gallerihouder-data.json', 'w') as json_file:
                json_file.write(json_gh_data)
            
            print(ghouder_dict)
            print(ghoudersInfo_dict)
            
            terugRegFrameFirspage()
            toonRegOfLogFrame()
        

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

######################################################################
"""
# Max | gekozen kunstwerk lijst frame 

gekozenKunstwerk = Frame(root)
button_kunstwerkzoeker = Button(master=bezochteKunstwerk, text= "zoek kunstwerk")

gekozenImage = PhotoImage(file='')
labelImage = Label(master=bottomframe, image=photo)
labelImage.image = gekozenImage
label.pack(side=LEFT)

#bezoekersFrameNaInlog = Frame(master=root)
#bezoekersFrameNaInlog.pack(fill="both", expand=True)
ButtonNaardewebsite = Button(master=bottomframe, text= "kaartje kopen", command=open)
ButtonNaardewebsite.pack()
"""




























gh_inloggenFrame = Frame(master=root)
gh_inloggenFrame.pack(fill="both", expand=True)
inloggennaamGhouder_entry = Entry(master=gh_inloggenFrame)
emailGhouder_entry = Entry(master=gh_inloggenFrame)
inloggennaamGhouder_label = Label(master=gh_inloggenFrame, text="Naam")
emailGhouder_label = Label(master=gh_inloggenFrame, text="Email")
terug_button_gh = Button(master=gh_inloggenFrame, text="Terug", command=terugRegNaarRegofLog)
inloggenGhouder_button = Button(master=gh_inloggenFrame, text="Inloggen", command="")



































#######################################################################


regOfLog = Frame(master=root)
regOfLog.pack(fill='both', expand=True)


reg_button = Button(master=regOfLog, text="registratie", command=registratieFrame)
log_button = Button(master=regOfLog, text="inloggen", command=toonGh_inloggenFrame)
terug_button2 = Button(master=regOfLog, text="Terug", command=terugRegOfLogNaarFirspage)

######################################################################

regFrame = Frame(master=root)
regFrame.pack(fill='both', expand=True)


gHouder_naam = Entry(master=regFrame)
gHouder_email = Entry(master=regFrame)
gHouder_postcode= Entry(master=regFrame)

gHouder_naam_label = Label(master=regFrame, text="Vol naam")
gHouder_email_label = Label(master=regFrame, text="Email")
gHouder_postcode_label = Label(master=regFrame, text="Postcode")


terug_button3 = Button(master=regFrame, text="Terug", command=terugRegFrameFirspage)

inloggen_button3 = Button(master=regFrame, text="Inloggen", command=gHouderInfo)






################################################################

bezoekersFrame = Frame(master=root)

bezoekersFrame.pack(fill="both", expand=True)
inloggennaam_entry = Entry(master=bezoekersFrame)

email_entry = Entry(master=bezoekersFrame)
inloggennaam_label = Label(master=bezoekersFrame, text="Naam")

email_label = Label(master=bezoekersFrame, text="Email")
terug_button1 = Button(master=bezoekersFrame, text="Terug", command=terugBezoekersNaarFirstpage)

inloggen_button = Button(master=bezoekersFrame, text="Inloggen", command=bezoekersInfo)




#######################################################################


welkom_label = Label(master=FirstPage, text="Welkom in onze programma\nBen je een bezoeker of een galeriehouder?")
welkom_label.pack(side=TOP, pady=10, padx=10)

bezoekers_button = Button(master=FirstPage, text="Bezoeker", command=toonBezoekersFrame)
bezoekers_button.pack(side=LEFT, pady=10, padx=10)

ghouder_button = Button(master=FirstPage, text="Galleriehouder", command=toonRegOfLogFrame)
ghouder_button.pack(side=RIGHT, pady=10, padx=10)


 ########################################################################

FirstPage.pack()

root.mainloop()