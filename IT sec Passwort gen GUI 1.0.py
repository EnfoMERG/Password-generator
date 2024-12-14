import random
import string
from customtkinter import *
from PIL import Image

# Passwort-Generierung
def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        lb_output.configure(text="Länge muss eine Zahl sein!")
        return

    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    if not any([use_upper, use_digits, use_special]):
        lb_output.configure(text="Bitte mindestens eine Zeichenoption wählen!")
        return

    if length < 12:
        lb_output.configure(text="Passwort sollte mindestens 12 Zeichen lang sein.")
        return

    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    lb_output.configure(text=password)

def close_app():
    fenster.destroy()

# Farbanpassung je nach Modus
def change_text_color(color):
    lb_output.configure(text_color=color)
    chk_upper.configure(text_color=color)
    chk_digits.configure(text_color=color)
    chk_special.configure(text_color=color)
    btn_generate.configure(fg_color="#F57449", hover_color="#BBCEF9")
    btn_exit.configure(fg_color="#F57449", hover_color="#BBCEF9")

def optionmenu_callback(choice):
    if choice == "Dark Mode":
        set_appearance_mode("dark")
        change_text_color("#BBCEF9")
    else:
        set_appearance_mode("light")
        change_text_color("#474448")

# Fenster
fenster = CTk()
fenster.geometry("900x700")
fenster.title("Password Generator")
fenster.configure(bg="#BBCEF9")


# OptionMenu für Light/Dark Mode
optChoice = ["Dark Mode", "Light Mode"]
optionmenu = CTkOptionMenu(fenster, values=optChoice, command=optionmenu_callback, fg_color="#F57449", button_color="#F57449", text_color="#141204", font=("Comic Sans MS", 13))
optionmenu.place(x=760, y=29)

lb_output = CTkLabel(fenster, text="Your Password Will Appear Here", text_color="#BBCEF9", font=("Comic Sans MS", 18))
lb_output.place(relx=0.5, rely=0.2, anchor="center")

# Checkboxen
upper_var = IntVar(value=1)
digits_var = IntVar(value=1)
special_var = IntVar(value=1)

chk_upper = CTkCheckBox(fenster, text="Großbuchstaben", variable=upper_var, text_color="#BBCEF9", font=("Comic Sans MS", 15))
chk_upper.place(relx=0.3, rely=0.4, anchor="w")

chk_digits = CTkCheckBox(fenster, text="Zahlen", variable=digits_var, text_color="#BBCEF9", font=("Comic Sans MS", 15))
chk_digits.place(relx=0.3, rely=0.47, anchor="w")

chk_special = CTkCheckBox(fenster, text="Sonderzeichen", variable=special_var, text_color="#BBCEF9", font=("Comic Sans MS", 15))
chk_special.place(relx=0.3, rely=0.54, anchor="w")

# Eingabefeld für Länge
length_var = StringVar(value="12")
entry_length = CTkEntry(fenster, textvariable=length_var, width=150, font=("Comic Sans MS", 15), fg_color="white", text_color="black")
entry_length.place(relx=0.5, rely=0.65, anchor="center")

# Buttons
btn_generate = CTkButton(fenster, text=">> Generate <<", command=generate_password, fg_color="#F57449", text_color="#141204", font=("Comic Sans MS", 18), hover_color="#BBCEF9")
btn_generate.place(relx=0.5, rely=0.75, anchor="center")

btn_exit = CTkButton(fenster, text=">> Exit <<", command=close_app, fg_color="#F57449", text_color="#141204", font=("Comic Sans MS", 18), hover_color="#BBCEF9")
btn_exit.place(relx=0.5, rely=0.82, anchor="center")

# set Startmode
set_appearance_mode("dark")
fenster.mainloop()
