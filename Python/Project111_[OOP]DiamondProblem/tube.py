from pytube import YouTube

while True:
    try:
        url = input("Masukkan URL YouTube (atau ketik 'exit' untuk keluar): ")
        if url.lower() == 'exit':
            break

        yt = YouTube(url)
        print(f"\n📹 Judul Video: {yt.title}")

        # Pilih video dengan resolusi terbaik (video + audio)
        stream = yt.streams.get_highest_resolution()

        print(f"⬇️ Mulai download dengan resolusi: {stream.resolution}")
        stream.download()
        print("✅ Selesai didownload!\n")

    except Exception as e:
        print(f"❗ Terjadi kesalahan: {e}\n")
