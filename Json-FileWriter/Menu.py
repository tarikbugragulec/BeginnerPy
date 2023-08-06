import display,CityPeopleNumber
from tkinter import *
import tkinter as tk
from WriteToFile import ToFile

def ClickEv(event):
    if enttr1.get() == "Değer Girin":
        enttr1.delete(0, END)
        enttr1.config(fg="black")

def FocusOut(event):
    if enttr1.get() == "":
        enttr1.config(fg="gray")
        enttr1.insert(0, "Değer Girin")

class Komutlar:
    def button1_Click():
        CityPeopleNumber.metod()

    def button2_Click():
        display.metod1()    
  
    def button3_Click():
        dosyaadi = enttr1.get()
        if dosyaadi == "":
            lbl_warning.config(text="Değer girin!", fg="red")
        else:
            ToFile(dosyaadi)
            lbl_warning.config(text="Dosya oluşturuldu.", fg="green")


root = tk.Tk()
root.geometry("800x600")
root.title("Giriş")

frame1 = tk.Frame(root, bg="white") 
frame1.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relheight=0.7, relwidth=0.8)

label1 = tk.Label(frame1, text="Dosya Adı=")
label1.grid(row=0, column=1, padx=5, pady=10)

enttr1 = tk.Entry(frame1, fg="gray")
enttr1.insert(0, "Değer Girin")
enttr1.grid(row=0, column=2, padx=5, pady=10)
enttr1.bind("<FocusIn>", ClickEv)
enttr1.bind("<FocusOut>", FocusOut)

lbl_warning = tk.Label(frame1, text="", fg="red")

button1 = tk.Button(frame1, text="City/Human Statistic", padx=20, pady=10, command=Komutlar.button1_Click)
button2 = tk.Button(frame1, text="Age,People Statistic", padx=20, pady=10, command=Komutlar.button2_Click)
button3 = tk.Button(frame1, text="Write To File", padx=20, pady=10, command=Komutlar.button3_Click)
button4 = tk.Button(frame1, text="Exit", padx=20, pady=10, command=root.destroy)

button1.grid(row=1, column=0, padx=5, pady=10)
button2.grid(row=1, column=1, padx=5, pady=10)
button3.grid(row=1, column=2, padx=5, pady=10)
button4.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
lbl_warning.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)

root.mainloop()
