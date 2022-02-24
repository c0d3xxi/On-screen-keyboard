#importing modules
from tkinter import *
from tkinter import ttk
import ttkthemes as themes

#Logo Path:
logo_path="F:\programming_and_algo\python programs\On-Screen Keyboard\logo.ico"

#Defining functions:

def but_sel(value):
    if value == 'Space':
        textarea.insert(INSERT, ' ')

    elif value == 'Enter':
        textarea.insert(INSERT, '\n')

    elif value == 'Tab':
        textarea.insert(INSERT, '\t')

    elif value == 'Delete':
        textarea.delete(1.0, END)

    elif value == 'Backspace':
        i = textarea.get(1.0, END)
        newtext = i[:-2]

        textarea.delete(1.0, END)
        textarea.insert(INSERT, newtext)

#Variable for rows = varR and columns = varC

    elif value == 'Shift On':
        varR = 2
        varC = 0

        for button in ShiftOnButtons:

            command = lambda x=button: but_sel(x)
            if button != 'Space':
                ttk.Button(root, text=button, command=command, width=14, ).grid(row=varR, column=varC)

            varC += 1
            if varC > 14:
                varC = 0
                varR += 1

    elif value == 'Shift Off':
        varR = 2
        varC = 0

        for button in buttons:

            command = lambda x=button: but_sel(x)
            if button != 'Space':
                ttk.Button(root, text=button, command=command, width=14, ).grid(row=varR, column=varC)

            varC += 1
            if varC > 14:
                varC = 0
                varR += 1

    elif value == 'Caps Lock':

        varR = 2
        varC = 0

        for button in capsButtons:

            command = lambda x=button: but_sel(x)
            if button != 'Space':
                ttk.Button(root, text=button, command=command, width=14, ).grid(row=varR, column=varC)

            varC += 1
            if varC > 14:
                varC = 0
                varR += 1

    elif value == 'CAPS LOCK':

        varR = 2
        varC = 0

        for button in buttons:

            command = lambda x=button: but_sel(x)
            if button != 'Space':
                ttk.Button(root, text=button, command=command, width=14, ).grid(row=varR, column=varC)

            varC += 1
            if varC > 14:
                varC = 0
                varR += 1


    else:
        textarea.insert(INSERT, value)

    textarea.focus_set()

#Main root window

root = themes.ThemedTk()
root.get_themes()
root.geometry("1500x400")
root.set_theme('black')
root.title('On-Screen Keyboard')
root.iconbitmap(logo_path)
root.config(bg='Black')
root.resizable(False, False)

titleLabel = Label(root, text='- On-Screen Keyboard -', font=('Lucida Calligraphy', 20, 'bold'), bg='Black', fg='Grey')
titleLabel.grid(row=0, columnspan=15)

#screen

textarea = Text(root, bg="black", fg="white",font=('Lucida Console', 14, 'bold'), height=10, width=120, wrap='word',bd=10,relief=SUNKEN)
textarea.grid(row=1, columnspan=15)
textarea.focus_set()

#buttons

buttons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace', 'Delete',
           'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', '7', '8', '9',
           'Caps Lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'Enter', '4', '5', '6',
           'Shift On', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift Off', '1', '2', '3',
           'Space']

ShiftOnButtons = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Backspace', 'Delete',
                    'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', ']', '7', '8', '9',
                    'Caps Lock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', 'Enter', '4', '5', '6',
                    'Shift On', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', 'Shift Off', '1', '2', '3',
                    'Space'

                    ]

capsButtons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace', 'Delete',
               'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', '7', '8', '9',
               'CAPS LOCK', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', 'Enter', '4', '5', '6',
               'Shift On', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift Off', '1', '2', '3',
               'Space']

varR = 2
varC = 0

for button in buttons:

    command = lambda x=button: but_sel(x)
    if button != 'Space':
        ttk.Button(root, text=button, command=command, width=14).grid(row=varR, column=varC)

    if button == 'Space':
        ttk.Button(root, text=button, command=command, width=150).grid(row=6, column=0, columnspan=14)

    varC += 1
    if varC > 14:
        varC = 0
        varR += 1

label_last = Label(root,text="Copyright © 2022, All Rights Reserved",bg="black", fg="white")
label_last.place(relx=0.445,rely=0.95)

root.mainloop()