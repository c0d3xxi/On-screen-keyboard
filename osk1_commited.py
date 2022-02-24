from tkinter import *
from tkinter import ttk
import ttkthemes as themes

root = themes.ThemedTk()
root.get_themes()
root.geometry("1500x400")
root.set_theme('black')
root.title('On-Screen Keyboard')
root.config(bg='Black')
root.resizable(False, False)

titleLabel = Label(root, text='- On-Screen Keyboard -')
titleLabel.grid(row=0, columnspan=15)

label_last = Label(root,text="Copyright © 2022, All Rights Reserved",bg="black", fg="white")
label_last.place(relx=0.445,rely=0.95)

root.mainloop()