import customtkinter
import tkinter as tk






customtkinter.set_appearance_mode("dark-blue")

root = customtkinter.CTk()
root.title("calculator")
root.geometry("240x225")

equesion = ""

def add_math(symbol):
    global equesion
    equesion += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, equesion)

def read_equesion():
    global equesion
    try:
        equesion = str(eval(equesion))
        result.delete(1.0, "end")
        result.insert(1.0, equesion)
    except:
        clear_text()
        result.insert(1.0, "arithmetic error")

def clear_text():
    global equesion
    equesion = ""
    result.delete(1.0, "end")

"""-----------------------------display-----------------------------"""

result = customtkinter.CTkTextbox(root, height=90)
result.grid(columnspan=4)

"""------------------------------keypad------------------------------"""

button_1 = customtkinter.CTkButton(root, text="1", command=lambda: add_math("1") ,width=60)
button_1.grid(row=1, column=0)

button_2 = customtkinter.CTkButton(root, text="2", command=lambda: add_math("2") ,width=60)
button_2.grid(row=1, column=1)

button_3 = customtkinter.CTkButton(root, text="3", command=lambda: add_math("3") ,width=60)
button_3.grid(row=1, column=2)

button_4 = customtkinter.CTkButton(root, text="4", command=lambda: add_math("4") ,width=60)
button_4.grid(row=2, column=0)

button_5 = customtkinter.CTkButton(root, text="5", command=lambda: add_math("5") ,width=60)
button_5.grid(row=2, column=1)

button_6 = customtkinter.CTkButton(root, text="6", command=lambda: add_math("6") ,width=60)
button_6.grid(row=2, column=2)

button_7 = customtkinter.CTkButton(root, text="7", command=lambda: add_math("7") ,width=60)
button_7.grid(row=3, column=0,)

button_8 = customtkinter.CTkButton(root, text="8", command=lambda: add_math("8") ,width=60)
button_8.grid(row=3, column=1,)

button_9 = customtkinter.CTkButton(root, text="9", command=lambda: add_math("9") ,width=60)
button_9.grid(row=3, column=2,)

button_0 = customtkinter.CTkButton(root, text="0", command=lambda: add_math("0") ,width=60)
button_0.grid(row=4, column=1,)

"""----------------------------operetions----------------------------"""

add = customtkinter.CTkButton(root, text="+", command=lambda: add_math("+")  ,width=60 ,fg_color="#f26400")
add.grid(row=1, column=3)

sub = customtkinter.CTkButton(root, text="-", command=lambda: add_math("-")  ,width=60 ,fg_color="#f26400")
sub.grid(row=2, column=3)

mul = customtkinter.CTkButton(root, text="*", command=lambda: add_math("*") ,width=60 ,fg_color="#f26400")
mul.grid(row=3, column=3)

div = customtkinter.CTkButton(root, text="%", command=lambda: add_math("/") ,width=60 ,fg_color="#f26400")
div.grid(row=4, column=3)

fin = customtkinter.CTkButton(root, text="=", command=read_equesion ,width=60 ,fg_color="#f26400")
fin.grid(row=4, column=2)

dell = customtkinter.CTkButton(root, text="clear", command=clear_text ,width=60 ,fg_color="red")
dell.grid(row=4, column=0)

root.mainloop()