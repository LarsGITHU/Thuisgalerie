from tkinter import *
from PIL import ImageTk, Image # dezz module moet je zelf installeren: pip install Pillow. Nodig om de Rijksmuseum logo in de eerste pagina te laten zien.
from tkinter.messagebox import showinfo
import random
import json
import importlib
import sys
import os


bezoekersInfo_dict = {}
ghoudersInfo_dict = {}
uniqueCode = []

 
def toonBezoekersFrame():
    '''Laat de bezoekers loginframe zien als gedrukt op "bezoekers" is'''
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
    '''packt weer de Firstpage nadat er gedrukt op "terug" is'''
    bezoekersFrame.pack_forget()
    root.geometry("700x250")
    welkom_label.pack(side=TOP, pady=10, padx=10)
    bezoekers_button.pack(side=LEFT, pady=10, padx=10)
    ghouder_button.pack(side=RIGHT, pady=10, padx=10)
    FirstPage.pack()

def terugRegOfLogNaarFirspage():
    '''packt weer de Firstpage nadat er gedrukt op "terug" is'''
    regOfLog.pack_forget()
    root.geometry("700x250")
    welkom_label.pack(side=TOP, pady=10, padx=10)
    bezoekers_button.pack(side=LEFT, pady=10, padx=10)
    ghouder_button.pack(side=RIGHT, pady=10, padx=10)
    FirstPage.pack()

def terugRegFrameFirspage():
    '''packt weer de Firstpage nadat er gedrukt op "terug" is'''
    regFrame.pack_forget()
    root.geometry("700x250")
    welkom_label.pack(side=TOP, pady=10, padx=10)
    bezoekers_button.pack(side=LEFT, pady=10, padx=10)
    ghouder_button.pack(side=RIGHT, pady=10, padx=10)
    FirstPage.pack()



def toonRegOfLogFrame():
    '''packt de frame waarin je kunt registreren en inloggen als galleriehouder'''
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
    # importeert de andere gedeelte van de code als een externe module, daarvoor gebruiken we "importlib"
    importlib.import_module("stukken.py")







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



def gallerieBezoekersCode():
    r = random.randint(1000,9999) # generates een willekeurige, unieke 4-cijferige code en slaat die op in een lijst  en dan checkt die 
    while True:                    # of de genereerde getal daar te vindn is, om duplicates te vermijden
        if r not in uniqueCode:
            uniqueCode.append(r)
            return r
        else:
           continue


def uitgeleendeKunststukkenFrame():
    pass

def gallerieBezoekersFrame():
    pass


def bezoekersInfo():
    # Deze variables halen user entry-input en zetten die als strings in deze variables
    bez_naam = str(inloggennaam_entry.get())   
    bez_email = str(email_entry.get())
    try:
        # vermijdt lege user-input
        if bez_naam == "" or bez_email == "":
            bericht = "Voer uw naam en emailadres in A.U.B."
            showinfo(title='Not a Valid Input', message=bericht)

        # checkt of de bezoekers eerste naam uit maar geldige charakters bestaat (i.e. alphabetische letters)
        elif bez_naam.isalpha() == False:
            bericht = "Voer uw eerste naam in"
            showinfo(title='Not a Valid Input', message=bericht)

        else:

            bez_code = gallerieBezoekersCode() # pakt een random unieke user code 
            bezoekersInfo_dict[bez_naam] = [bez_email, bez_code]


            with open('bezoekers-data.txt', 'a') as f: # slaat de data op in een text bestandje, een aparte regel voor elk user
                for i, v in bezoekersInfo_dict.items():
                    f.write('{}  {}\n'.format(i, v))

            with open('bezoekers-data.txt', 'r') as f: 
                alle_bezokers = f.read()
            
            print(alle_bezokers)
            #wordt de bestandsinhoud in de console geprint, noding voor testen
            kunststukkenLijstFrame()
            
    except:
        pass
    
    
  


    
def restart_program():
    # wordt gebruikt om de programma te herstarten, zie op de merking bij de restart button
    python = sys.executable
    os.execl(python, python, * sys.argv)
    


def gHouderInfo():
    # Een locale ditctionary
    ghouder_dict = {}
    
    # Deze variables halen user entry-input en zetten die als strings in deze variables
    gH_naam = str(gHouder_naam.get())
    gH_email = str(gHouder_email.get())
    gH_postcode = str(gHouder_postcode.get())
    fn_ln = gH_naam.split() 

            
    try:
        if gH_naam == "" or gH_email == "" or gH_postcode == "": # vermijdt lege input
            bericht = "Unvalid input. Probeer nog een keer!"
            showinfo(title='Not a Valid Input', message=bericht)         

        else:
            ghouder_dict['ghouder naam'] = gH_naam
            ghouder_dict['ghouder email'] = gH_email
            ghouder_dict['ghouder postcode'] = gH_postcode
            gh_firstname = fn_ln[0]
            ghoudersInfo_dict[gh_firstname] = ghouder_dict # zet de locale dict van een enkel user, en met zijn/haar eerste naam als 'key' in die globale 
            json_gh_data = json.dumps(ghoudersInfo_dict, indent=4) # zet de data in json format
            
            with open('gallerihouder-data.json', 'w') as json_file: 
                json_file.write(json_gh_data) 
            
            print(ghouder_dict)
            print(ghoudersInfo_dict)
            # gebruikt voor testen 


            terugRegFrameFirspage()
            toonRegOfLogFrame()
        

    except:
        pass
            

def gH_inlog_info():

    # Deze variables halen user entry-input en zetten die als strings in deze variables
    gHI_naam = str(inloggennaamGhouder_entry.get())
    gHI_email = str(emailGhouder_entry.get())

    with open('gallerihouder-data.json', 'r') as json_file: 
        gh_reg_data = json.load(json_file) # Leest de registratie data die opgeslagen als json is, en zet die data om als een python dictionary

   
    try:
    
        fn_ln_in = gHI_naam.split()[0] # Pakt de first name
           
        if fn_ln_in in gh_reg_data.keys(): # Zoekt eerst in de keys van de dictionary op te zien of de eerste naam in de dict te vinden is
            if (gHI_naam == gh_reg_data[fn_ln_in]['ghouder naam']) and (gHI_email == gh_reg_data[fn_ln_in]['ghouder email']): # checkt of de volledige naam en of de email eigenlijk kloppen
                #print('IS GELUKT!') 
                #was gebruikt in de testen
                kunststukkenLijstFrame()
            else:
                bericht = "Voer de juiste data in A.U.B."
                showinfo(title='Fout!', message=bericht)
        else:
            print(ghoudersInfo_dict)
            bericht = "Voer de juiste data in A.U.B."
            showinfo(title='Fout!', message=bericht)
    

    except:
        bericht = "Voer uw naam en emailadres in A.U.B."
        showinfo(title='Not a Valid Input', message=bericht)
    



root= Tk()
root.geometry("700x250")
root.title("Rijksmuseum App")


FirstPage = Frame(master=root)
photo = PhotoImage(file= 'rm-logo.gif')
label = Label(master=FirstPage, image = photo)
label.image = photo
label.pack(side=TOP, padx=10)

#######################################################################

gh_inloggenFrame = Frame(master=root)
gh_inloggenFrame.pack(fill="both", expand=True)
inloggennaamGhouder_entry = Entry(master=gh_inloggenFrame)
emailGhouder_entry = Entry(master=gh_inloggenFrame)
inloggennaamGhouder_label = Label(master=gh_inloggenFrame, text="Naam")
emailGhouder_label = Label(master=gh_inloggenFrame, text="Email")
terug_button_gh = Button(master=gh_inloggenFrame, text="Terug", command=terugRegNaarRegofLog)
inloggenGhouder_button = Button(master=gh_inloggenFrame, text="Inloggen", command=gH_inlog_info)


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

inloggen_button3 = Button(master=regFrame, text="registreer", command=gHouderInfo)



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


Button(FirstPage, text="Restart", command=restart_program).pack(side=BOTTOM, pady=10, padx=10)
# deze button is bedoeld als een workaround een bug die optreedt wanneer je de kunststukkenlijst voor de 1e keer opent en dan ie gaat sluiten,
# dan kun je hem niet meer openen tenzij je de programma opnieuw start! we konden niet snel genoeg weten waarom dat nou gebeurd en dus maakten we dit als een oplossing.

 ########################################################################

FirstPage.pack()

root.mainloop()