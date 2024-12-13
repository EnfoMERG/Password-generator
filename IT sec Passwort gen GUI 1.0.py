import random
import string
import re
import tkinter


def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if length < 12:
        return "Passwort sollte mindestens 12 Zeichen lang sein."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    lbAusgabe["text"] = password

def  ende():
    fenster.destroy()

labelOptions = {
    "bg": "black",  # Background Buttons
    "fg": "white", # Textfarbe Buttons
    "font": ("Elephant", 15, "bold"), # Schriftart- und Grösse
    "width": 15,
    "borderwidth": 5,
    "relief": "raised"
}

fenster = tkinter.Tk()
fenster.title("Password Generator") 
fenster.configure(bg="black") # Hintergrundfarbe des Fensters bg= Background
fenster.minsize(400, 400)

buttonOptions = {
    "bg": "#333",  # Background Buttons
    "fg": "white", # Textfarbe Buttons
    "font": ("Elephant", 15, "bold"), # Schriftart- und Grösse
    "width": 15,
    "borderwidth": 5,
    "relief": "raised"
}

lbAusgabe = tkinter.Label(fenster, text=" New Password ", **labelOptions)                  #lb = Label , Ausgabe
lbAusgabe.grid( sticky="w", padx=200, pady=50 )

buMultiplikation = tkinter.Button(fenster, text=" >> generate << ", command=generate_password, **buttonOptions)   # bu = Button, command ruft die Funktion auf !
buMultiplikation.grid(row=2, column=0, sticky="w", padx=200, pady=5)

lbAusgabe = tkinter.Label(fenster, text="", **labelOptions)                  #lb = Label , Ausgabe
lbAusgabe.grid(row=3, column=0, sticky="w", padx=200, pady=5 )

fenster.mainloop()