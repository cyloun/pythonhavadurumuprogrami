import requests
import json
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
import customtkinter
import _thread as thread

myApiKey = "2889d0108e7f6c8f2d12b3dda48e73cb"
url = "https://api.openweathermap.org/data/2.5/weather"

tk = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
tk.title("Hava Durumu || MR. Cyloun")
tk.geometry("300x200")
tk.resizable(0,0)


def HavaDurumu():
    try:    
        şehir = EntryGiris.get()
        parametre = {'q':şehir,'appid':myApiKey,'lang':'tr'}
        bilgi = requests.get(url,params=parametre).json()       
     
        sehir = bilgi["name"]
        sıcaklık = bilgi['main']['temp'] - 273
        durum = bilgi['weather'][0]['description']
        icon = bilgi['weather'][0]['icon']

        # şehirAdıLabel['text'] = "Şehir Adı: {}".format(sehir.title())
        # sıcaklıkLabel['text'] = "Mevcut Sıcaklık: {}°".format(int(sıcaklık))
        # durumLabel['text'] = "Hava bugün {}.".format(durum.title())

        if sehir:
            şehirAdıLabel.configure(text="Şehir Adı: {}".format(sehir.title()))
        if sıcaklık:
            sıcaklıkLabel.configure(text="Mevcut Sıcaklık: {}°".format(int(sıcaklık)))
        if durum:
            durumLabel.configure(text="Hava bugün {}.".format(durum.title()))
        if icon:
            iconLink = "http://openweathermap.org/img/wn/{}@2x.png".format(icon)
            resim = customtkinter.CTkImage(light_image=Image.open(requests.get(iconLink,stream=True).raw),
                                  dark_image=Image.open(requests.get(iconLink,stream=True).raw),
                                  size=(100,100))
            fotoLabel.configure(image=resim)
            fotoLabel.image = resim
            

        return (sehir,sıcaklık,durum,icon,iconLink,resim)
    except KeyError:
        messagebox.showerror("Hata!","Lütfen girildilerden emin olunuz!")
    else:
        pass

EntryGiris = customtkinter.CTkEntry(master=tk,justify="center")
EntryGiris.pack(fill=BOTH,ipady=6,padx=5,pady=5)
EntryGiris.focus()
ButonIsleyici = customtkinter.CTkButton(master=tk,text="Arama",command=HavaDurumu)
ButonIsleyici.place(x=150,y=65,anchor=tkinter.CENTER)

şehirAdıLabel = customtkinter.CTkLabel(master=tk,justify="center",text="")
şehirAdıLabel.place(x=10,y=100)
sıcaklıkLabel = customtkinter.CTkLabel(master=tk,text="")
sıcaklıkLabel.place(x=10,y=125)
durumLabel = customtkinter.CTkLabel(master=tk,text="")
durumLabel.place(x=10,y=150)
fotoLabel = customtkinter.CTkLabel(master=tk,text="")
fotoLabel.place(x=190,y=90)

tk.mainloop()
