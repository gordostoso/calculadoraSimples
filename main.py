import customtkinter
import tkinter as tk






customtkinter.set_appearance_mode("dark-blue")

root = customtkinter.CTk()
root.title("calculator")
root.geometry("240x300")

def button_callback():
    print("button pressed")

"""-----------------------------display-----------------------------"""

result = customtkinter.CTkTextbox(root, height=90)
result.grid(columnspan=4)

"""------------------------------keypad------------------------------"""

button_1 = customtkinter.CTkButton(root, text="1", command=button_callback ,width=60)
button_1.grid(row=1, column=0)

button_2 = customtkinter.CTkButton(root, text="2", command=button_callback ,width=60)
button_2.grid(row=1, column=1)

button_3 = customtkinter.CTkButton(root, text="3", command=button_callback ,width=60)
button_3.grid(row=1, column=2)

button_4 = customtkinter.CTkButton(root, text="4", command=button_callback ,width=60)
button_4.grid(row=2, column=0)

button_5 = customtkinter.CTkButton(root, text="5", command=button_callback ,width=60)
button_5.grid(row=2, column=1)

button_6 = customtkinter.CTkButton(root, text="6", command=button_callback ,width=60)
button_6.grid(row=2, column=2)

button_7 = customtkinter.CTkButton(root, text="7", command=button_callback ,width=60)
button_7.grid(row=3, column=0,)

button_8 = customtkinter.CTkButton(root, text="8", command=button_callback ,width=60)
button_8.grid(row=3, column=1,)

button_9 = customtkinter.CTkButton(root, text="9", command=button_callback ,width=60)
button_9.grid(row=3, column=2,)

button_0 = customtkinter.CTkButton(root, text="0", command=button_callback ,width=60)
button_0.grid(row=4, column=1,)

"""----------------------------operetions----------------------------"""

add = customtkinter.CTkButton(root, text="+", command=button_callback ,width=60)
add.grid(row=1, column=3)

sub = customtkinter.CTkButton(root, text="-", command=button_callback ,width=60)
sub.grid(row=2, column=3)

mul = customtkinter.CTkButton(root, text="*", command=button_callback ,width=60)
mul.grid(row=3, column=3)

div = customtkinter.CTkButton(root, text="%", command=button_callback ,width=60)
div.grid(row=4, column=3)

fin = customtkinter.CTkButton(root, text="=", command=button_callback ,width=60)
fin.grid(row=4, column=2)

root.mainloop()