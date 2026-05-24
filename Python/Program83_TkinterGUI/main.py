# pengenalan tkinter
# GUI adalah graphical user interface
import tkinter as tk
from tkinter import ttk #  munggunakan ttk  
from tkinter.messagebox import showinfo # show info adalah tempat memberikan notifikasi lewat tampilan yang berbeda 

# gui nya mau dikasih apa
# bikin objek yang namanya window
# Ini bagian init
window = tk.Tk()
window.configure(bg="white") # tempat edit edit
window.geometry("300x300") # ukuran 
window.resizable(False, False) #agar tidak bisa di perbesar dan di perkecil ukurannya
window.title("Halo Dunia")

# variable dan input
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Tombol
def tombolClick(): # fungsi ini akan dipanggil oleh tombol
    # print(f"HALO {NAMA_BELAKANG.get()}") # hasil muncul di terminal
    # print(NAMA_BELAKANG.get()) # wajib menggunakan dot .get() untuk memanggil isi data
    pesan = f"Haloo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteng"
    showinfo(title="WOi halo",message=pesan)



# membuat frame input
inputF = ttk.Frame(window)
# penempatan grid, pack, place
# menggunkan place. berurutan dari atas ke bawah
inputF.pack(padx=10,pady=10,fill="x", expand=True) # kalo x ke kanan dan y ke bawah
# komponen komponen
# 1. label untuk lama depna
namaDepanL = ttk.Label(inputF, text="Nama Depan")
namaDepanL.pack(fill="x", expand=True)
# 2. entry untuk nama depan
namadepanE = ttk.Entry(inputF, textvariable=NAMA_DEPAN)
namadepanE.pack(padx=10,fill="x", expand=True)
# 3. label untuk nama belakang
namaBelakangL = ttk.Label(inputF, text="Nama Belakang")
namaBelakangL.pack(fill="x", expand=True)
# 4. entry untuk nama depan
namaBelakangE = ttk.Entry(inputF, textvariable=NAMA_BELAKANG)
namaBelakangE.pack(padx=10,fill="x", expand=True)
# tombol
tombolSapa = ttk.Button(inputF, text="SApa!",command=tombolClick)
tombolSapa.pack(fill='x',expand=True,pady=10, padx=10)


# untuk membuat program muter2 terus
window.mainloop()
# cuma butuh 3 command untuk munculin gui
