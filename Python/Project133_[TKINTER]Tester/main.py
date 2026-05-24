import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def listRumus():
    print("1. Kalkulator ")
    print("1. Kalkulator ")
    print("1. Kalkulator ")
    print("1. Kalkulator ")

win = tk.Tk()
win.configure(bg="white")
# win.geometry("400x250")
win.title("Tkinter Tester")

inputFrame = ttk.Frame(win)
inputFrame.pack(padx=10,pady=10,fill="x",expand=True)
# bagian pilihan operator
kalkulatorMode = ttk.Button(inputFrame, text="Hasil", command=listRumus)
kalkulatorMode.pack(fill="x", expand=True, pady=10, padx=10)
# agar hasil printnya di tampilkan juga di tkinter
 


listRumus()
win.mainloop()