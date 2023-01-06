from tkinter import *
import pyautogui, pyperclip, keyboard
import time

window = Tk()
window.title("Source Generator")
window.geometry('500x300')

authorEntry = Entry(window, width=20)
authorLabel = Label(window, text="Автор")

nameEntry = Entry(window, width=20)
nameLabel = Label(window, text="Назва")

linkEntry = Entry(window, width=20)
linkLabel = Label(window, text="Посилання")

yearEntry = Entry(window, width=20)
yearLabel = Label(window, text="Рік")

sourcelabel = Label(window, text="Тут текст посилання", wraplength=400)

def nonTake():
	text = f"{authorEntry.get()}. {nameEntry.get()}. ({yearEntry.get()}) [Електронний ресурс]. – Режим доступу: {linkEntry.get()} - Назва з екрана;"
	pyperclip.copy(text)
	authorEntry.delete(0, END)
	nameEntry.delete(0, END)
	linkEntry.delete(0, END)
	yearEntry.delete(0, END)
	sourcelabel.config(text=text)


	
buttonCopy = Button(window, text="Створити", command=nonTake)

authorLabel.grid(column=0, row=0)
authorEntry.grid(column=1, row=0)

nameLabel.grid(column=0, row=1)
nameEntry.grid(column=1, row=1)

linkLabel.grid(column=0, row=2)
linkEntry.grid(column=1, row=2)

yearLabel.grid(column=0, row=3)
yearEntry.grid(column=1, row=3)

buttonCopy.grid(column=0, row=4)
sourcelabel.grid(column=2, row=5)



window.mainloop()
