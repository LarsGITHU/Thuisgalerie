import http.client, urllib.parse, json
import json
from tkinter import *
from webbrowser import *

root = Tk()
kunststFrame = Frame(master=root)
root.title("Rijksmuseum kunststukken")

def openlink():
    open("https://www.rijksmuseum.nl/nl/tickets/artikelen")



def informatie():
    s = Button(kunststFrame, text="Quit", command=root.destroy).pack(side=BOTTOM)
    ButtonNaardewebsite = Button(master=kunststFrame, text= "kaartje kopen", command=openlink).pack(side=BOTTOM)

    
    werkstukken_dict = {}
    key = 'Ostta0g5'

    try:
        conn = http.client.HTTPSConnection('www.rijksmuseum.nl')
        req = "/api/nl/collection?key=" + key + "&format=json&ps=20&p=2"
        conn.request("GET", req)

        response = conn.getresponse()
        responsetext = response.read()
        conn.close()
        resjson = json.loads(responsetext)
   # print(informatie(resjson))
        artobject= resjson['artObjects']
        for object in artobject:
            werkstukken_dict[object['longTitle']] =  (object['webImage']['url'])

    except Exception as e:
        print(f"Fout: {e.errno} {e.strerror}")


    result =[]
    eval_link = lambda x: (lambda e: open(x))
    for key in werkstukken_dict:
        value = werkstukken_dict[key]
        print(key,value)
        result.append(Label(kunststFrame, text=key, fg="blue", cursor="hand2"))
        result[-1].bind("<Button-1>", eval_link(value))
#    for i in range(10):
#        result[-1].bind("<Button-1>", lambda e: open(value))
        result[-1].pack()
    
    kunststFrame.pack()
    return root.mainloop()

informatie()