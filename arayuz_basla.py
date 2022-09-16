from asyncore import write
from cgitb import text
from tkinter import *
from tkinter import messagebox
from turtle import color
from webbrowser import get
from PIL import *
import random
from playsound import playsound
import time
import math

tk =Tk()

tk.geometry("520x320+450+200")
tk.title("Giriş Ekranı")


'''resim = ImageTk.PhotoImage(Image.open("/home/maxwell/Masaüstü/spyhackerz.ico"))
Label(image=resim).pack()
'''


selam = Label(text="selamlar",bg="cyan")
selam.pack()

entrybir = Entry(width=30)
write = Label(text="Email or Username")
write.pack()
entrybir.pack()

entryiki = Entry(textvariable=StringVar(),show="*",width=30)
writeiki = Label(text="Password")
writeiki.pack()
entryiki.pack()

def buton():
    mail = entrybir.get()
    psw = entryiki.get()
    if mail == 'admin' and psw =='3131':
        x = messagebox.showinfo("Giriş Yapıldı","Başarıyla Giriş Yaptınız :)")
        tk.destroy()
        hesap =Tk()
        hesap.resizable(width=False,height=False)

        hesap.geometry("820x520+300+150")
        hesap.title("Hesapla Makinesi")

        selam = Label(text="Hesapla Gitsin",font=("Times 24"))
        selam.pack()

        words = ("PUHAHAHAHAHAAHAHHAAHAHAH","Eline Kuvvet","Anime Kızları Gerçek Mi?")


        entry1 = Entry(width=30)
        write = Label(text="1. Sayıyı Giriniz:")
        write.pack()
        entry1.pack()

        entry2 = Entry(width=30)
        write = Label(text="2. Sayıyı Giriniz:")
        write.pack()
        entry2.pack()

        entry3 = Label(text="-------------",font=("Arial 14 bold",25),bg="gray")
        entry3.place(x=430,y=230)

        esittir = Label(text="=",font=("Arial 14 bold",55))
        esittir.place(x= 340,y=205)

        def topla():
            try:
            
                ilk_deger = int((entry1.get()))
                ikinci_deger = int((entry2.get()))
                sonuc = ilk_deger + ikinci_deger
                
                
            
                if sonuc == 31:
                    entry3.config(text=random.choice(words))
                elif sonuc >999999999:
                    liste = []
                    liste.append(sonuc)
                    entry3.config(text=liste[0:1])

                else:
                    entry3.config(text=sonuc)
            except ValueError:
                entry3.config(text="Sadece Sayı Girin!")
                
            except ZeroDivisionError:
                entry3.config(text="Sıfırla Ne İşin Var Kıro!")
        def cıkar():
            try:
                ilk_deger = int(entry1.get())
                ikinci_deger = int(entry2.get())
                sonuc = ilk_deger - ikinci_deger
                if sonuc == 31:
                    entry3.config(text=random.choice(words))
                else:
                    entry3.config(text=sonuc)
            except ValueError:
                entry3.config(text="Sadece Sayı Girin!")
            except ZeroDivisionError:
                entry3.config(text="Sıfırla Ne İşin Var Kıro!")

        def carp():
            try:
                ilk_deger = int(entry1.get())
                ikinci_deger = int(entry2.get())
                sonuc = ilk_deger * ikinci_deger

            
                if sonuc == 31:
                    entry3.config(text=random.choice(words))
                else:
                    entry3.config(text=sonuc)
            except ValueError:
                entry3.config(text="Sadece Sayı Girin!")
            except ZeroDivisionError:
                entry3.config(text="Sıfırla Ne İşin Var Kıro!")


        def bol():
            try:
                ilk_deger = int(entry1.get())
                ikinci_deger = int(entry2.get())
                sonuc = ilk_deger / ikinci_deger

            
                if sonuc == 31:
                    entry3.config(text=random.choice(words))
                    time.sleep(2)
                    playsound('/home/maxwell/İndirilenler/Beter.mp3')
                else:
                    entry3.config(text=sonuc)
            except ValueError:
                entry3.config(text="Sadece Sayı Girin!")
            except ZeroDivisionError:
                entry3.config(text="Sıfırla Ne İşin Var Kıro!")

        def factor():
            try:
                ilk_deger = math.factorial(int(entry1.get()))
                ikinci_deger = math.factorial(int(entry2.get()))

                sonuc = ilk_deger + ikinci_deger

                entry3.config(text=sonuc)

            except ValueError:
                messagebox.showerror("Value Eror","Lütfen Her yeri eksiksiz ve doğru doldurun")

        def btn_us():
            pass
        
        btn_topla =Button(

                text="+",
                padx="30",
                pady="25",
                bg="#FF99CC",
                command=topla
        )   

        btn_cıkar =Button(

                text="-",
                padx="32.5",
                pady="27",
                bg="#999900",
                command=cıkar

        )

        btn_carp =Button(

                text="*",
                padx="32",
                pady="27",
                bg="magenta",
                command=carp

        )
        btn_bol =Button(

                text="/",
                padx="32",
                pady="27",
                bg="#FF3333",
                command=bol
        )

        btn_factor = Button(
            text="!",
            padx="32",
            pady="27",
            bg="#66FF66",
            command=factor

        )

        btn_us = Button(
            text="Üs",
            padx="29",
            pady="26",
            bg="#006600"

        )

        btn_topla.place(x=140,y=150)
        btn_cıkar.place(x=140,y=250)
        btn_carp.place(x=240,y=150)
        btn_bol.place(x=240,y=250)
        btn_factor.place(x=240,y=350)
        btn_us.place(x=136,y=350)

        hesap.mainloop()

    else:
        messagebox.showwarning("Hata","Kullanıcı Adı ya da Şifre Hatalı!")

def uyari():
    messagebox.showwarning("404 Not Found ","Hemen Halledip Geliyoruz :)")

btn = Button(
            text="Log In",
            padx="30",
            pady="25",
            bg="yellow",
            command=buton
            
) 
btn.pack()
tk.mainloop()
