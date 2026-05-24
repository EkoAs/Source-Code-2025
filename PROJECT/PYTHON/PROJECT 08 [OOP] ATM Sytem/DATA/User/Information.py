
class Informasi_User:
    def info_user(self, nama, noRek, pin, saldo):
        self.nama = nama
        self.noRek = noRek
        self.pin = pin
        self.saldo = saldo

    def tampil_info(self):
        print(f"Nama: {self.nama}")
        print(f"No Rekening: {self.noRek}")
        print(f"PIN: {self.pin}")
        print(f"Saldo: {self.saldo}")