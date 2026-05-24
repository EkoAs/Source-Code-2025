import pygame

# bagian init 
# init itu kayak bikin dunia atau kt=rakternya

# struktur dasar game
# init # bikin dunia
# user input, data base input # masukan input dari stick atau mouse
# laluu update assetnya # update aset dari user input
# render ke display # proses paling berat

# bagian init
pygame.init()  # inisialisasi pygame

# variable running game

isrun = True  # kondisi untuk menjalankan game



#  membuat display surface object # menaruh semua yang kit buat
windowlebar = 500
windowpanjang = 500
window = pygame.display.set_mode((windowlebar, windowpanjang))  # ukuran window 500x500

# objek game
# kordinat x dan y / posisi
x = 250
y = 250

# ukkuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 2 # piksel per detik






while isrun:
    pygame.time.delay(10)  # delay untuk mengatur kecepatan game, 10 milidetik
    #  lokasi user input
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrun = False
            
            
    # ambil semua keyboarf press
    keys = pygame.key.get_pressed()  # mengambil semua tombol yang ditekan
    # ambil ke kiri 
    if keys[pygame.K_LEFT] and x > 0:  # jika tombol kiri ditekan dan x lebih besar dari 0
        x -= speed  # kurangi x dengan kecepatan
    # ambil ke kanan
    if keys[pygame.K_RIGHT] and x < windowlebar - lebar:  # jika tombol kanan ditekan dan x kurang dari 500 - lebar
        x += speed  # tambahkan x dengan kecepatan
    # ambil ke bawah 
    if keys[pygame.K_DOWN] and y < windowpanjang - panjang:  # jika tombol bawah ditekan dan y kurang dari 500 - panjang
        y += speed  # tambahkan y dengan kecepatan
    # ambil ke atas
    if keys[pygame.K_UP] and y > 0:  # jika tombol atas ditekan dan y lebih besar dari 0
        y -= speed  # kurangi y dengan kecepatan
    # 

    # update game state
    window.fill((255,255,255))  # mengisi layar dengan warna putih
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))  # menggambar persegi panjang merah
    # render
    pygame.display.update()  # memperbarui tampilan

pygame.quit()  # keluar dari pygame








