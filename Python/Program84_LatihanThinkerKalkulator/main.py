# membuat kalkulator dengan GUI 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

win = tk.Tk()
win.configure(bg="white")
win.geometry("400x250")

        
def tambah(n1,n2):
    return n1 + n2
def kurang(n1,n2):
    return n1 - n2
def kali(n1,n2):
    return n1 * n2
def bagi(n1,n2):
    return n1 / n2
def pangkat(n1,n2):
    return n1 ** n2
def modulus(n1,n2):
    return n1 % n2

def hitung_otomatis(event=None):
    try:
        num1 = float(NUMP0.get())  # Ambil nilai dan konversi ke float
        num2 = float(NUMP1.get())
        operator = OPERATOR.get()

        if operator == "+":
            result = tambah(num1, num2)  # Berikan argumen
        elif operator == "-":
            result = kurang(num1, num2)  # Berikan argumen
        elif operator == "x" or operator == "*":
            result = kali(num1, num2)  # Berikan argumen
        elif operator == "/":
            result = bagi(num1, num2)  # Berikan argumen
        elif operator == "**" or operator == "xx":
            result = pangkat(num1, num2)  # Berikan argumen
        elif operator == "%":
            result = modulus(num1, num2)  # Berikan argumen
        else:
            result = "Error: Invalid operator"

        showinfo("Hasil", f"Hasil = {result}", icon='info')  # Tampilkan hasil dalam dialog info

    except ValueError:
        showinfo("Error", "Masukkan angka yang valid.")
# def focus_next_entry(event):
#     event.widget.tk_focusNext().focus()
#     return "break"

# frame input utama
inputFrame = ttk.Frame(win)
inputFrame.pack(padx=10,pady=10,fill="x",expand=True)
# color font and background on 





# input main
titleWin = ttk.Label(inputFrame, text="Kalkulator Sederhana", foreground="blue", background="lightgray", font=("Times New Roman", 16, "bold"), anchor="center")
titleWin.pack(fill="x", expand=True)

NUMP0 = tk.StringVar()
nump0 = ttk.Label(inputFrame, text="Masukan angka :", foreground="blue", background="lightgray",font=("Times New Roman", 12, "bold"), anchor="w")
nump0.pack(fill="x", expand=True)
nump00 = ttk.Entry(inputFrame, textvariable=NUMP0,foreground="green", background="lightgray",cursor="xterm", font=("Times New Roman", 12, "bold"))
nump00.pack(fill="x", expand=True)
# nump00.bind("<Return>", focus_next_entry)

OPERATOR = tk.StringVar()
numpOP = ttk.Label(inputFrame, text="Masukan Operator :", foreground="blue", background="lightgray",font=("Times New Roman", 12, "bold"), anchor="w")
numpOP.pack(fill="x", expand=True)
numpOPE = ttk.Entry(inputFrame, textvariable=OPERATOR, foreground="green", background="lightgray", cursor="xterm", font=("Times New Roman", 12, "bold"))
numpOPE.pack( fill="x", expand=True)
# numpOPE.bind("<Return>", focus_next_entry)  # Enter pindah ke field berikutnya
# numpOPE.bind("<KeyRelease>", lambda e: hitung_otomatis() if OPERATOR.get() in "+-*/" else None)


NUMP1 = tk.StringVar()
nump1 = ttk.Label(inputFrame, text="Masukan angka ke dua :", foreground="blue", background="lightgray",font=("Times New Roman", 12, "bold"), anchor="w")
nump1.pack(fill="x", expand=True)
nump11 = ttk.Entry(inputFrame, textvariable=NUMP1, foreground="green", background="lightgray", cursor="xterm", font=("Times New Roman", 12, "bold"))
nump11.pack( fill="x", expand=True)
# nump11.bind("<Return>", hitung_otomatis)

tombol = ttk.Button(inputFrame, text="Hasil", command=hitung_otomatis)
tombol.pack(fill="x", expand=True, pady=10, padx=10)


win.mainloop()