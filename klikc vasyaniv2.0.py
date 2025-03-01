from tkinter import *
from tkinter import ttk

def lvl():
    global xp

def sdorove():
    global sdorovi
    sdorovi-=1
    sdorovie['text']= f'tvoe sdorovie: {sdorovi}'

def clear_window():
    for widget in root. winfo_children():
        if not isinstance(widget, Menu):
            widget.destroy()

def naviki():
    clear_window()
    opot=Label(root,text='Опыт: 10')
    opot.grid(row=1, column=0)
    sila=Label(root,text='Сила')
    sila.grid(row=2, column=0)
    lovkost=Label(root,text='Ловкость')
    lovkost.grid(row=3, column=0)
    inteleckt=Label(root,text='Интелект')
    inteleckt.grid(row=4, column=0)
    opot_p=ttk.Button(root,text='+')
    opot_p.grid(row=1, column=1)
    sila_p=ttk.Button(root,text='+')
    sila_p.grid(row=2, column=1)
    lovkost_p=ttk.Button(root,text='+')
    lovkost_p.grid(row=3, column=1)
    intelekt_p=ttk.Button(root,text='+')
    intelekt_p.grid(row=4, column=1)
root = Tk()
root.title("masyany")
root.geometry("1200x1200")
 
btn = ttk.Button(root,text='нажми', command=sdorove)
btn.pack()

sdorovi=10


sdorovie=Label(root, text="10")
sdorovie.pack()
 
file_menu = Menu()
file_menu.add_command(label="Новое")
file_menu.add_command(label="Сохронить")
file_menu.add_command(label="Открыть")
file_menu.add_separator()
file_menu.add_command(label="Вход")

person=Menu()
person.add_command(label='навыки', command=naviki)

main_menu = Menu()
main_menu.add_cascade(label="Игра", menu=file_menu)
main_menu.add_cascade(label="Персонаж", menu=person)
main_menu.add_cascade(label="Настройки")
 
root.config(menu=main_menu)

root.mainloop()
