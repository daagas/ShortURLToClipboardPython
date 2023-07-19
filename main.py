#No funciona, pyshorteners y clipboard han dejado de estar dispobibles...
import pyshorteners
import tkinter as tk
from tkinter import ttk
from tkinter .messagebox import showinfo
import clipboard

win = tk.Tk()
win.title("URL shortener")

def short():
    url = entry_url.get()
    shorted_url = pyshorteners.Shortener()
    showinfo("Shorted url",f"{shorted_url.tinyurl.short(url)}")
    clipboard.copy(f"{shorted_url.tinyurl.short(url)}")

url_label = tk.Label(win,text="Enter URL here: ")
url_label.grid(row=0,column=0)

entry_url = tk.Entry(win,width=30,bg="#69BEF6",bd=2)
entry_url.grid(row=0,column=2,padx=5,pady=5)

button = ttk.Button(win,text="Short",command=short)
button.grid(row=1,column=0,columnspan=2)

win.mainloop()